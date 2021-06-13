import act
import player
import world

try:
  if __name__ == "__main__":
    print("Oh great, another one.")
    player.pc = player.Player(
      "y" == input("Dost this hero have any personality at all? ")
    )

    while True:
      print("You are at", player.pc.coords)
      world.print_visible()
      words = input("What do? ").split()
      if len(words) == 0:
        continue
      action = words[0].lower()
      if action in act.ions:
        act.ions[action](words[1:])
      else:
        print("Try 'go', dummy")

except:
  print("You have done a sin.")
  raise