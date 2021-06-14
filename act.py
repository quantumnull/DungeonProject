import player
import world
from individual import Individual

def go(words):
  if len(words) == 0:
    words = input("Go where? ").split()
  
  if len(words) == 1:
    vector = direction_vector(words[0])
    if vector != None:
      player.pc.walk(vector)
      return
  elif len(words) == 3 and words[0] == "to":
    if words[2] in world.pops and words[1] in world.pops[words[2]]:
      player.pc.teleport(world.pops[words[2]][words[1]].coords)
      return

  print("You cannot go", " ".join(words))

def evil(words):
  try:
    print(eval(" ".join(words)))
  except BaseException as e:
    print("You have done a sin.")
    print(e)
    pass

ions = {
  "go": go,
  "n": lambda _: go(["north"]),
  "s": lambda _: go(["south"]),
  "e": lambda _: go(["east"]),
  "w": lambda _: go(["west"]),
  "ne": lambda _: go(["northeast"]),
  "nw": lambda _: go(["northwest"]),
  "se": lambda _: go(["southeast"]),
  "sw": lambda _: go(["southwest"]),
  "whoami": lambda _: player.pc.print_stats(),
  "eval": evil
}

def direction_vector(dir, steps: int = 10) -> None:
  dir = dir.lower()

  steps = steps

  if dir == "north":
    return (0.0, steps)
  if dir == "south":
    return (0.0, -steps)
  if dir == "east":
    return (steps, 0.0)
  if dir == "west":
    return (-steps, 0.0)
  if dir == "northeast":
    return (steps, steps)
  if dir == "northwest":
    return (-steps, steps)
  if dir == "southeast":
    return (steps, -steps)
  if dir == "southwest":
    return (-steps, -steps)
  if dir == "est" or dir == "northk":
    print("The floor is made of meat.")
    return (0, 0)
  
  return None

def move_individual(
  individual: Individual, 
  direction: tuple([float, float]), 
  steps: int = 10
) -> None:
  individual = individual
  loc_x, loc_y = individual.coords
  dir_x, dir_y = direction
  steps = steps

  

  return None