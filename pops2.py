import adject
import world
import esper

class WorldObject:
  def __init__(self, coords, size, noun):
    self.size = size


class Creature(WorldObject):
  pass

class Goblin(Creature):
  def __init__(self, size="20", noun="Goblin", adjective=adject.ive()):
    pass



#  class Size:
#  def __init__(self, size):
#    self.size=size