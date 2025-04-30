from uuid import uuid4

# for now we assume all spheres are centered at the origin and are unit sphere (radius of 1)
class Sphere:
    "A sphere object."

    def __init__(self):
        self.id = uuid4()