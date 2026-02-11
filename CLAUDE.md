# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

**Testing**: `PYTHONPATH=. uv run pytest .`
**Type checking**: `PYTHONPATH=. uv run mypy .`
**Linting**: `ruff check .` (format with `ruff format .`)
**Run scratchpad script**: `PYTHONPATH=. uv run python -m scripts.scratchpad`

## Project Architecture

This is a ray tracer implementation built from scratch in Python. The project is structured in two main parts:

### Core Ray Tracer (`src/ray_tracer/`)
- **Tuples**: `CustomTuple` represents 3D points (w=1) and vectors (w=0), with `ColorTuple` for RGB values
- **Canvas**: 2D pixel array for rendering, with PPM export functionality
- **Matrix**: `RTMatrix` handles 4x4 transformation matrices for 3D operations
- **Ray**: Primitive ray objects with origin and direction for ray casting
- **Sphere**: 3D sphere primitives for intersection testing

### Physics Simulation (`src/cannon/`)
- **Projectile**: Objects with position and velocity
- **Environment**: Contains gravity and wind forces
- **tick**: Physics step function that applies environmental forces

### Key Patterns
- All main classes are imported through `__init__.py` files for clean imports
- Uses static factory methods like `CustomTuple.point()` and `CustomTuple.vector()`
- Canvas uses row-major indexing: `canvas[row, col]` or `canvas[row][col]`
- Ray position calculation: `Ray.position(ray, t)` returns `origin + direction * t`

### Dependencies
- **numpy**: Used for mathematical operations
- **pytest**: Testing framework
- **mypy**: Static type checking (strict mode enabled)
- **ruff**: Linting and formatting (line length 120, Google docstring convention)

The project follows strict typing with mypy and comprehensive linting with ruff. Test files ignore most style rules to focus on functionality testing.