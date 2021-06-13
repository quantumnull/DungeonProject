import player
import world

def go(words):
  if len(words) == 0:
    words = input("Go where? ").split()
  
  if len(words) == 1:
    vector = direction_vector(words[0])
    if vector != None:
      player.pc.walk(vector)
      return
  elif len(words) == 3 and words[0] == "to":
    if words[2] in world.populations \
    and words[1] in world.populations[words[2]].individuals:
      player.pc.teleport(
        world.populations[words[2]].individuals[words[1]].coords
      )
      return

  print("You cannot go", " ".join(words))

def evil(words):
  try:
    print(eval(" ".join(words)))
  except:
    print("You have done a sin.")
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

def direction_vector(dir):
  dir = dir.lower()

  if dir == "north":
    return (0.0, 10.0)
  if dir == "south":
    return (0.0, -10.0)
  if dir == "east":
    return (10.0, 0.0)
  if dir == "west":
    return (-10.0, 0.0)
  if dir == "northeast":
    return (10.0, 10.0)
  if dir == "northwest":
    return (-10.0, 10.0)
  if dir == "southeast":
    return (10.0, -10.0)
  if dir == "southwest":
    return (-10.0, -10.0)
  if dir == "est" or dir == "northk":
    print("The floor is made of meat.")
    return (0, 0)
  
  return None