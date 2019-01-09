import pyglet
from hilbert import HilbertCurve

class Window(pyglet.window.Window):
    
    
    def __init__(self):
        super(Window,self).__init__()
        self.set_size(1000,1000)
        self.curve = HilbertCurve((100,100,600,600),0)
        self.cycle = 1
        pyglet.clock.schedule_interval(self.update,1.0/.5)
        
      
    
    def on_draw(self):
        self.clear()
        self.curve.draw()
    
    #i had to recreate the curve and instantly
    # recursivly break it down everytime 
    #because for some reason it wouldnt draw the curve 
    #correctly if i updated it every so often
    #i know recreating it takes longer but... it wouldn't
    #work other wise. Take what you can get i guess.
    def update(self,dt):       
        self.curve = HilbertCurve((100,100,600,600),0)
        for x in range(self.cycle):
            self.curve.deeper()
        self.cycle += 1
        
        


if __name__ == '__main__':
    window = Window()
    pyglet.app.run() 