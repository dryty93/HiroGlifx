# i will intergrate the pygame functions gui abilities to make creating a gui
# application easy as heck!

import pygame_functions

def makeWindow(len,wid):
    while True:
        screen = pygame_functions.screenSize(len,wid)
        if pygame_functions.keyPressed('ENTER'):
            exit('Goodbye!')


