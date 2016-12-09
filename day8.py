"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

Your puzzle answer was 115.

--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

Your puzzle answer was EFEYKFRFIJ.
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