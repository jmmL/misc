def main():
    """A simulation-ish of Summer Eights bumps racing"""
    
    import random
    course_length = 1000.0
    bung_line_separation = 20
    number_of_bung_lines = 12
    
    class Boat:
        def __init__(self,name,speed,bung_line):
            self.name = name
            self.speed = speed
            self.bung_line = bung_line
            
    def time_to_complete_course(boat):
        if (random.random() > 0.95):
            boat.speed *= 0.8
        return ((course_length - ((number_of_bung_lines - boat.bung_line)
         * bung_line_separation)) / boat.speed)
       
    univ = Boat("Univ",20.0,3)
    balliol = Boat("Balliol",16.0,1)
    boats = [univ, balliol] 
    
    #print(time_to_complete_course(univ_boat))
    
    
    
    if (time_to_complete_course(univ) < time_to_complete_course(balliol)):
        print(univ.name + " won!")
    else:
        print(balliol.name + " won!")
    
main()
