from ast import main
import pygame
from game import Game
import pytmx

if __name__=='__main__':
    pygame.init()
    game = Game(2)
    game.simulation()
    #game.run()
    
    