#!/usr/bin/env python3

from blessings import Terminal
import curses
import time

from . import utils, api
from .constants import NAME, SLOGAN, VERSION, SUN

def main():
   term = Terminal()
   with utils.screen() as screen:
      # Splash screen
      splash_text = '\n'.join([
         NAME.upper(),
         '',
         SLOGAN,
         '',
         '',
         'Version {}'.format(VERSION)
      ])
      x, y = utils.print_center(term, splash_text)
      with term.location(x-6, y-6):
         utils.print_safe(term, SUN)
      time.sleep(20)


if __name__ == '__main__':
   main()