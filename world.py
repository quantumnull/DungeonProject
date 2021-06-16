from population import Population
import player
import language
import entity_types
from graphics import window as w
import processors

#starting to add framework to be able to use esper ECS
import esper

world=esper.World()
update_processor = processors.UpdateProcessor()
world.add_processor(update_processor)


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
  