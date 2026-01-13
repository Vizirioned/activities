import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


vertices = [
    (0, 1, 0),   # 1
    (0, -1, 0),  # 3
    (-1, 0, -1), # 2
    (1, 0, -1), 
    (1, 0, 1),
    (-1, 0, 1),
]


faces = [
    (0, 2, 3),
    (0, 3, 4),
    (0, 4, 5),
    (0, 5, 2),
    (1, 3, 2),
    (1, 4, 3),
    (1, 5, 4),
    (1, 2, 5),
]


colors = [
    (1, 0, 0),  
    (0, 1, 0),   
    (0, 0, 1),   
    (1, 1, 0),   
    (1, 0, 1),  
    (0, 1, 1),   
    (1, 0.5, 0), 
    (0.5, 0, 1)  
]

def draw_diamond():
    glBegin(GL_TRIANGLES)
    for i, face in enumerate(faces):
        glColor3fv(colors[i])  
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -6)  

   
    rot_x, rot_y, rot_z = 0, 0, 0
    scale = 1.0
    move_x, move_y = 0, 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

       
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]: rot_y -= 2
        if keys[K_RIGHT]: rot_y += 2
        if keys[K_UP]: rot_x -= 2
        if keys[K_DOWN]: rot_x += 2
        if keys[K_q]: rot_z -= 2
        if keys[K_e]: rot_z += 2

        if keys[K_w]: move_y += 0.1
        if keys[K_s]: move_y -= 0.1
        if keys[K_a]: move_x -= 0.1
        if keys[K_d]: move_x += 0.1

        if keys[K_z]: scale += 0.05
        if keys[K_x]: scale = max(0.1, scale - 0.05)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

        glPushMatrix()
        glTranslatef(move_x, move_y, 0)
        glScalef(scale, scale, scale)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)
        glRotatef(rot_z, 0, 0, 1)

        draw_diamond()
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
