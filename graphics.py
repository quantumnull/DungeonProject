import curses
import textwrap

window_height = 24
window_width = 60

inport = None
outport = None
output_buffer = []

def init():
  global inport
  global outport
  global output_buffer

  # The `screen` is a window that acts as the master window
  # that takes up the whole screen. Other windows created
  # later will get painted on to the `screen` window.
  screen = curses.initscr()
  
  # we can't change or even query repl.it's terminal dimensions,
  # so this subwindow lets create a terminal of custom size
  window = screen.subwin(window_height, window_width, 0, 0)

  # box drawing
  window.addstr(0, 0, "╔" + "═"*(window_width-2) + "╗")
  for i in range(1, window_height-4):
    window.addstr(i, 0, "║" + " "*(window_width-2) + "║")
  window.addstr(window_height-4, 0, "╟" + "─"*(window_width-2) + "╢")
  window.addstr(window_height-3, 0, "║ >" + " "*(window_width-4) + "║")
  window.addstr(window_height-2, 0, "╚" + "═"*(window_width-2) + "╝")

  # two sub-subwindows that we can independently clear and write to
  # without messing up the box
  outport = window.subwin(window_height-5, window_width-4, 1, 2)
  inport = window.subwin(1, window_width-6, window_height-3, 4)

  window.refresh()  # display the changes to window and its children

def write(str):
  global outport
  global output_buffer
  output_buffer.append(str)
  outport.clear()

  recent_output = output_buffer[-(window_height-6):].copy()
  i = 0
  while True:
    if len(recent_output) < 1 or i > window_height-6:
      break
    line = recent_output.pop()
    line = textwrap.wrap(line, window_width-5)
    line.reverse()
    for part in line:
      outport.addstr(window_height-6-i, 0, part)
      i += 1
      if i > window_height-6:
        break
      
  outport.refresh()

def read(str=""):
  global inport
  inport.addstr(0, 0, str)
  command = inport.getstr().decode('ascii')
  inport.clear()
  inport.refresh()
  write(f"> {str}{command}")
  return command