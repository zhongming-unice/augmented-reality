from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import collections
import numpy as np
import sys
import time

# Some api in the chain is translating the keystrokes to this binary string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\x1b'

# Number of the glut window.
window = 0

a = np.loadtxt('ecg.txt')
v = [[x, a[x]] for x in range(len(a))]
dq = collections.deque(maxlen=1000)
index_vertice = 0

def init():
    # Commands # 1 enable or disable server-side GL capabilities
    glEnable(GL_POINT_SMOOTH)  # 1.1 draw points with proper filtering ;permet d'arrondir des points
    glEnable(GL_LINE_SMOOTH)  # 1.2 draw lines with correct filtering ;"lisse" la courbe pour plus de visibilite
    glEnable(
        GL_BLEND)  # 1.3 blend the computed fragment color values with the values in the color buffers ;melange les valeurs de couleurs calcules des fragment avec les valeurs dans le buffer de couleur
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # 1.4  specify pixel arithmetic ;
    # Commands # 2
    glClearColor(1.0, 1.0, 1.0, 1.0)  # 2.1 on color le fond en blanc
    gluOrtho2D(0, 1000, -50, 500)  # 2.2 on cree le repere da la fenetre



def plot_func():
    # Commands # 3
    glClear(GL_COLOR_BUFFER_BIT)  # 3.1 nettoyer des tampons memoire
    glColor3f(0.0, 0.0, 0.0)  # 3.2 definir la coleur noire
    glPointSize(3.0)  # 3.3 taille de point
    glLineWidth(1.0)  # 3.4 taille de l'epaisseur de la courbe

    # Commands # 4 desoine le repere
    glBegin(GL_LINES)
    glColor3f(0.2, 0.2, 0.2)
    glVertex2f(0.0, 0.0)
    glVertex2f(1000.0, 0.0)
    glEnd()

    # Set points to plot graphic
    global index_vertice
    v_deque = dq

    # My computer screen refresh rate is 59
    for i in range(59):
        v_deque.append(v[index_vertice])
        index_vertice += 1
        index_vertice = index_vertice % 15000


    # 0 mV corresponding to the value 2047
    vertices = [[x,v_deque[x][1] - 2047] for x in range(index_vertice if (index_vertice<1000) else 1000)]

    # Commands # 5 relie les points en range pour le trace de la courbe
    for i in range(len(vertices) - 1):
        glBegin(GL_LINES)
        glColor3f(0.8, 0.2, 0.2)
        glVertex2fv(vertices[i])
        glVertex2fv(vertices[i + 1])
        glEnd()

    glBegin(GL_LINES)
    # Light pink(#ffb6c1) = (255/255, 182/255, 193/255) = (1.0, 0.71, 0.76)
    glColor3f(1.0, 0.71, 0.76)
    for i in range(0,1001,25):
        glVertex2i(i, 500)
        glVertex2i(i, -50)
    for i in range(-50,501,10):
        glVertex2i(0, i)
        glVertex2i(1000, i)
    glEnd()




    # Commands # 7 permet d'echanger les valeurs calculees et les valeurs precedentes au fonction mesure
    # since this is double buffered, swap the buffers to display what just got drawn.
    # time.sleep(...)
    glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    print(args[0])
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        glutDestroyWindow(window)
        sys.exit(0)


def main():
    global window
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Function Plotter")
    glutDisplayFunc(plot_func)
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(plot_func)
    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)
    # Initialization
    init()
    # Main drawing loop
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")
main()
