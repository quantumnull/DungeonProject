try:
  if __name__ == "__main__":
    import act
    import player
    import world
    import graphics
    from graphics import read, write
    import curses  # yes that's seriously what it's called

    graphics.init()
    write("Oh great, another one.")
    has_personality = read("Dost this hero have any personality at all? ")
    player.pc = player.Player("y" == has_personality)

    while True:
      write(f"You are at {player.pc.coords}")
      world.print_visible(player.pc.coords)
      write(f"You have found {len(player.pc.fairies)} fairies")
      words = read("What do? ").split()
      if len(words) == 0:
        continue
      action = words[0].lower()
      if action in act.ions:
        act.ions[action](words[1:])
      else:
        write("Try 'go', dummy")

except:
  curses.endwin()  # or else the terminal is messed up when we crash
  print("You have done a sin.")
  raise