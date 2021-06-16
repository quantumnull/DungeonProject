try:
  if __name__ == "__main__":
    import graphics
    import act
    import player
    import world

    with graphics.window as w:
      w.draw_box()
      w.print("Oh great, another one.")
      has_personality = w.input("Dost this hero have any personality at all? ")
      player.pc = player.Player("y" == has_personality)
      w.draw_box(f"{player.pc.name} the {player.pc.epithet}")
      '''
      while True:
        w.print(f"You are at {player.pc.coords}.")
        world.print_visible(player.pc.coords)
        w.draw_outbox()
        words = w.input().split()
        if len(words) == 0:
          w.print("Try 'go', dummy.")
          continue
        action = words[0].lower()
        if action in act.ions:
          act.ions[action](words[1:])
        else:
          w.print("Try 'go', dummy.")
      '''

      while True:
        world.world.process()




except:
  print("You have done a sin.")
  raise