# awake.utils
# Utility functions

import curses
from contextlib import contextmanager

@contextmanager
def screen():
   '''Context manager for setting up and tearing down curses screen'''
   stdscr = curses.initscr()
   curses.noecho() # No echo key input
   curses.cbreak() # Input without enter
   curses.curs_set(0) # Hide cursor
   stdscr.keypad(True) # Allow arrow keys
   stdscr.nodelay(True) # Non-blocking input reading
   try:
      yield stdscr
   finally:
      curses.curs_set(1)
      curses.nocbreak()
      curses.echo()
      curses.endwin()

def print_safe(terminal, text):
   '''Print text with newlines safely with regards to cursor position'''
   lines = text.split('\n')
   for line in lines:
      with terminal.location():
         print(line)
      print(terminal.move_down(), end='')

def print_center(terminal, text):
   '''Print text in center of terminal'''
   lines = text.split('\n')
   text_height = len(lines)
   x = int(terminal.width/2)
   y = int(terminal.height/2)
   line_y = int((y-(text_height/2)))
   min_x = x
   min_y = line_y
   for line in lines:
      line_x = int((x-(len(line)/2)))
      with terminal.location(line_x, line_y):
         print(line)
      line_y += 1
      if line_x < min_x:
         min_x = line_x
   return (min_x, min_y)