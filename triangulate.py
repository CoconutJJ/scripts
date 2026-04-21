class Triangle:

    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dot(self, v: 'Vector2'):

        return v.x * self.x + v.y * self.y

def triangulate(points: list[tuple[int, int]]):

    def computeEnclosingTriangle():

        minX = float('inf')
        maxX = float('-inf')

        minY = float('inf')
        maxY = float('-inf')
        
        for x,y in points:

            minX, maxX = min(x, minX), max(x, maxX)
            minY, maxY = min(y, minY), max(y, maxY)

        h = maxY - minY
        w = maxX - minX

        k = max(w, h)
        
        a = (minX, maxY)
        b = (minX, minY - k)
        c = (maxX + k, maxY)
        
        return Triangle(a,b,c)
        
        
            
        
        
        #  (minX, maxY) -------------- (maxX, maxY)
        #      |                            |
        #      |                            |
        #  (minX, minY) -------------- (maxX, minY)
        
