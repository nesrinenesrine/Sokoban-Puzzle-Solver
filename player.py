from email.mime import image
from mimetypes import init
from re import M
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y) :
        super().__init__()
        self.sprite_sheet=pygame.image.load('Sokoban pack\PNG\Character4.png')
        self.image=self.get_image()
        self.image.set_colorkey([0,0,0])
        self.rect=self.image.get_rect()
        self.position=[x,y]
    
    def move(self,node):
        for i in range(len(node)) :
            for j in range(len(node[0])) :
                if node[i][j]=='R' or node[i][j]=='.' :
                    self.position=[64*j, 64*i]
                    break
                
    def update(self):
        self.rect.topleft=self.position
        
    def get_image(self):
        image=pygame.Surface([64,64])
        image.blit(self.sprite_sheet,(0,0))
        return image
        
            
        