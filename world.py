import random
import adject

class Entity:
  def __init__(self, noun, num, bounds, sight_distance):
    self.noun = noun
    self.sight_distance = sight_distance
    self.members = {}
    for i in range(num):
      x = random.uniform(*bounds)
      y = random.uniform(*bounds)
      name = adject.ive()
      self.members[name] = (x,y)
  
  def in_sight(coords):
    visible = []

entities = {
  "trees": Entity("tree", 200, (-1000, -1000), 200.0),
  "goblins" Entity("goblin", 100, (-30, -30), 20.0),
}
#world.populate(world.treecoörds, 200, -1000, 1000)
#world.populate(world.goblincoörds, 100, -30, 30)



#treecoörds={}
#goblincoörds={}
testcoords=[(0.0,0.0),(10.0,10.0),(20.0,20.0),(-10.0,-10.0),(-20.0,-20.0),(10.0,0.0),(0.0,10.0),(-10.0,0.0),(0.0,-10.0)]

#def populate(objecttype, number, x, y):
#  for i in range (number):
#    X = random.uniform(x,y)
#    Y = random.uniform(x,y)
#    adj = adject.ive()
#    objecttype[adj] = (X,Y)
#  return True

def ProximityList(origin, target, span):
  found=[]
  for item in target: 
    if origin[0]-span <= item[0] <= origin[0]+span and origin[1]-span <= item[1] <= origin[1]+span:
      if (((origin[0]-item[0])**2+(origin[1]-item[1])**2))<=span**2:
        found.append(item)
  return found

#we're gonna want to clean this shit up with classes or something eventually
VisibleLists=["treecoörds","goblincoörds"]
SightDict={"treecoörds": 200.0, "goblincoörds": 20.0}
DescDict={"treecoörds": "tree", "goblincoörds": "goblin"}
HasAdj={"treecoörds": False, "goblincoörds": True}


def Vision(LocationCoord):
  VisibleLists=["treecoörds","goblincoörds"]
  for objectlist in VisibleLists:
      found=ProximityList(LocationCoord,eval(objectlist),SightDict[objectlist])
      if len(found)>1:
        visadj=""
        print("You can see", len(found), visadj, DescDict[objectlist]+"s")
        print("They are", GetDirection(LocationCoord,found))
      elif len(found)==1:
        print("You can see", len(found), DescDict[objectlist] +"s")
        print("It is", GetDirection(LocationCoord,found))


#this is a bad approach, we should probably try to average and/or group, "they are mostly to the southwest and northeast of you etc"

def GetDirection(origin,target):
  output=""
  for site in target:
    site=(site[0]-origin[0],site[1]-origin[1])
    if site==0:
      if len(output)==0: output+= "right on top of you"
      else: output = "on top, and " + output
    if site[0]>0:
      if site[1]==0:
        if len(output)==0: output+= "due east of you"
        else: output = "due east, and " + output
      elif site[1]>0:
        if len(output)==0: output+= "northeast of you"
        else: output = "northeast, and " + output
      elif site[1]<0:
        if len(output)==0: output+= "southeast of you"
        else: output = "southeast, and " + output
    elif site[0]<0:
      if site[1]==0:
        if len(output)==0: output+= "due west of you"
        else: output = "due west, and " + output
      if site[1]>0:
        if len(output)==0: output+= "northwest of you"
        else: output = "northwest, and " + output
      elif site[1]<0:
        if len(output)==0: output+= "southwest of you"
        else: output = "southwest, and " + output
    else:
      if site[1]>0:
        if len(output)==0: output+= "due north of you"
        else: output = "due north, and " + output
      if site[1]<0:
        if len(output)==0: output+= "due south of you"
        else: output = "due south, and " + output
  
  return(output)
  