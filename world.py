from population import Population
import player

pops = {
  "fairy": Population("fairy", 20.0, 200, 1000),
  "goblin": Population("goblin", 40.0, 100, 1000),
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
      print("You see a", ind.name, ind.noun, ind.get_direction(from_coords))
    else:
      print("You faintly see something", ind.get_direction(from_coords))