import copy
import math
from typing import TypeVar

import adject

from math import pi as π
from math import atan2

T = TypeVar("T", bound = "Entity")

# the plan is to ultimately have Entity contain subclasses for items,
# characters, and whatever else could be considered an entity
# TODO: decide whether we want the player to be considered an Entity or not
class Entity:
  def __init__(
    self,
    name: str = "Unnamed",
    noun: str = "Unnamed",
    size: int = 1,
    coords: tuple([float, float]) = (0, 0),
    farstring: str = "Nondescript",
  ):
    self.name = name
    self.noun = noun
    self.size = size
    self.coords = coords
    self.farstring = farstring 

  # return distance between entity and a set of coordinates
  def distance(self, coords: tuple([float, float])) -> float:
    return math.sqrt((coords[0] - self.coords[0]) ** 2 + (coords[1] - self.coords[1]) ** 2)

  # get text depending on direction of entity relative to the player
  def get_direction(self, other_coords: tuple([float, float])) -> str:
    (ox, oy) = other_coords
    (sx, sy) = self.coords
    if (sx-ox, sy-oy) == (0.0, 0.0):
      return "right on top of you"
    angle = atan2(sy-oy, sx-ox)
    if -π/8.0 < angle < π/8.0:
      return "due east of you"
    elif π/8.0 < angle < 3.0*π/8.0:
      return "northeast of you"
    elif -π/8.0 > angle > -3.0*π/8.0:
      return "southeast of you"
    elif 3.0*π/8.0 < angle < 5.0*π/8.0:
      return "due north of you"
    elif -3.0*π/8.0 > angle > -5.0*π/8.0:
      return "due south of you"
    elif 5.0*π/8.0 < angle < 7.0*π/8.0:
      return "northwest of you"
    elif -5.0*π/8.0 > angle > -7.0*π/8.0:
      return "southwest of you"
    else:
      return "due west of you"

  # create a deep copy of one of the entities in entity_types.py,
  # give it a name, and place it at the given coordinates
  def spawn(self: T, coords: tuple([float, float])) -> T:
    clone = copy.deepcopy(self)
    clone.name = adject.ive()
    clone.coords = coords
    return clone

  # TODO: make this actually kill stuff, however we want to handle that
  def destroy(self) -> None:
    self.name = 'dead'

# used for individuals, so creatures, really
# TODO: create way to turn into a corpse
class Individual(Entity):
  def __init__(
    self,
    name: str = "Unnamed",
    noun: str = "Unnamed",
    size: int = 1,
    coords: tuple([float, float]) = (0, 0),
    farstring: str = "Nondescript"
  ):
    super().__init__(
      name = name,
      noun = noun,
      size = size,
      coords = coords,
      farstring = farstring,
    )

  # update coords with a new set of coordinates
  def move(self, dest: tuple([float, float])) -> None:
    self.coords = tuple(item1 + item2 for item1, item2 in zip(self.coords, dest))
  
  #zach snuck this untested function in here, and into player
  def get_offset(origin, dest):
    return tuple(item1 + item2 for item1, item2 in zip(origin, dest))

#class Item(Entity):
