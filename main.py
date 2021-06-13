#this is where we make a character and world
import adject
import character
import world
import random

#self-explanatory
def meatfloor():
  print("The floor is made of meat")
  return True

def indiscretion():
    print("You have done a sin")
    return True

def issecretion(str):
  return str in ['pus', 'ichor', 'saliva', 'earwax']

def misdirection(str):
  if str == 'north':
    return 'west'
  if str == 'south':
    return 'east'
  if str == 'east':
    return 'north'
  if str == 'west':
    return 'south'

def isildurerection():
  return 'dat ring tho'

def isdirection(str):
  str = str.lower()
  if str=="north" or str=="east" or str=="west" or str=="south": return True
  elif str=="northk" or str=="est": meatfloor()
  return False

def GetDirection(str):
  str = str.lower()
  if str=="north": return (0.0, 10.0)
  if str=="south": return (0.0, -10.0)
  if str=="east": return (10.0,0.0)
  if str=="west": return (-10.0,0)
  indiscretion()
  meatfloor()
  return (0.0,0.0)

def update(text):
  global LocationCoord
  # first things first: forget all goblins
  VisibleGoblins.clear()
  words = text.split()
  if len(words)==0: words.append("Empty")
  elif words[0]=="timelordify":
    character.GenerateCharacter()
  elif words[0]=="whoami":
    character.PrintCharacter()
  elif words[0]=="multiclassme":
    character.Class = character.enterClass(character.Class)
  elif words[0]=="go":
    if len(words)==1:
      print("Go what direction?")
    elif isdirection(words[1]):
      LocationCoord=tuple(map(lambda i, j: i + j,LocationCoord, GetDirection(words[1])))
    else:
      print("try going a direction")
  else:
    print("try go")
  world.Vision(LocationCoord)
  print("You are at", LocationCoord)
  if len(world.ProximityList(LocationCoord, world.treecoörds, 200))>0:
    for tree in world.ProximityList(LocationCoord,world.treecoörds, 200):
      FoundTrees.add(tree)
    print("You have found " + str(len(FoundTrees)) + " trees.")
  if len(world.ProximityList(LocationCoord, world.goblincoörds, 20))>0:
    for goblin in world.ProximityList(LocationCoord,world.goblincoörds, 20):
      VisibleGoblins.add(goblin)
    print("You see " + str(len(VisibleGoblins)) + " " + adject.ive() + " goblins.")

if __name__ == "__main__":
  #make a forest around 0,0


  start = input("Oh hero, dost thou desire a joyless experience? [Y/N] ")
  if start == "Y": character.GenerateJoylessCharacter()
  elif start == "N": character.GenerateCharacter()
  else: 
    indiscretion()
    print("Invalid choice! Experience a journey devoid of mirth, oh " + adject.ive() + " one")
    character.GenerateJoylessCharacter()

  LocationCoord=(0.0,0.0)

  print(len(world.ProximityList(LocationCoord,world.testcoords,10.0)),5)

  FoundTrees=set()
  VisibleGoblins=set()

  while True:
    update(input("What do? "))