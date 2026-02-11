from math import sqrt

from src.ray_tracer.intersection import Intersection
from src.ray_tracer.sphere import Sphere
from src.ray_tracer.tuples import CustomTuple
from src.ray_tracer.matrix.transforms import Transform


class Ray:
    """Primitive Ray object for the Ray Tracer."""

    def __init__(self, origin: CustomTuple, direction: CustomTuple) -> None:
        self.origin = origin
        self.direction = direction

    @staticmethod
    def position(ray: "Ray", t: float) -> CustomTuple:
        """Calculates the position of a Ray after time t.

        Args:
            ray: the Ray object to calculate the final position for
            t: the time at which the position is calculated

        Returns:
            A CustomTuple of type Point that represents the final position of the Ray
        """
        return ray.origin + ray.direction * t

    def transform(self, matrix: Transform) -> "Ray":
        """Transforms the Ray using a given matrix.

        Args:
            matrix: the matrix to transform the Ray with

        Returns:
            A new Ray object that represents the transformed Ray
        """
        return Ray(matrix * self.origin , self.direction.transform(matrix))

def intersect(ray: "Ray", sphere: Sphere) -> tuple[Intersection, Intersection] | tuple[()]:
    """Calculate and return the intersection points for a given Ray and Sphere.
    Args:
        ray: Ray object
        sphere: Sphere object

    Returns:
        tuple containing the intersection points
    """
    # first we calculate the discriminant
    sphere_to_ray = ray.origin - sphere.origin
    a = ray.direction.dot(ray.direction)
    b = 2 * ray.direction.dot(sphere_to_ray)
    c = sphere_to_ray.dot(sphere_to_ray) - 1

    discriminant = (b**2) - (4 * a * c)

    # if discriminant negative, no intersection occurs
    if discriminant < 0:
        return ()

    t1 = float((-b - sqrt(discriminant)) / (2 * a))
    t2 = float((-b + sqrt(discriminant)) / (2 * a))

    return (Intersection(t1, sphere), Intersection(t2, sphere))


def hit(intersections: tuple[Intersection, ...]) -> Intersection | None:
    """Determine which intersection should actually be rendered given a list of intersections."""
    lowest = Intersection(float("inf"), Sphere())

    for intersection in intersections:
        if intersection.t < 0:
            continue
        if intersection.t < lowest.t:
            lowest = intersection

    if lowest.t == float("inf"):
        return None

    return lowest


def transform
