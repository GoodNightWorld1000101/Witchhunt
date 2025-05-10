from typing import Any
import pygame
from objects.conf import CARD,GOLD_CARD
pygame.init()
class Card(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.size = (30,40)
        self.image = CARD.convert_alpha()
        self.image = pygame.transform.scale(self.image,self.size)
        self.rect = self.image.get_rect()
        self.rect.center = (x ,y )
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = -10
    def resize(self,scale_x:float,scale_y:float):
        self.size = (self.size[0]*scale_x,self.size[1]*scale_y)
        self.velocity *= scale_y
    
    def xandy(self):
        return (self.rect.x,self.rect.y)
    
    def update(self,info_struct):
        if self.rect.y < 10/800*info_struct.screen_height:
            self.image = GOLD_CARD.convert_alpha()
        self.rect.move_ip(0,self.velocity)
        if self.rect.y < 1:
            self.kill()
        #self.image = pygame.image.load(img).convert_alpha()
    