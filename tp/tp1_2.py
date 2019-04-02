from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Enter here the binary command that is read when you type ESC
ESCAPE = b'\x1b'

# Number of the glut window.
window = 0

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):            # We call this right after our OpenGL window is created.
    glClearColor(0.0, 1.0, 1.0, 0.0)  # Background color
    glClearDepth(1.0)                 # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)              # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)           # Enables Depth Testing
    glShadeModel(GL_SMOOTH)           # Enables Smooth Color Shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()# Reset The Projection Matrix
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (it should not be called if full screen option is chosen)
def resize_scene(Width, Height):
    if Height == 0:                   # Prevent A Divide By Zero If The Window Is Too Small 
        Height = 1

    glViewport(0, 0, Width, Height)   # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# The main drawing function. 
def draw():
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()# Reset The View 

    # # Move Left 1.5 units and into the screen 6.0 units.
    # glTranslatef(0.0, 0.0, -6.0)

     # Draw
     glBegin(GL_POLYGON)                 # Start drawing a polygon
     glVertex3f(0.0, 1.0, 0.0)           # Top
     glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
     glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
     glEnd()                             # We are done with the polygon

    #  since this is double buffered, swap the buffers to display what just got drawn. 
    glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def key_pressed(*args):
    print(args[0])
    # If escape is pressed, kill everything.
    if args[0]==ESCAPE:
        glutDestroyWindow(window)
        sys.exit(0)

def main():
    global window
    # Start glut with empty argument
    glutInit(())

    # Select type of Display mode:   
    # Double buffer 
    # RGBA color
    # Alpha components supported 
    # Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    
    # Window size
    glutInitWindowSize(400, 400)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)

    # Create a window with GLUT.
    window = glutCreateWindow("Test 1")
    # Binary cast may be required in Windows version
    # window = glutCreateWindow(b"Assignment 1 - pyOpenGL") 

    # Register the drawing function with glut.
    glutDisplayFunc(draw)
    
    # Uncomment this line to get full screen.
    #glutFullScreen()
    # While ESC is not pressed, redraw the scene.
    glutIdleFunc(draw)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(resize_scene)

    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(key_pressed)

    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine.
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print("Press ESC key to kit. The Kernel will be restarted later.")
main()