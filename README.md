# ray-tracer

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mypy](https://img.shields.io/badge/type--checked-mypy-blue.svg)](https://mypy-lang.org/)
[![Tests](https://img.shields.io/badge/tests-138%20passed-brightgreen.svg)]()
[![DeepSource](https://app.deepsource.com/gh/taihim/ray-tracer.svg/?label=code+coverage&show_trend=true&token=qhNUwL2P7FqyHO602IYkmmKW)](https://app.deepsource.com/gh/taihim/ray-tracer/)

A ray tracer built from scratch in Python, following test-driven development.

## Features

- **Tuples & Points** - Custom 3D tuple implementation supporting points (w=1) and vectors (w=0) with full arithmetic operations (add, subtract, negate, dot product, cross product, normalization)
- **Colors** - RGB color representation with Hadamard product for color blending
- **Canvas** - 2D pixel array for rendering with PPM image export
- **Matrices** - 4x4 transformation matrices with multiplication, transposition, determinant, and inversion
- **Transforms** - Translation, scaling, rotation (x/y/z), shearing, and chained transformations
- **Rays** - Ray casting with origin/direction, position calculation, and ray transformation
- **Spheres** - Unit sphere primitives with configurable transforms, ray-sphere intersection testing, and surface normals
- **Materials** - Phong reflection model properties (color, ambient, diffuse, specular, shininess)
- **Lights** - Point light sources with position and intensity
- **Parallel Rendering** - Multiprocessing support for faster image generation

## Project Structure

```
src/
  ray_tracer/
    tuples/         # CustomTuple (points & vectors) and ColorTuple
    canvas/         # Canvas and PPM export
    matrix/         # RTMatrix and Transform classes
    ray/            # Ray and intersection functions
    sphere/         # Sphere primitives and surface normals
    intersection/   # Intersection records
    material/       # Material properties (Phong model)
    lights/         # Point light sources
  cannon/           # Physics simulation (projectile + environment)
scripts/
  draw_sphere.py    # Render a sphere with transforms
  clock.py          # Draw clock face points using rotation transforms
  use_cannon.py     # Projectile simulation
tests/              # Comprehensive test suite (138 tests, 100% coverage)
```

## Setup

Requires Python 3.12.

```bash
# Install dependencies
uv sync

# Run tests
pytest .

# Type checking
mypy .

# Lint
ruff check .

# Render the sphere
python -m scripts.draw_sphere
```

Output images are saved to `images/` in PPM format.
