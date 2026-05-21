# Numba (LLVM JIT) Optimization for Ray Tracer

## Goal

Speed up the render loop by compiling the per-pixel math to native machine code via Numba's LLVM JIT.

## Results

| Canvas Size | Original (Python + Pool) | Numba (after warmup) | Speedup |
|---|---|---|---|
| 1000x1000 | ~17s | ~0.08s render + save | ~200x |

The Numba-compiled render at 1000x1000 takes **0.08s**. The remaining time is file I/O, which was further optimized with P6 binary PPM output.

## Why

The bottleneck was Python object overhead -- every pixel creates multiple `CustomTuple`, `Ray`, and `ColorTuple` objects. The actual math (dot products, normalize, quadratic solve) is trivial float arithmetic buried under:

- Object allocations and garbage collection
- Method dispatch and attribute lookups
- Reference counting

## Approach

Two-layer architecture:

```
┌─────────────────────────────┐
│  Existing code              │  CustomTuple, Ray, Sphere, etc.
│  (object layer)             │  Stays exactly as-is
│  Used for: tests, clarity   │
└──────────────┬──────────────┘
               │ calls into
┌──────────────▼──────────────┐
│  Numba kernel               │  Raw floats only
│  (math layer)               │  Compiled by LLVM via @njit
│  Used for: fast rendering   │
└─────────────────────────────┘
```

Existing objects are untouched. The Numba path duplicates the math using raw floats, and the **entire hot loop** (not just individual helpers) must be inside `@njit` for the speedup to apply.

## Key Constraint

`@njit` functions can only use: floats, ints, tuples, numpy arrays. No custom Python objects.

## Functions (in `scripts/numba_test.py`)

### Completed

| Function | Description |
|---|---|
| `dot` | 3D dot product from 6 floats |
| `normalize` | Vector normalization, returns (x, y, z) tuple |
| `intersect_sphere` | Ray-sphere intersection via quadratic formula. Takes ray origin/direction + 4x4 inverse transform as numpy array. Returns (t1, t2) or (-1, -1) for miss |
| `normal_at_sphere` | Surface normal at a hit point. Uses inverse transform for object-space conversion and transpose(inverse) for world-space normal |
| `lighting_phong` | Phong shading: ambient + diffuse + specular. Takes material properties, light position/intensity, hit point, eye vector, normal as raw floats |
| `render_row_numba` | Single-row pixel loop. Compiles the inner `for x` loop with all math |
| `render_image_numba` | Full image render. Both `for y` and `for x` loops compiled to native code. Returns a `(canvas_pixels, canvas_pixels, 3)` numpy array. Canvas size is configurable at runtime |

### File I/O (in `scripts/draw_sphere_numba.py`)

| Function | Description |
|---|---|
| `save_ppm_from_array` | P3 (text) PPM output with clamping and 70-char line wrapping. Correct but slow (~0.7s for 1000x1000) |
| `save_ppm_p6` | P6 (binary) PPM output. Uses `np.clip` + `astype(uint8)` + `tobytes()` for near-instant save. Raw bytes, no formatting needed |

## Scripts

| Script | Description |
|---|---|
| `scripts/numba_test.py` | All `@njit` functions + unit tests comparing against existing Python implementations |
| `scripts/draw_sphere.py` | Original renderer (Python + multiprocessing Pool) |
| `scripts/draw_sphere_numba.py` | Numba renderer with P6 save |
| `scripts/render_gallery.py` | Side-by-side comparison: original vs numba for all sphere variants |

## How to Test

Each Numba function is tested against the existing Python implementation with the same inputs:

```bash
PYTHONPATH=. uv run python scripts/numba_test.py
```

## Warmup

The first call to any `@njit` function triggers LLVM compilation (~1-2s). Use a 1x1 canvas warmup call before timing:

```python
render_image_numba(1, ...)  # compiles with tiny workload
render_image_numba(1000, ...)  # runs at full speed
```

Numba compiles based on **types**, not values -- so a 1x1 warmup produces the same machine code as a 4000x4000 render.

## Memory Usage

The numpy array is stored entirely in RAM:

| Canvas Size | float64 array | Peak during P6 save |
|---|---|---|
| 1,000 x 1,000 | 24 MB | ~72 MB |
| 4,000 x 4,000 | 384 MB | ~1.2 GB |
| 10,000 x 10,000 | 2.4 GB | ~7.2 GB |

Peak is ~3x the array size during save due to temporary copies from `np.clip` and `astype`.

## Next Steps

| Step | Description |
|---|---|
| `@njit(cache=True)` | Cache compiled code to disk to avoid recompilation on every run |
| `prange` for large images | `@njit(parallel=True)` with `prange` for the outer loop. Not worth it at 1000x1000 (thread overhead > render time) but helps at 4000+ |
| Multi-sphere support | Current kernel handles a single sphere. Extend to loop over multiple spheres and pick the closest hit |
| In-place save optimization | Use `np.clip(image, 0, 1, out=image)` and `image *= 255` to avoid temporary copies during save |

## Key Lessons

1. Compiling individual functions but calling them from a Python loop gains almost nothing -- the Python loop overhead dominates
2. The entire hot loop must be inside `@njit`
3. Points (w=1) include the translation column (`inv[row, 3]`) in matrix multiply; vectors (w=0) do not
4. Normal computation uses `transpose(inverse) * normal`, not `inverse * normal` -- index swap: `inv[j,i]` instead of `inv[i,j]`
5. All return paths in an `@njit` function must return the same type
6. The reflect formula is `incoming - normal * 2 * dot(incoming, normal)` -- the dot is with the **normal**, not the light direction
7. Numba can't access module-level globals inside `@njit` -- pass constants (like `WALL_Z`) as parameters or hardcode them
8. Use numpy arrays (not lists of tuples) for output from `@njit` functions -- Numba handles them natively
9. After optimizing compute, the bottleneck shifts to I/O -- P6 binary PPM is orders of magnitude faster than P3 text
10. A numpy array is a flat contiguous memory block -- `tobytes()` dumps it directly, matching P6's expected byte layout
11. `prange` has thread management overhead that can exceed the render time for small workloads -- profile before parallelizing
