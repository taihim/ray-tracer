# Numba (LLVM JIT) Optimization for Ray Tracer

## Goal

Speed up the render loop in `render_gallery.py` by compiling the per-pixel math to native machine code via Numba's LLVM JIT.

## Why

A 400x400 render takes ~3s. The bottleneck is Python object overhead -- every pixel creates multiple `CustomTuple`, `Ray`, and `ColorTuple` objects. The actual math (dot products, normalize, quadratic solve) is trivial float arithmetic buried under:

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

### Still To Do

| Function | Description |
|---|---|
| `lighting_phong` | Phong shading: ambient + diffuse + specular. Takes material properties, light position/intensity, hit point, eye vector, normal as raw floats |
| `render_row_numba` | Full pixel loop combining all the above -- this is where the real speedup lives since the loop itself is compiled |

## How to Test

Each Numba function is tested against the existing Python implementation with the same inputs:

```bash
PYTHONPATH=. uv run python scripts/numba_test.py
```

## Key Lessons

1. Compiling individual functions but calling them from a Python loop gains almost nothing -- the Python loop overhead dominates
2. The entire hot loop must be inside `@njit`
3. Points (w=1) include the translation column (`inv[row, 3]`) in matrix multiply; vectors (w=0) do not
4. Normal computation uses `transpose(inverse) * normal`, not `inverse * normal` -- index swap: `inv[j,i]` instead of `inv[i,j]`
5. All return paths in an `@njit` function must return the same type
