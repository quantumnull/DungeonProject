def setup(screen):
  import player
  import world
  from graphics import window as w

  w.init(screen)
  w.draw_box()
  w.print("Oh great, another one.")
  has_personality = w.input("Dost this hero have any personality at all? ")
  player.pc = player.Player("y" == has_personality)
  w.draw_box(f"{player.pc.name} the {player.pc.epithet}")

  while True:
    world.world.process()

if __name__ == "__main__":
  try:
    import curses
    curses.wrapper(setup)
  except:
    print("You have done a sin.")
    raise