from src.ray_tracer.tuples import CustomTuple


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
        return ray.origin + ray.direction * t;            

