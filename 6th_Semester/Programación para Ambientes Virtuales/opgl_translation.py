import pygame
from pygame.locals impor *
from OpenGL.GL import *
from OpenGl.GLU import *

verticer = ((2, -2, -2),
            (-2, -2, -2),
            (0, 2, -2),
            (0, 0, 2))

edges = ((0, 1),
         (0, 2),
         (0, 3),
         (1, 2),
         (1, 3),
         (2, 3))


def Tria():
    glBegin(GL_Lines)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display(1366, 768)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluePerspectives(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            
