import adject
from graphics import read, write

pc = None

class Player:
  def __init__(self, unmirthless):
    if unmirthless:
      self.name = read("What is your name? ")
      self.vocation = read("What is your vocation? ")
      self.color = read("What is your favorite color? ")
      self.velocity = read("How much airspeed velocity could an unladen swallow swallow if an unladen swallow could swallow speed? ")
      self.love = read("What is love? ")
      self.licks = read("How many licks to the center of a footsie pop? ")
      self.conan = read("Conan, what is best in life? ")
    else:
      write("How boring!")
      write(f"Experience a journey devoid of mirth, oh {adject.ive()} one.")
      self.name = adject.ive().capitalize()
      self.vocation = adject.ive()
      self.color = adject.ive()
      self.velocity = adject.ive()
      self.love = adject.ive()
      self.licks = adject.ive()
      self.conan = adject.ive()
      self.print_stats()
    
    self.coords = (0.0, 0.0)
    self.fairies = set()

  def print_stats(self):
    write(f"Your name is {self.name}")
    write(f"Your vocation is {self.vocation}")
    write(f"Your favorite color is {self.color}")
    write(f"You believe the airspeed of an unladen swallow to be {self.velocity}")
    write(f"You think that love is {self.love}")
    write(f"You insist that you know what a footsie pop is, and that its center can be reached in a number of licks equal to {self.licks}")
    write(f"You loudly exclaim that {self.conan} is best in life")
    
  def teleport(self, vector):
    self.coords = vector

  def walk(self, vector):
    new_x = self.coords[0] + vector[0]
    new_y = self.coords[1] + vector[1]
    self.coords = (new_x, new_y)
  #zach snuck this untested function in here, and in entity
  def get_offset(origin, dest):
    return tuple(item1 + item2 for item1, item2 in zip(origin, dest))