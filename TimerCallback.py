import vtk

class TimerCallback():
    def __init__(self):
        self.timer_count = 0
        self.actor=0
        self.function=0
        self.args=0
 
    def simple_execute(self,obj,event):
        print self.timer_count
           
        self.actor.(self.function(self.args));
        iren = obj
        iren.GetRenderWindow().Render()
        self.timer_count += 1
       
    def fully_execute(self,obj,event):
    
    
        iren = obj
        iren.GetRenderWindow().Render()
        self.timer_count += 1
 
 
