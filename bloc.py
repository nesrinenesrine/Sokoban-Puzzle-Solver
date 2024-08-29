from mimetypes import init
from re import M
import pygame

class Bloc(pygame.sprite.Sprite):
    def __init__(self,x,y) :
        super().__init__()
        self.sprite_sheet=pygame.image.load('Sokoban pack\PNG\CrateDark_Gray.png')
        self.image=self.get_image()
        self.image.set_colorkey([0,0,0])
        self.rect=self.image.get_rect()
        self.position=[x,y]
        
    def move(blocs,solution) :
        k=0
        for i in range(len(solution)) :
            for j in range(len(solution[0])) :
                if solution[i][j]=='B'or solution[i][j]=='*' :
                    blocs[k].position=[64*j, 64*i]
                    k=k+1
                if (k==len(blocs)) : 
                    break
                    
    def update(self):
        self.rect.topleft=self.position
        
    def get_image(self):
        image=pygame.Surface([64,64])
        image.blit(self.sprite_sheet,(0,0))
        return image