import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


vertices = [
    (0, 1, 0),    # 1
    (0, -1, 0),   # 3
    (-1, 0, -1),  # 2 
    (1, 0, -1),
    (1, 0, 1),
    (-1, 0, 1),
]


faces = [
    (0, 2, 3), (0, 3, 4), (0, 4, 5), (0, 5, 2),  # 1
    (1, 3, 2), (1, 4, 3), (1, 5, 4), (1, 2, 5),  # 2
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
    
    gluPerspective(45, display[0]/display[1], 0.1, 50.0)

    
    rot_x = rot_y = 0
    move_x = move_y = 0
    zoom = -6  

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # rotate
        if keys[K_LEFT]: rot_y -= 2
        if keys[K_RIGHT]: rot_y += 2
        if keys[K_UP]: rot_x -= 2
        if keys[K_DOWN]: rot_x += 2

       
        if keys[K_a]: move_x -= 0.1 #left
        if keys[K_d]: move_x += 0.1 #right
        if keys[K_w]: move_y += 0.1 #up
        if keys[K_s]: move_y -= 0.1 #down

        
        if keys[K_z]: zoom += 0.1 #laki
        if keys[K_x]: zoom -= 0.1 #liit

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

        glLoadIdentity()  
        glTranslatef(move_x, move_y, zoom)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)

        draw_diamond()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
