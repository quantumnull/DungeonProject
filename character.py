#so far this is all we ask about the character

#this is one way
Name = Class = Color = Velocity = Love = Licks = Conan = """"""
#this is the better way?
Name+=str()

def GenerateCharacter():
  global Name; global Class; global Color; global Velocity; global Love; global Licks; global Conan
  Name=enterName(Name)
  Class=enterClass(Class)
  Color=enterColor(Color)
  Velocity=enterVelocity(Velocity)
  Love=enterLove(Love)
  Licks=enterLicks(Licks)
  Conan=enterConan(Conan)
  PrintCharacter()
  return

def GenerateJoylessCharacter():
  global Name; global Class;
  Name=enterName(Name)
  Class=enterClass(Class)
  PrintCharacter()
  return

def enterName(Name):
  Name+=input("What is your name? " )
  return Name  
def enterClass(Class):
  Class+=input("What is your class? ")
  return Class
def enterColor(Color):
  Color+=input("What is your favorite color? ")
  return Color
def enterColon():
  lookForPolyps()
  return
def enterVelocity(Velocity):
  Velocity+=input("How much airspeed velocity could an unladen swallow swallow if an unladen swallow could swallow speed? ")
  return Velocity
def enterLove(Love):
  Love+=input("What is love? ")
  return Love
def enterLicks(Licks):
  Licks+=input("How many licks to the center of a footsie pop? ")
  return Licks
#adam's favourite def name
def enterConan(Conan):
  Conan+=input("Conan, what is best in life? ")
  return Conan
def lookForPolyps():
  #we are merciful
  return False

def PrintCharacter():
  print ("Your name is ", Name, "\nYour class is: ", Class, "\nYour favorite color is: ", Color, "\nYou believe the airspeed of an unladen swallow to be:", Velocity)
  return