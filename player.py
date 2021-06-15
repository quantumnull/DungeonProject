import adject

pc = None

class Player:
  def __init__(self, unmirthless):
    if unmirthless:
      self.name = input("What is your name? ")
      self.vocation = input("What is your vocation? ")
      self.color = input("What is your favorite color? ")
      self.velocity = input("How much airspeed velocity could an unladen swallow swallow if an unladen swallow could swallow speed? ")
      self.love = input("What is love? ")
      self.licks = input("How many licks to the center of a footsie pop? ")
      self.conan = input("Conan, what is best in life? ")
    else:
      print("How boring!")
      print("Experience a journey devoid of mirth, oh", adject.ive(), "one.")
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
    print("Your name is", self.name)
    print("Your vocation is", self.vocation)
    print("Your favorite color is", self.color)
    print("You believe the airspeed of an unladen swallow to be", self.velocity)
    print("You think that love is", self.love)
    print("You insist that you know what a footsie pop is, and that its center can be reached in a number of licks equal to", self.licks)
    print("You loudly exclaim that", self.conan, "is best in life")
    
  def teleport(self, vector):
    self.coords = vector

  def walk(self, vector):
    new_x = self.coords[0] + vector[0]
    new_y = self.coords[1] + vector[1]
    self.coords = (new_x, new_y)
  #zach snuck this untested function in here, and in entity
  def get_offset(origin, dest):
    return tuple(item1 + item2 for item1, item2 in zip(origin, dest))