from src.ray_tracer.lights.point import PointLight
from src.ray_tracer.material import Material
from src.ray_tracer.tuples import ColorTuple, CustomTuple


def lighting(
    m: Material, light: PointLight, position: CustomTuple, eye_vec: CustomTuple, normal_vec: CustomTuple
) -> ColorTuple:
    """Calculate the lighting at a point on a surface."""
    effective_color = m.color * light.intensity
    light_vec = (light.position - position).normalize()

    ambient = effective_color * m.ambient

    light_dot_normal = light_vec.dot(normal_vec)
    if light_dot_normal < 0:
        diffuse = ColorTuple(0, 0, 0)
        specular = ColorTuple(0, 0, 0)
    else:
        diffuse = effective_color * m.diffuse * light_dot_normal
        reflect_vec = (-light_vec).reflect(normal_vec)
        reflect_dot_eye = reflect_vec.dot(eye_vec)

        if reflect_dot_eye <= 0:
            specular = ColorTuple(0, 0, 0)
        else:
            factor = pow(reflect_dot_eye, m.shininess)
            specular = light.intensity * m.specular * factor

    return ambient + diffuse + specular
