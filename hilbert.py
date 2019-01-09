import pyglet

#I could make these universal by sending in the length of the curve
# and sending in the type of curve so it can check, If i want to
# do other fractals i should consider this

#finds the first point for a curve
def first(point):
        if isinstance(point,HilbertCurve) or len(point) == 4:
            return first(point.points[0])
        else:
            return point 

#finds the last point for a curve
def last(point):
    if isinstance(point,HilbertCurve) or len(point) == 4:
            return last(point.points[3])
    else:
            return point 

#draws a line between two points
def draw_line(points):
        sep_points = (points[0][0],points[0][1],
                      points[1][0],points[1][1])
        #print(sep_points)
        pyglet.graphics.draw(2,pyglet.gl.GL_LINES,
                                        ('v2i',(sep_points)))

class HilbertCurve:
    def __init__(self,dim,kind):
        
        self.face = kind
        #4 kinds of curves defined by where hole faces
        #bottom:0
        #left:1
        #up:2
        #right:3
        #i should change these to enums but
        #its fine

        #the dimentions from the 
        #bottom left conner to the top right connor 
        self.b_x = dim[0]
        self.b_y = dim[1]
        self.t_x = dim[2]
        self.t_y = dim[3]

        #the center point of the given square for reference
        self.center_x = int((self.b_x + self.t_x) / 2)
        self.center_y = int((self.b_y + self.t_y) / 2)

        #the set of points in the current curve
        self.points = ( ( int((self.center_x + self.b_x) / 2),
                          int((self.center_y + self.b_y) / 2) ),
                        ( int((self.center_x + self.b_x) / 2),
                          int((self.center_y + self.t_y) / 2) ),
                        ( int((self.center_x + self.t_x) / 2),
                          int((self.center_y + self.t_y) / 2) ),
                        ( int((self.center_x + self.t_x) / 2),
                          int((self.center_y + self.b_y) / 2) )   
                    )

    #the recusrsive call of the "fractal" structure
    def deeper(self):
       
        #cheching if current curve is just made of smaller curves
        if isinstance(self.points[0],HilbertCurve):
            for point in self.points:
                point.deeper()
        else:        

            #determining the next curves make up of smaller curves
            if self.face == 0:
                nextDown = (1,0,0,3)
            elif self.face == 1:
                nextDown = (0,2,1,1)
            elif self.face == 2:
                nextDown = (2,1,3,2)
            if self.face == 3:
                nextDown = (3,3,2,0)

            #recreating this curve with smaller curves
            p1 = HilbertCurve((self.b_x,      self.b_y,
                               self.center_x, self.center_y), nextDown[0])
            p4 = HilbertCurve((self.center_x, self.b_y,
                               self.t_x,      self.center_y), nextDown[3])
            p2 = HilbertCurve((self.b_x,      self.center_y,
                               self.center_x, self.t_y ),     nextDown[1])
            p3 = HilbertCurve((self.center_x, self.center_y,
                               self.t_x,      self.t_y),      nextDown[2])
            self.points = ((p1,p2,p3,p4))


    #determines the order of the points for the given curve     
    def find_order(self):
        if self.face == 0:
            order = (0,1,2,3)           
        elif self.face == 1:
            order = (0,3,2,1)         
        elif self.face == 2:
            order = (2,3,0,1)         
        if self.face == 3:
            order = (2,1,0,3)

        self.points = (self.points[order[0]],
                       self.points[order[1]],
                       self.points[order[2]],
                       self.points[order[3]])
       
    
    def draw(self):
        
        #checking if current curve is made of smaller curves
        if  isinstance(self.points[0],HilbertCurve):
            for p in self.points:
                    p.draw()
           
        self.find_order()
        
        draw_line(( last(self.points[0]), first(self.points[1])))   
        draw_line(( last(self.points[1]), first(self.points[2])))  
        draw_line(( last(self.points[2]), first(self.points[3])))  

  



