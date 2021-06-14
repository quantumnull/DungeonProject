import adject
from individual import Individual

import random
from math import sqrt

class Population:
  def __init__(self, noun, size, num, boundary):
    self.noun = noun
    self.individuals = {}
    for i in range(num):
      x = random.uniform(-boundary, boundary)
      y = random.uniform(-boundary, boundary)
      name = adject.ive()
      self.individuals[name] = Individual(name, noun, size, (x, y))
    self.individuals["tutorial"] = Individual("tutorial", noun, size, (0.0, 0.0))
  
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