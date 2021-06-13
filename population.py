import adject
from individual import Individual
import player

import random

class Population:
  def __init__(self, noun, num, boundary, sight_dist):
    self.noun = noun
    self.sight_dist = sight_dist
    self.individuals = {}
    for i in range(num):
      x = random.uniform(-boundary, boundary)
      y = random.uniform(-boundary, boundary)
      name = adject.ive()
      self.individuals[name] = Individual(name, (x, y))
    self.individuals["tutorial"] = Individual("tutorial", (0.0, 0.0))
  
  def in_sight(self):
    (px, py) = player.pc.coords
    dist = self.sight_dist
    faint_dist = self.sight_dist * 2
    visible = []
    faint = []
    for name in self.individuals:
      ind = self.individuals[name]
      (ix, iy) = ind.coords
      if px-dist <= ix <= px+dist and py-dist <= iy <= py+dist:
        if (px-ix)**2 + (py-iy)**2 <= dist**2:
          visible.append(ind)
      elif px-faint_dist <= ix <= px+faint_dist and py-faint_dist <= iy <= py+faint_dist:
        if (px-ix)**2 + (py-iy)**2 <= faint_dist**2:
          faint.append(ind)
    return (visible, faint)