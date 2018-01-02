#!/usr/bin/env python3

import curses
import blessings
from . import api

def main():
   print(api.today())

if __name__ == '__main__':
   main()