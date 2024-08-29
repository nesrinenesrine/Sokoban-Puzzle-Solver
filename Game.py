from email.policy import default
from re import X
from xml.etree.ElementInclude import default_loader
import pygame
import pytmx
import pyscroll
from player import Player
from bloc import Bloc
from time import sleep
from search import *

class Game():
    def __init__(self,x,y,nb_bloc,interface) :
        self.x=x
        self.y=y
        self.nb_bloc=nb_bloc
        self.interface=interface
        
        self.screen=pygame.display.set_mode((x,y))
        pygame.display.set_caption("sokoban")
        tmx_data=pytmx.util_pygame.load_pygame(interface)
        
        map_data=pyscroll.data.TiledMapData(tmx_data)
        map_layer=pyscroll.orthographic.BufferedRenderer(map_data ,self.screen.get_size())
        self.group=pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=2)
        
        player_position=tmx_data.get_object_by_name("player")
        self.player=Player(player_position.x,player_position.y)
        self.group.add(self.player)

        self.bolcs=[]
        
        
            
        
        if (nb_bloc==1):
            name_bloc=tmx_data.get_object_by_name("bloc")
            self.bolcs.append(Bloc(name_bloc.x ,name_bloc.y))
        else:
            for i in range(1,self.nb_bloc+1):
                name_bloc="bloc"+str(i)
                name_bloc=tmx_data.get_object_by_name(name_bloc)
                self.bolcs.append(Bloc(name_bloc.x, name_bloc.y))
    
        self.group.add(self.bolcs)
        
        
    def simulation(self,board):
        initial_node = create_initial_node(board=board)
        #goalNode, num_steps = Search.breadthFirst(initial_node)
        goalNode, num_steps = Search.A(initial_node,heuristic=3)
        if goalNode:
            #print (f"Optimal Solution found after {num_steps} steps")
            solutions = goalNode.getSolution()        
            t=len(solutions)-1
            for solution in solutions:
                self.player.move(solution)
                Bloc.move(self.bolcs,solution)
                self.group.update() 
                self.group.draw(self.screen)
                pygame.display.flip()
                sleep(1)
        return  t
    

    def run(self):
        running=True
       
        while running:
            
            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()


