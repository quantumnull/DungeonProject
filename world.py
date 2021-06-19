from population import Population
import player
import language
import entity_types
from graphics import window as w
import processors
import pops2

#starting to add framework to be able to use esper ECS
import esper

world=esper.World()
interface_processor = processors.InterfaceProcessor()
pathfinding_processor = processors.PathfindingProcessor()
world.add_processor(interface_processor)
world.add_processor(pathfinding_processor)
world.add_processor(processors.EnpopulateHandler())


# run through population __init__ method and generate entities
# arguments = (entity type, number to generate, max distance from origin)
pops = {
  "fairy": Population(entity_types.fairy, 200, 1000),
  "goblin": Population(entity_types.goblin, 200, 1000),
  "fire": Population(entity_types.fire, 10, 1000),
  "elephant": Population(entity_types.elephant, 100, 1000),
}



def print_visible(from_coords):
  visible = []
  for _, pop in pops.items():
    visible += pop.in_sight(from_coords)
  visible.sort(key=lambda i: i[1])  # sort all by distance
  for ind, dist in visible:
    if ind.noun == "fairy":
      player.pc.fairies.add(ind.name)

    if dist < ind.size / 2:
      w.print(f"You see {language.article(ind.name)} {ind.name} {ind.noun} {ind.get_direction(from_coords)}.")
    else:
      w.print(f"{ind.farstring} {ind.get_direction(from_coords)}.")

#class World():


class Coords:
  def __init__(self, coords=(0.0, 0.0)):
    self.coords=coords

class Size:
  def __init__(self, size):
    self.size=size

class FarString:
  def __init__(self,string):
    self.farstring=string

class Noun:
  def __init__(self,string):
    self.noun=string

class EnPopulator:
  def __init__(self):
    pass

class Kind:
  def __init__(self, kind):
    self.kind = kind

class Num:
  def __init__(self, num):
    self.num = num

class Spread:
  def __init__(self, spread):
    self.spread = spread

world.create_entity(EnPopulator(), Kind(pops2.Goblin()), Num(10000), Spread(400))

jeremy = world.create_entity(Coords((8.0,8.0)),FarString("Jeremy is far away"), Noun("Jeremy"))
#world.add_component(jeremy, Coord(coords=(1.1, 1.1)))
#world.add_component(jeremy, FarString(string="Jeremy is far away"))
#world.add_component(jeremy, Noun("Jeremy"))