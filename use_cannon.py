from src.ray_tracer import Canvas

# # p1 = CustomTuple.point(0, 1, 0)
# # v1 = CustomTuple.vector(1, 1, 0)

# # gravity = CustomTuple.vector(0, -0.1, 0)
# # wind = CustomTuple.vector(-0.01, 0, 0)

# # projectile = Projectile(p1, v1)
# # environment = Environment(gravity, wind)

# # while projectile.position.y > 0:
# #     projectile = tick(environment, projectile)
# #     print(projectile.position)

# # c1 = ColorTuple(1, 2, 3)
# # c2 = ColorTuple(4, 5, 6)

# # # print(c1)

# # # print(c1 + c2)
# # # print(c1 - c2)
# # c4 = c1 * 3
# # print(c4 == ColorTuple(3, 6, 9))
# # print(c1.hadamard(c2))

cv = Canvas(256, 256, (0.5, 0.3, 0.7))

# cv[0][0] = ColorTuple(1.5, 0, 0)
# cv[1][2] = ColorTuple(0, 0.5, 0)
# cv[2][4] = ColorTuple(-0.5, 0, 1)
cv.save()

# for i in range(cv.height):
#     for j in range(cv.width):
#         print(cv.pixels[i][j])
#         print(c1)
#         print(cv.pixels[i][j] == c1)
