def setup ():
    size(250, 250)
    
def draw():
    # blue 1
    fill(0, 0, random(255))
    rect(0, 0, 25, 25)
    # blue 3
    rect(50, 50, 25, 25)
    
    # green 2
    fill(0, random(255), 0)
    rect(25, 25, 25, 25) 
    # green 5
    rect(100, 100, 25, 25)
    
    # red 4
    fill(random(255), 0, 0)
    rect(75, 75, 25, 25)
    # red 6
    rect(125, 125, 25, 25)
