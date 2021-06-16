import adject
from graphics import window as w

pc = None

class Player:
  def __init__(self, unmirthless):
    if unmirthless:
      self.name = w.input("What is your name?")
      self.epithet = w.input("What is your epithet?")
      self.color = w.input("What is your favorite color?")
      self.velocity = w.input("How much airspeed velocity could an unladen swallow swallow if an unladen swallow could swallow speed?")
      self.love = w.input("What is love?")
      self.licks = w.input("How many licks to the center of a footsie pop?")
      self.conan = w.input("Conan, what is best in life?")
    else:
      w.print("How boring!")
      w.print(f"Experience a journey devoid of mirth, oh {adject.ive()} one.")
      self.name = adject.ive().capitalize()
      self.epithet = adject.ive().capitalize()
      self.color = adject.ive()
      self.velocity = adject.ive()
      self.love = adject.ive()
      self.licks = adject.ive()
      self.conan = adject.ive()
      self.print_stats()
    
    self.coords = (0.0, 0.0)
    self.fairies = set()

  def print_stats(self):
    w.print(f"Your name is {self.name}.")
    w.print(f"Your epithet is {self.epithet}.")
    w.print(f"Your favorite color is {self.color}.")
    w.print(f"You believe the airspeed of an unladen swallow to be {self.velocity}.")
    w.print(f"You think that love is {self.love}.")
    w.print(f"You insist that you know what a footsie pop is, and that its center can be reached in a number of licks equal to {self.licks}.")
    w.print(f"You loudly exclaim that {self.conan} is best in life.")
    
  def teleport(self, vector):
    self.coords = vector

  def walk(self, vector):
    new_x = self.coords[0] + vector[0]
    new_y = self.coords[1] + vector[1]
    self.coords = (new_x, new_y)
  #zach snuck this untested function in here, and in entity
  def get_offset(self, origin, dest):
    return (dest[0]-origin[0], dest[1]-origin[1])