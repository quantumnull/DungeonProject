import curses
import textwrap
from collections import deque
from math import ceil

class Window():
  def __init__(self, height, width):
    # the initial window that takes up the whole screen
    self.screen = curses.initscr()
    # this makes colors available. it also fucks up all the colors,
    # so we have to fix them after.
    # what a fucking piece of shit
    curses.start_color()
    curses.init_color(curses.COLOR_BLACK, 0, 0, 0)
    # values out of 1000? what the fuck?
    curses.init_color(curses.COLOR_WHITE, 1000, 1000, 1000)
    # for whatever godforsaken reason printing text doesn't print in the expected
    # white foreground/black background, and the uppercase letters print as
    # different colors from the lowercase letters (what the FUCK?), so we have
    # to define a color pair just for text to get sane behavior
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # most of the time the "real" underlying terminal dimensions are
    # determined by whatever the repl.it server chooses to render the window at,
    # which has no connection to the size of the terminal as displayed
    # in any user's web interface.
    # so we arbitrarily choose some smaller terminal window dimensions
    # to display on the web nicely, however, occasionally repl.it
    # randomly decides that the server's "real" terminal dimensions
    # are smaller than the dimensions we picked, which would cause curses
    # to crash. we prevent that crash by overriding our chosen dimensions
    # if they're determined to be larger than the "real" terminal.
    # also, height is weird here because we want it to represent the
    # "logical" height of our window, but in fact we have to initialize
    # the window with a height of +1 or else curses will crash after it
    # writes a full line to the bottom line in the window, causing the cursor
    # to automatically wrap to the next (non-existent) line.
    (max_h, max_w) = self.screen.getmaxyx()
    if max_h < height+1:
      height = max_h-1
    if max_w < width:
      width = max_w

    self.height = height
    self.width = width
    
    # height is dumb, curses is dumb, see prior comment
    self.box = self.screen.subwin(height+1, width, 0, 0)

    # subwindows that we can independently clear and write to,
    # defined as relative children of the box
    self.outbox_h = height - 4
    self.outbox_w = width - 2
    self.inbox_h = 1
    self.inbox_w = width - 4
    self.outbox = self.box.subwin(self.outbox_h, self.outbox_w, 1, 0)
    self.inbox = self.box.subwin(self.inbox_h, self.inbox_w, height - 2, 2)

    self.outbox_history = deque(maxlen=self.outbox_h*10)
  
  def draw_box(self, title=""):
    self.box.clear()

    self.box.addstr(0, 0, "┏" + "━"*(self.width-2) + "┓")
    self.box.addstr(self.height-3, 0, "┣" + "━"*(self.width-2) + "┫")
    self.box.addstr(self.height-2, 0, "❱")
    self.box.addstr(self.height-1, 0, "┗" + "━"*(self.width-2) + "┛")

    if title != "":
      start_pos = (self.width // 2) - (int(ceil(len(title) / 2))) - 2
      self.box.addstr(0, start_pos, "┫ ")
      self.box.addstr(0, start_pos + len(title) + 2, " ┣")
      self.box.addstr(0, start_pos + 2, title, curses.A_BOLD)

    self.box.refresh()

  # note that this function will not actually update the terminal,
  # it only updates the internal output buffer.
  # the main game loop should call `window.draw_outbox()` every tick.
  # this prevents screen flickering caused by spurious refreshes. 
  def print(self, str, gutter="  "):
    if str == "":
      return
    
    for line in textwrap.wrap(str, self.outbox_w-3):
      self.outbox_history.append(f"{gutter}{line}")
  
  def draw_outbox(self):
    self.outbox.clear()

    # only the most recent messages get printed in white.
    # a message is recent if it's been printed since the last command input.
    stale = False
    for i in range(1, self.outbox_h+1):
      if i > len(self.outbox_history):
        break
      line = self.outbox_history[-i]
      style = curses.A_NORMAL
      if stale:
        style |= curses.A_DIM
      # detect command inputs to set stale for subsequent lines
      if line[0] == "❱":
        style |= curses.A_BOLD
        stale = True
      self.outbox.addstr(self.outbox_h-i, 0, self.outbox_history[-i], style)

    self.outbox.refresh()

  def input(self, prompt=None):
    if prompt != None:
      self.print(prompt)
      self.draw_outbox()

    command = self.inbox.getstr().decode('ascii')

    if command != "":
      self.inbox.clear()
      self.inbox.refresh()
      self.print(command, "❱ ")

    self.inbox.move(0, 0)  # make sure cursor is where it belongs
    return command

  # allows us to use context managers (the `with` keyword) on instances
  def __enter__(self):
    return self
  
  # context manager cleanup, ensures that the terminal isn't fucked
  def __exit__(self, exc_type, exc_value, traceback):
    curses.endwin()

window = Window(height=24, width=60)