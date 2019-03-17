points = []

def setup():
    size(720, 720)
    background(255)
    stroke(0)
    
def draw():

    line(width/2,0,width/2,height)
    line(0,height/2,width,height/2)
    drawline()
    
def mousePressed():
    a = width/2
    b = height/2

    if(mousePressed):
        points.append([mouseX-a, -(mouseY-b)])
        print(points)
        
def drawline():

    a = width/2
    b = height/2
    if(len(points) != 0):
        for i in range(len(points)-1):
            line(points[i][0]+a,-points[i][1]+b, points[i+1][0]+a,-points[i+1][1]+b)
        
        j = len(points)-1
        line(points[j][0]+a,-points[j][1]+b, points[0][0]+a,-points[0][1]+b)
        
    
        
def keyPressed():
    if(keyCode == 83 or keyCode == 115): # scale if s is pressed
        scaleimg()
    if(keyCode == 82 or keyCode == 114): # rotate if r is pressed
        rotateimg()
    if(keyCode == 84 or keyCode == 116): # translate if t is pressed
        translateimg()
    if(keyCode == 88 or keyCode == 120): # reflect along X if x is pressed
        reflectAboutX()
    if(keyCode == 89 or keyCode == 121): # reflect along Y if y is pressed
        reflectAboutY()
    if(keyCode == 79 or keyCode == 111): # reflect along origin if o is pressed
        reflectAboutO()
    if(keyCode == 61):
        reflectAboutYequalX() # reflect along Y = X if = is pressed
    if(keyCode == 45):
        reflectAboutYequalmX() # reflect along Y = -X if - is pressed
            
        
        
def scaleimg():
    sx = 2 # assuming scaling factor to be 2
    sy = 2
        
    for i in range(len(points)):
        points[i][0] = points[i][0] * sx
        points[i][1] = points[i][1] * sy
        
def rotateimg():
    angle = 90
    #assuming anti-clockwise rotation
    for i in range(len(points)):
        points[i][0] = points[i][0]*cos(angle) + points[i][1]*sin(angle)
        points[i][1] = -points[i][0]*sin(angle) + points[i][1]*sin(angle)
        
def translateimg():
    tx, ty = 50, 50 #assuming we move 50 right and 50 up
    
    for i in range(len(points)):
        points[i][0] = points[i][0] + tx
        points[i][1] = points[i][1] + ty
        
def reflectAboutX():
    for i in range(len(points)):
        points[i][1] = -points[i][1]

def reflectAboutY():
    for i in range(len(points)):
        points[i][0] = -points[i][0]

def reflectAboutO():
    for i in range(len(points)):
        points[i][0] = -points[i][0]
        points[i][1] = -points[i][1]

        
def reflectAboutYequalX():
    for i in range(len(points)):
        temp = points[i][0]
        points[i][0] = points[i][1]        
        points[i][1] = temp
        
def reflectAboutYequalmX():
    for i in range(len(points)):
        temp = -points[i][0]
        points[i][0] = -points[i][1]        
        points[i][1] = temp        
        
        
        
        
        
        
        
        
        
        
        
        
    
