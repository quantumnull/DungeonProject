from population import Population

populations = {
  "fairy": Population("fairy", 100, 1000, 20.0),
  "goblin": Population("goblin", 100, 1000, 20.0),
}

def print_visible():
  for _, pop in populations.items():
    (visible, faint) = pop.in_sight()
    for ind in visible:
      print("You see a", ind.name, pop.noun, ind.get_direction())
    for ind in faint:
      print("You faintly see something", ind.get_direction())