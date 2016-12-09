"""
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?

--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

Your puzzle answer was 182.

"""



directions = "R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5"


def get_direction(direction, steps, facing):
  if direction == 'R':
    # turn right
    facing += 1
  else:
    # turn left
    facing -= 1

  # make sure facing cardinal directions loops back
  # Cardinal directions = ['N', 'R', 'D', 'L']
  if facing > 3: facing = 0
  if facing < 0: facing = 3

  x, y = (0, 0)

  if facing == 0:
    x, y = 0, steps
  elif facing == 1:
    x, y = steps, 0
  elif facing == 2:
    x, y = 0, -steps
  else:
    x, y = -steps, 0

  return (x, y, facing)

def blocks_away(directions):
  start = (0, 0)
  facing = 0

  for coord in directions.split(','):
    coord = coord.strip()
    direction = coord[:1]
    steps = coord[1:]
    x, y, facing = get_direction(direction, int(steps), facing)
    start = (start[0] + x, start[1] + y)

  return abs(start[0]) + abs(start[1])

def blocks_away_first(directions):
  start = (0, 0)
  facing = 0
  routes = set()
  for coord in directions.split(','):
    coord = coord.strip()
    direction = coord[:1]
    steps = coord[1:]
    x, y, facing = get_direction(direction, int(steps), facing)

    # Generate path walked from prev position to new position
    x_step = 1 if x >= 0 else -1
    y_step = 1 if y >= 0 else -1
    if x != 0:
      path = [(x_, start[1]) for x_ in range(start[0], start[0] + x, x_step)]
    else:
      path = [(start[0], y_) for y_ in range(start[1], start[1] + y, y_step)]
    
    # Add path to our routes set, if encountered, then we have our twice visited location
    for p in path:
      if p in routes:
        return abs(p[0]) + abs(p[1])
      else:
        routes.add(p)

    start = (start[0] + x, start[1] + y)

# Part 1 Answer
print (blocks_away(directions))
# Part 2 Answer
print (blocks_away_first(directions))
