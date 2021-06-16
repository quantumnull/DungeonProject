import esper
import graphics
import act
import world
import player


#this is a dummy processor created by moving the game loop out of main, eventually we will have like, a movement processor, maybe an AI processor, a graphics processor etc, this is a placeholder for now.
class UpdateProcessor(esper.Processor):
  def process(self):
    with graphics.window as w:
      w.print(f"You are at {player.pc.coords}.")
      world.print_visible(player.pc.coords)
      w.draw_outbox()
      words = w.input().split()
      if len(words) == 0:
        w.print("Try 'go', dummy.")
        return
      action = words[0].lower()
      if action in act.ions:
        act.ions[action](words[1:])
      else:
        w.print("Try 'go', dummy.")