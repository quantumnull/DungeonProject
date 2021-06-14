import player
import math

from math import pi as π
from math import atan2

class Individual:
  def __init__(self, name, noun, size, coords):
    self.name = name
    self.noun = noun
    self.size = size
    self.coords = coords

  def get_direction(self, other_coords):
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

# none of the below is used yet
# the plan is to ultimately have Entity contain subclasses for items,
# characters, and whatever else could be considered an entity
class Entity:
  def __init__(
    self,
    coords: tuple([float, float]),
    name: str = "Unnamed",
    noun: str = "Unnamed",
  ):
    self.coords = coords
    self.name = name

  # update coords with a new set of coordinates
  def move(self, dest: tuple([float, float])) -> None:
    self.coords = tuple(item1 + item2 for item1, item2 in zip(self.coords, dest))

  # return distance between entity and a set of coordinates
  def distance(self, coords) -> float:
    return math.sqrt((coords[0] - self.coords[0]) ** 2 + (coords[1] - self.coords[1]) ** 2)

  # TODO: need to have some sort of class to hold the game world as a whole
  # before this can be added
  def spawn(self):
    return None

# will ultimately replace both Individual and Player
class Test_Ind(Entity):
  def __init__(
    self,
    coords: tuple([float, float]),
    name: str = "Unnamed",
    noun: str = "Unnamed",
  ):
    super().__init__(
      coords = coords,
      name = name,
      noun = noun,
    )
