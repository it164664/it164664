# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 16:06:20 2021

@author: Lalik
"""

import curses

myscreen=curses.initscr()
myscreen.border(0)
myscreen.addstr(12, 25, "Python curses in action!")    
myscreen.refresh()
myscreen.getch()     
curses.endwin()