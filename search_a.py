from sokoPuzzle import SokoPuzzle
from node import Node
from collections import deque
import itertools
from copy import deepcopy
import numpy as np

def find_key(dict,v): 
    for k, val in dict.items(): 
        if v == val: 
            return k 

def find_indice(liste,noeud):
    for i in range(liste):
        if(liste[i].state == noeud):
            return i

class SearchA ():
    @staticmethod
    def A(initial_node) :
        if initial_node.state.isGoal(Node.wall_space_obstacle):
            return initial_node, 0
         
        open = list([initial_node]) 
        closed = list() 
        
        step=0
        while True:
            
            print (f'*** Step {step} ***')
            step +=1
            
            if len(open) == 0:
                return None, -1
            
            if len(open) == 1:
                current=open.pop()
                
            heuristic_elm={}
            if len(open)>1:
                for elm in open:
                    heuristic_elm.update({elm,elm.cost})
                    
                l=[]
                for cle, valeur in heuristic_elm.items():
                    l.append(valeur)
                    
                heuristic_min=min(l)
                current=find_key(heuristic_elm,heuristic_min)
                
            open.pop(current)
            closed.append(current)
            if current.state.isGoal(Node.wall_space_obstacle):
                print (f'*** Step {step} ***')
                print ("Goal reached")
                return current, step 
            
            succs = current.succ()
            while len(succs) != 0:
                child = succs.pop()
                child.cost=child.costHeur(1)
                

                # Check if the child is not in the OPEN queue and the CLOSED list
                if (child.state.robot_block not in [n.state.robot_block for n in closed] and \
                    child.state.robot_block not in [n.state.robot_block for n in open]):
                

                    # Put the child in the OPEN queue 
                    open.append(child)    
                elif(child.state.robot_block in [n.state.robot_block for n in open]  ):
                    
                    i=find_indice(open,child.state.robot_block)
                    if(child.cost < open[i].cost):
                        open.pop(i)
                        open.append(child)
                elif(child.state.robot_block  in [n.state.robot_block for n in closed]):
                    
                    
                    
                    

                    
                    
                    
# board1 = [['O', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'S', ' ', 'B', ' ', 'O'],
#         ['O', ' ', 'O', 'R', ' ', 'O'],
#         ['O', ' ', ' ', ' ', ' ', 'O'],
#         ['O', ' ', ' ', ' ', ' ', 'O'],
#         ['O', 'O', 'O', 'O', 'O', 'O']]
            
# def create_initial_node(board=None):        
        
#         height = len(board)
#         width = len(board[0])
                
#         # Separate walls, spaces and obstacles board from robot and boxes board
#         robot_block = [['']*width for _ in range(height)]
#         wall_space_obstacle = [['']*width for _ in range(height)]
        
#         for i, j in itertools.product(range(height), range(width)):
#             if board[i][j] == 'R':
#                 robot_position = (i, j) 
#                 robot_block[i][j] = 'R'
#                 wall_space_obstacle[i][j] = ' '
#             elif board[i][j] == 'B':
#                 robot_block[i][j] = 'B'
#                 wall_space_obstacle[i][j] = ' '
#             elif board[i][j] == 'S' or board[i][j] == 'O' or board[i][j] == ' ':
#                 robot_block[i][j] = ' '   
#                 wall_space_obstacle[i][j] = board[i][j]         
#             elif board[i][j] == '*':
#                 robot_block[i][j] = 'B'
#                 wall_space_obstacle[i][j] = 'S'
#             else: # self.board[i][j] == '.'
#                 robot_position = (i, j) 
#                 robot_block[i][j] = 'R'
#                 wall_space_obstacle[i][j] = 'S'

#         Node.wall_space_obstacle = wall_space_obstacle        
#         initial_node = Node(SokoPuzzle(robot_block, robot_position))

#         return initial_node

# initial_node = create_initial_node(board=board1)
# goalNode, num_steps = SearchA.breadthFirst(initial_node)
# if goalNode:
#     print (f"Optimal Solution found after {num_steps} steps")
#     solution = goalNode.getSolution()        
# else:
#     print ("Optimal solution not found")   


                
            
            
