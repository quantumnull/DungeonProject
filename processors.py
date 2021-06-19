import esper
import graphics
from graphics import window as w
import act
import world
import player
import numpy
import random
import pops2


#this is a dummy processor created by moving the game loop out of main, eventually we will have like, a movement processor, maybe an AI processor, a graphics processor etc, this is a placeholder for now.
class InterfaceProcessor(esper.Processor):
  def process(self):
      w.print(f"You are at {player.pc.coords}.")
      world.print_visible(player.pc.coords)
      w.draw_outbox()
      words = w.input().split()
      if len(words) == 0:
        w.print("Try 'go', dummy.")
        return
      action = words[0].lower()
      if action in act.ions:
        act.ions[action](words[1:])
      else:
        w.print("Try 'go', dummy.")


#this is a fun joke, it also uses numpy because
#ben told me not to; right now jeremy walks somwhat naively towards the player, in future I would like him to follow behind you (out of your vision cone) and quietly laugh from time to time
#by then he will sadly not be in his own processor, though
class PathfindingProcessor(esper.Processor):
  def process(self):
    for ent, (noun,coords) in world.world.get_components(world.Noun,world.Coords):
      if noun.noun == "Jeremy":
        coords.coords = tuple(numpy.add((coords.coords),random.uniform(1,10)*(numpy.subtract(player.pc.coords,coords.coords))/numpy.linalg.norm(numpy.subtract(player.pc.coords,coords.coords))))
        w.print (f"Jeremy is at {coords.coords}")

#class VolitionProcessor(esper.Processor):
#  def process(self):
#    for ent, (needs, desires, intent) in world.world.get_components(world.Volition):

class EnpopulateHandler(esper.Processor):
  def process(self):
    for ent, (enpop, kind, num, spread) in world.world.get_components(world.EnPopulator, world.Kind, world.Num, world.Spread):
      if (kind == pops2.Goblin):
        for i in range(num.num):
          destination = random.uniform(spread.spread, -1 * spread.spread)
          world.world.create_entity(kind.kind(coords=destination),world.Noun("Goblin"), world.FarString("You see a tiny figure in the distance"),world.Coords(destination),world.Size(20))
          w.print(f"in theory we have created {i} invisible goblins")
      else:
        continue