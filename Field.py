from Tkinter import *

class Point:
	x = 0
	y = 0
	def __init__(self,x,y):
		self.x = float(x)
		self.y = float(y)
	def copy(self):
		return Point(self.x, self.y)
	def __str__(self):
		return '<%s:%s>' % (self.x, self.y)
	def __repr__(self):
		return self.__str__()

radius = 5
minX = -5
maxX = 5
minY = -5
maxY = 5
step = 0.1

# class for drawing functions and points
class Field(Canvas):
	def __init__(self,root,w,h):
		Canvas.__init__(self,root,width=w,height=h)
		self.bind('<Button-1>',self.onClick)
		self.width = w
		self.height = h
		self._points = [] # points for clicking
		self.funs    = [] # functions for drawing
		self.beforeRedraw = None # callback 
		self.allowClick = True
		self.onClick = None # callback for getting points
		self.redraw()
	def points(self):
		def adapt(p):
			x = p.x / (self.width / 2.0)
			y = p.y / (self.height / 2.0)
			return Point(x * maxX, y * maxY)
		return map(adapt, self._points)
	def setPoints(self,pts):
		self._points = map(lambda p: p.copy(), pts)
	def clear(self):
		_points = []
		self.redraw()
	def onClick(self,event):
		if not self.allowClick:
			return
		self._points.append(Point(event.x - self.width / 2.0, event.y - self.height / 2.0))
		if self.onClick:
			self.onClick()
		self.redraw()
	def redraw(self):
		if self.beforeRedraw:
			self.beforeRedraw()
		self.delete('all')
		# making field
		w = self.width
		h = self.height
		self.create_line(w/2.0,0,w/2.0,h, width=2, fill='black')
		self.create_line(0,h/2.0,w,h/2.0, width=2, fill='black')
		hw = w / 2.0
		hh = h / 2.0
		# drawing pts
		for p in self._points:
			self.create_oval([p.x - radius + hw, p.y - radius + hh], [p.x + radius + hw, p.y + radius + hh], fill='orange')
		# drawing funs
		for (f,color) in self.funs:
			pts = []
			x = minX
			while x < maxX:
				y = f(x)
				pts.append(Point(x,y))
				x = x + step
			prevPoint = None
			for p in pts:
				x = (p.x - minX) / (maxX - minX) * w
				y = (p.y - minY) / (maxY - minY) * h
				pt = Point(x, y)
				if not (prevPoint is None):
					self.create_line(prevPoint.x, prevPoint.y, pt.x, pt.y, fill=color)
				prevPoint = pt
