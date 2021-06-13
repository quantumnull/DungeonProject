#behold, we import the data
with open("logicgatesinstructions2.txt") as f:
  lines=[]
  for line in f:
    lines.append(line.split())


#we try to sort this terrible input list
#the sorting didn't work so we do it 10 times (or no less than a thousand and fifty times I guess)
for repetition in range(1049):
#champs are thing that will be declared properly, and therefore are not really bozos
  champs=[]
  #we loop through the list of lines by index nerd
  for nerd in range(len(lines)):
    #we loop through lines[nerd] by index jerk
    for jerk in range(len(lines[nerd])-1):
    #the specific jerk and/or nerd we're looking at is now stored as a bozo:
      bozo=lines[nerd][jerk]
      threw=False
      if (bozo != "->") and (bozo != "OR") and (bozo != "NOT") and (bozo != "AND") and (bozo != "RSHIFT") and (bozo != "LSHIFT") and (bozo not in champs):
        try:
          eval(lines[nerd][jerk])
        except NameError:
          lines.append(lines.pop(nerd))
          threw=True
        except SyntaxError:
          lines.append(lines.pop(nerd))
          threw=True
      if threw:
        break
    if not threw: champs.append(lines[nerd][-1])
#using the safe and popular exec and eval functions we
#try to perform the bitwise operations and assignments in our data

for i2 in lines:
  dummy1=i2[-1]
  if "AND" in i2:
    print(i2)
    dummy2=eval(i2[0])&eval(i2[2])
    i2[0]=dummy2
  if "OR" in i2:
    dummy2=eval(i2[0])|eval(i2[2])
    i2[0]=dummy2
  if "LSHIFT" in i2:
    dummy2=eval(i2[0])<<eval(i2[2])
    i2[0]=dummy2
  if "RSHIFT" in i2:
    dummy2=eval(i2[0])>>eval(i2[2])
    i2[0]=dummy2
  if "NOT" in i2:
    dummy2=65536 + (~eval(i2[1]))
    i2[0]=dummy2
  dummy1 = str(i2[-1])+"="+str(i2[0])
  print(dummy1)
  exec(dummy1)



    #if j=="AND"
    #if j=="OR"
    #if j=="LSHIFT"
    #if j=="RSHIFT"

#in the end, we only care about the value of d, though:
print(eval("a"))





#  if l[1]=="->":
#    dummy = str(l[2])+"="+str(l[0])
#    print(dummy)
#    exec(dummy)
#    print(x)