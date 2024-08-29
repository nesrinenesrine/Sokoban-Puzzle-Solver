from unicodedata import name
from sokoPuzzle import SokoPuzzle
from node import Node
from Game import Game
import pygame
import pytmx
import pyscroll
from search import *
from tkinter import *


if __name__=='__main__':
       pygame.init()

       # game=Game(576,576,1,"interface2.tmx")
       # t=game.simulation(board2)

       # game=Game(448,576,3,"interface4.tmx")
       # t=game.simulation(board4)

       game=Game(576,512,3,"interface5.tmx")
       t=game.simulation(board5)

       window=Tk()
       window.geometry("400x30")
       window.title("Le nombre d'itération")
       text="Le nombre d'itération est:"+str(t)
       lable=Label(window,text=text,font=('Arial',10,'bold'),fg='#000000',bg='#FFDAB9')
       lable.pack()
       window.mainloop()
       

       
       
       
       
       


# #l'image dans le poly
# board=[['O','O','O','O','O','O','O','O'],
#        ['O','O','O',' ',' ',' ','O','O'],
#        ['O','.',' ','B',' ',' ','O','O'],
#        ['O','O','O',' ','B','S','O','O'],
#        ['O','S','O','O','B',' ','O','O'],
#        ['O',' ','O',' ','S',' ','O','O'],
#        ['O','B',' ','*','B','B','S','O'],
#        ['O',' ',' ',' ','S',' ',' ','O'],
#        ['O','O','O','O','O','O','O','O']]
# node=SokoPuzzle()

# #init_node=Node(SokoPuzzle(board))
