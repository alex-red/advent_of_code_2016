"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

"""
triangles = []
with open('day3.txt', 'r') as f:
  triangles = f.readlines()

def is_valid_triangle(a, b, c):
  return (a + b > c) and (a + c > b) and (b + c > a)

def get_valid_triangles(triangles):
  valid_triangles = 0
  
  for triangle in triangles:
    # sides of the triangle
    a, b, c = (list(map(int, triangle.strip().split())))
    if is_valid_triangle(a, b, c):
      valid_triangles += 1

  return valid_triangles

def get_valid_triangles_columns(triangles):
  valid_triangles = 0

  def clean(triangle):
    return [int(side) for side in triangle.strip().split()]

  a, b, c = 0, 1, 2
  while len(triangles) > c:
    t1, t2, t3 = clean(triangles[a]), clean(triangles[b]), clean(triangles[c])
    for i in range(0, 3):
      if is_valid_triangle(t1[i], t2[i], t3[i]):
        valid_triangles += 1
    a, b, c = a + 3, b + 3, c + 3

  return valid_triangles

print (get_valid_triangles(triangles))
print (get_valid_triangles_columns(triangles))

