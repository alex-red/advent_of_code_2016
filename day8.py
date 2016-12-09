"""
"""

inputs = []
with open('day8.txt', 'r') as f:
  inputs = f.readlines()

rect = {}
WIDTH = 50
HEIGHT = 6

def fill_rect(x, y):
  for _x in range(int(x)):
    for _y in range(int(y)):
      rect[(_x,_y)] = 1

def shift_rect(direction, start, value):
  # Shift direction: From {start} by {value}
  if direction == 'y':
    # Shift row
    # All values to be shifted
    moved = [xy[0] for xy, val in rect.items() if xy[1] == start and val == 1]
    # Clear the values (set to 0)
    [rect.__setitem__((x, start), 0) for x in moved]
    for x in moved:
      offset = (x + value) if (x + value) < WIDTH else ((x + value) % WIDTH)
      rect[(offset, start)] = 1
  else:
    # Shift column
    # All values to be shifted
    moved = [xy[1] for xy, val in rect.items() if xy[0] == start and val == 1]
    # Clear the values (set to 0)
    [rect.__setitem__((start, y), 0) for y in moved]
    for y in moved:
      offset = (y + value) if (y + value) < HEIGHT else ((y + value) % HEIGHT)
      rect[(start, offset)] = 1

def process_inputs(inputs):
  for line in inputs:
    line = line.strip().split(' ')
    if len(line) == 2:
      x, y = line[1].split('x')
      fill_rect(x, y)
    else:
      start, value = line[2], line[4]
      direction, start = start.split('=')
      shift_rect(direction, int(start), int(value))

def get_lit_pixels():
  return len([value for value in rect.values() if value == 1])

def show_lit_pixels():
  off = u'\U0001F533'
  on = u'\U0001F532'
  for y in range(HEIGHT):
    for x in range(WIDTH):
        value = rect.get((x,y), 0)
        print (on if value else off, end=" ")
    print("")

# Process our inputs
process_inputs(inputs)
# Part 1: Number of lit pixels
print (get_lit_pixels())
# Part 2: Figure out what it says
show_lit_pixels()