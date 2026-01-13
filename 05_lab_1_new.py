from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("05 Lab 1 - Five Cubes")

glDisable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glClearColor(0.0, 0.0, 0.0, 1.0)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)

def draw_cube():
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(-1, -1,  1)
    glVertex3f( 1, -1,  1)
    glVertex3f( 1,  1,  1)
    glVertex3f(-1,  1,  1)
    
    # Back face
    glVertex3f(-1, -1, -1)
    glVertex3f(-1,  1, -1)
    glVertex3f( 1,  1, -1)
    glVertex3f( 1, -1, -1)
    
    # Left face
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1,  1)
    glVertex3f(-1,  1,  1)
    glVertex3f(-1,  1, -1)
    
    # Right face
    glVertex3f(1, -1, -1)
    glVertex3f(1,  1, -1)
    glVertex3f(1,  1,  1)
    glVertex3f(1, -1,  1)
    
    # Top face
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1,  1)
    glVertex3f( 1, 1,  1)
    glVertex3f( 1, 1, -1)
    
    # Bottom face
    glVertex3f(-1, -1, -1)
    glVertex3f( 1, -1, -1)
    glVertex3f( 1, -1,  1)
    glVertex3f(-1, -1,  1)
    glEnd()

def draw_object():
    # Define 5 different colors with transparency
    colors = [
        (1.0, 0.0, 0.0, 0.7),  # Red
        (0.0, 1.0, 0.0, 0.7),  # Green
        (0.0, 0.0, 1.0, 0.7),  # Blue
        (1.0, 1.0, 0.0, 0.7),  # Yellow
        (1.0, 0.0, 1.0, 0.7)   # Purple
    ]
    
    # Different scales for each cube
    scales = [2.0, 1.6, 1.2, 0.8, 0.4]
    
    # Draw each cube with its color and scale
    for color, s in zip(colors, scales):
        glPushMatrix()
        glColor4f(*color)  # Set the color with transparency
        glScalef(s, s, s)  # Scale the cube
        draw_cube()
        glPopMatrix()

angle_x = 0
angle_y = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle_y -= 5
            if event.key == pygame.K_RIGHT:
                angle_y += 5
            if event.key == pygame.K_UP:
                angle_x -= 5
            if event.key == pygame.K_DOWN:
                angle_x += 5

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -10)
    glRotatef(angle_x, 1, 0, 0)  # Rotate around X axis
    glRotatef(angle_y, 0, 1, 0)  # Rotate around Y axis
    draw_object()
    pygame.display.flip()
    pygame.time.wait(15)

pygame.quit()