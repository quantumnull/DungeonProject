import player

from math import pi as π
from math import atan2

class Individual:
  def __init__(self, name, coords):
    self.name = name
    self.coords = coords

  def get_direction(self):
    (px, py) = player.pc.coords
    (ix, iy) = self.coords
    if (ix-px, iy-py) == (0.0, 0.0):
      return "right on top of you"
    angle = atan2(iy-py, ix-px)
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