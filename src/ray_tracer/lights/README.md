# Phong Reflection Model

The Phong model breaks the final color of a point on a surface into three components:

```
final color = ambient + diffuse + specular
```

## Ambient

```python
effective_color = m.color * light.intensity
ambient = effective_color * m.ambient
```

Base light that is always present, simulating indirect light bouncing around the scene. Every point on the surface gets this regardless of where the light is. Without it, the side facing away from the light would be pure black.

## Diffuse

```python
light_vec = (light.position - position).normalize()  # vector from hit point to light
light_dot_normal = light_vec.dot(normal_vec)
diffuse = effective_color * m.diffuse * light_dot_normal
```

Models direct illumination from the light source. The dot product between `light_vec` and `normal_vec` gives how directly the light hits the surface:

- Dot product = 1: light hits head-on, full diffuse contribution
- Dot product approaching 0: surface is angled away, less contribution
- Dot product < 0: light is behind the surface, diffuse = 0

This is why a sphere looks rounded under light — the edges are angled away and receive less diffuse contribution.

## Specular

```python
reflect_vec = (-light_vec).reflect(normal_vec)  # light ray reflected off the surface
reflect_dot_eye = reflect_vec.dot(eye_vec)       # how much reflected light goes toward camera
factor = pow(reflect_dot_eye, m.shininess)
specular = light.intensity * m.specular * factor
```

Models the shiny highlight seen on glossy objects. It asks: does the reflected light ray point back toward the camera? If yes, you get a bright highlight. `m.shininess` controls how tight the highlight is — higher values produce a smaller, sharper highlight, lower values produce a wider, softer one.

Note that specular uses `light.intensity` directly rather than `effective_color`, which is why specular highlights tend to be the color of the light rather than the surface.

## Summary

| Component | Question it answers |
|-----------|-------------------|
| Ambient   | What color is the surface regardless of light angle? |
| Diffuse   | How directly is the light hitting this point? |
| Specular  | Is the reflection of the light pointing back at the camera? |
