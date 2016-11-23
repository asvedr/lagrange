#!/usr/bin/env python
# PYTHON 2.7
# require tkinter

from Field import *
from Tkinter import Tk
from Polynom import *
import math
import sys

root = Tk()

fld = Field(root, 500, 500)
fld.pack()

p = Lagrange() # making polynom
fld.funs = [(math.sin, 'red'), (p.calculate, 'green')] # setting functions to draw

# if you want make it by your hands
def manualSetPoints():
	def rebuild():
		l = fld.points()
		l.sort(cmp = lambda a,b: cmp(a.x,b.x))
		p.setPoints(l)
	fld.onClick = rebuild

# just show demo
def autoSetPoints():
	fld.allowClick = False
	maxX = 3
	minX = -3
	pts = []
	x = minX
	s = step * 10
	while x < maxX:
		pts.append(Point(x,math.sin(x)))
		x = x + s
	x = maxX
	pts.append(Point(x,math.sin(x)))
	p.setPoints(pts)

try:
	if sys.argv[1] == '-show':
		autoSetPoints()
	else:	
		manualSetPoints()
except:
	manualSetPoints()

fld.redraw()

root.mainloop()
