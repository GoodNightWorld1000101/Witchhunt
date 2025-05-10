from typing import Any
import pygame
from objects.conf import prayer_pic 
pygame.init()
class Laser(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = prayer_pic.convert_alpha()
        self.size = (30,50)
        self.image = pygame.transform.scale(self.image,self.size)
        self.rect = self.image.get_rect()
        self.rect.center = (x ,y )
        self.mask = pygame.mask.from_surface(self.image)
       
    
    def update(self,info_struct:object):
        if self.rect.y < info_struct.screen_height:
            self.rect.move_ip(0,5)
        else: 
            self.kill()
        #self.image = pygame.image.load(img).convert_alpha()
