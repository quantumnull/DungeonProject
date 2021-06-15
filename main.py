try:
  if __name__ == "__main__":
    import act
    import player
    import world
    import locations
    print("Oh great, another one.")
    has_personality = input("Dost this hero have any personality at all? ")
    player.pc = player.Player("y" == has_personality)

    while True:
      print("You are at", player.pc.coords)
      world.print_visible(player.pc.coords)
      print("You have found", len(player.pc.fairies), "fairies")
      words = input("> What do? ").split()
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