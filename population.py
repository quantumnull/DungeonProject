import entity_types
from entity import Entity


import random
from math import sqrt

# generate entities using the entity spawn method
# which creates clones of creatures in entity_types
# I'm not sure how I feel about the population __init__ doing all the heavy lifting,
# might be worth breaking it into a separate def at some point?
class Population:
  def __init__(self, entity, num, boundary):
    self.individuals = {}
    for i in range(num):
      x = random.uniform(-boundary, boundary)
      y = random.uniform(-boundary, boundary)
      new_entity = entity.spawn((x, y))
      self.individuals[new_entity.name] = new_entity
  
  def __getitem__(self, key):
    return self.individuals[key]

  def __contains__(self, key):
    return key in self.individuals
  
  def in_sight(self, other_coords):
    (ox, oy) = other_coords
    visible = []
    for name in self.individuals:
      ind = self.individuals[name]
      (sx, sy) = ind.coords
      dist = sqrt((ox-sx)**2 + (oy-sy)**2)
      if dist <= ind.size:
        visible.append((ind, dist))
    return visible