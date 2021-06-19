import player
import world
from graphics import window as w
from entity import Individual
import curses
import math
import random

def go(words):
  if len(words) == 0:
    words = w.input("Go where? ").split()
  
  if len(words) == 1:
    vector = direction_vector(words[0])
    if vector != None:
      player.pc.walk(vector)
      return
  elif len(words) == 3 and words[0] == "to":
    if words[2] in world.pops and words[1] in world.pops[words[2]]:
      vector=player.pc.get_offset(player.pc.coords,world.pops[words[2]][words[1]].coords)
      player.pc.walk(vector)
      return
#      player.pc.teleport(world.pops[words[2]][words[1]].coords)
  elif len(words) ==3 and words[0].isdigit() and words[1][:4]=="step":
    vector = direction_vector(words[2],int(words[0]))
    if vector != None:
      w.print(f"You take {words[0]} steps {words[2]}")
      player.pc.walk(vector)
      return


  w.print(f"You cannot go {' '.join(words)}")

def evil(words):
  try:
    w.print(str(eval(" ".join(words))))
  except BaseException as e:
    w.print("You have done a sin.")
    w.print(str(e))
    
def exaq(words):
  try:
    exec(" ".join(words))
  except BaseException as e:
    w.print("You have done a sin.")
    w.print(str(e))
    

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
  "eval": evil,
  "exec": exaq,
}

def direction_vector(dir, steps: int = 10) -> None:
  dir = dir.lower()

  steps = steps + random.uniform(-0.015,0.015)

  if dir == "north":
    return (0.0, steps)
  if dir == "south":
    return (0.0, -steps)
  if dir == "east":
    return (steps, 0.0)
  if dir == "west":
    return (-steps, 0.0)
  if dir == "northeast":
    return (steps / math.sqrt(2), steps / math.sqrt(2))
  if dir == "northwest":
    return (-steps / math.sqrt(2), steps / math.sqrt(2))
  if dir == "southeast":
    return (steps / math.sqrt(2), -steps / math.sqrt(2))
  if dir == "southwest":
    return (-steps / math.sqrt(2), -steps / math.sqrt(2))
  if dir == "est" or dir == "northk":
    w.print("The floor is made of meat.")
    return (0, 0)
  
  return None

# will ultimately
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