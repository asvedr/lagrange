class Lagrange:
	_points = []
	def clear(self):
		self._points = []
	def setPoints(self, pts):
		self._points = map(lambda p: p.copy(), pts)
	def l(self,x,i): # lagrange function
		res = 1
		points = self._points
		xI = points[i].x
		for j in range(len(points)):
			if j == i:
				continue
			else:
				xJ = points[j].x
				res = res * (x  - xJ) / (xI - xJ)
		return res
	def calculate(self,x):
		res = 0
		points = self._points
		for i in range(len(points)):
			yI = points[i].y
			res = res + yI * self.l(x,i)
		return res

