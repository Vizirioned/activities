from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("05 Lab 1 - Five Cube Object")

# enable depth testing so cubes occlude correctly
glEnable(GL_DEPTH_TEST)

# simple perspective camera
gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)

# object transform state (we'll transform the whole object)
obj_tx = 0.0
obj_ty = 0.0
obj_tz = -10.0
obj_scale = 1.0
obj_rot = 0.0

def draw_cube():
    """Draw a unit cube centered at the origin using GL_QUADS.
    No glColor calls here — colors are set by caller before calling draw_cube().
    """
    glBegin(GL_QUADS)
    # front face
    glVertex3f(-1, -1,  1)
    glVertex3f( 1, -1,  1)
    glVertex3f( 1,  1,  1)
    glVertex3f(-1,  1,  1)
    # back face
    glVertex3f(-1, -1, -1)
    glVertex3f(-1,  1, -1)
    glVertex3f( 1,  1, -1)
    glVertex3f( 1, -1, -1)
    # left face
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1,  1)
    glVertex3f(-1,  1,  1)
    glVertex3f(-1,  1, -1)
    # right face
    glVertex3f(1, -1, -1)
    glVertex3f(1,  1, -1)
    glVertex3f(1,  1,  1)
    glVertex3f(1, -1,  1)
    # top face
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1,  1)
    glVertex3f( 1, 1,  1)
    glVertex3f( 1, 1, -1)
    # bottom face
    glVertex3f(-1, -1, -1)
    glVertex3f( 1, -1, -1)
    glVertex3f( 1, -1,  1)
    glVertex3f(-1, -1,  1)
    glEnd()

def draw_object():
    """Draw an object made of 5 cubes (center + up/down/left/right).
    Each cube has its own color and local transform. We use push/pop matrix
    to isolate each cube's transform.
    """
    # center cube (red)
    glPushMatrix()
    glScalef(0.8, 0.8, 0.8)
    glColor3f(1.0, 0.0, 0.0)
    draw_cube()
    glPopMatrix()

    # top cube (green)
    glPushMatrix()
    glTranslatef(0.0, 2.2, 0.0)
    glScalef(0.6, 0.6, 0.6)
    glColor3f(0.0, 1.0, 0.0)
    draw_cube()
    glPopMatrix()

    # bottom cube (blue)
    glPushMatrix()
    glTranslatef(0.0, -2.2, 0.0)
    glScalef(0.6, 0.6, 0.6)
    glColor3f(0.0, 0.0, 1.0)
    draw_cube()
    glPopMatrix()

    # left cube (yellow)
    glPushMatrix()
    glTranslatef(-2.2, 0.0, 0.0)
    glScalef(0.6, 0.6, 0.6)
    glColor3f(1.0, 1.0, 0.0)
    draw_cube()
    glPopMatrix()

    # right cube (magenta)
    glPushMatrix()
    glTranslatef(2.2, 0.0, 0.0)
    glScalef(0.6, 0.6, 0.6)
    glColor3f(1.0, 0.0, 1.0)
    draw_cube()
    glPopMatrix()


def handle_key(key):
    """Modify the global object transform based on a key press."""
    global obj_tx, obj_ty, obj_tz, obj_scale, obj_rot
    step = 0.3
    sstep = 0.05
    rstep = 5.0
    if key == K_a:
        obj_tx -= step
    elif key == K_d:
        obj_tx += step
    elif key == K_w:
        obj_ty += step
    elif key == K_s:
        obj_ty -= step
    elif key == K_z:  # move closer
        obj_tz += step
    elif key == K_x:  # move farther
        obj_tz -= step
    elif key == K_q:  # scale down
        obj_scale = max(0.1, obj_scale - sstep)
    elif key == K_e:  # scale up
        obj_scale += sstep
    elif key == K_r:  # rotate
        obj_rot += rstep


running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handle_key(event.key)

    # clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # reset modelview, apply camera + object transforms
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(obj_tx, obj_ty, obj_tz)
    glScalef(obj_scale, obj_scale, obj_scale)
    glRotatef(obj_rot, 0, 1, 0)

    draw_object()

    pygame.display.flip()
    # cap to 60fps
    clock.tick(60)

pygame.quit()
