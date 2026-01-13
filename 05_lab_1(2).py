from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("05 Lab 1")

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
    glVertex3f(-1, -1,  1)
    glVertex3f( 1, -1,  1)
    glVertex3f( 1,  1,  1)
    glVertex3f(-1,  1,  1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1,  1, -1)
    glVertex3f( 1,  1, -1)
    glVertex3f( 1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1,  1)
    glVertex3f(-1,  1,  1)
    glVertex3f(-1,  1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1,  1, -1)
    glVertex3f(1,  1,  1)
    glVertex3f(1, -1,  1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1,  1)
    glVertex3f( 1, 1,  1)
    glVertex3f( 1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f( 1, -1, -1)
    glVertex3f( 1, -1,  1)
    glVertex3f(-1, -1,  1)
    glEnd()

def draw_object():
    shades = [
        (0.0, 0.3, 0.0, 0.25),
        (0.0, 0.5, 0.0, 0.35),
        (0.0, 0.7, 0.0, 0.45),
        (0.0, 1.0, 0.0, 0.9)
    ]
    scales = [2.0, 1.5, 1.0, 0.5]
    for color, s in zip(shades, scales):
        glPushMatrix()
        glColor4f(*color)
        glScalef(s, s, s)
        draw_cube()
        glPopMatrix()

angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -10)
    glRotatef(angle, 1, 1, 0)
    draw_object()
    pygame.display.flip()
    pygame.time.wait(15)
    angle += 1

pygame.quit()
