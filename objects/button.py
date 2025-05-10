from typing import Any
import pygame
import time

SCREEN_WIDTH, SCREEN_HEIGHT = 1540, 800

pygame.init()
class BUTTON(pygame.sprite.Sprite):
    
    def __init__(self,pic_1:object,pic_2:object,button_position:float) -> None:
        """Class to create buttons"""
        self.image = pic_1
        self.image_hit = pic_2
        self.button_position = button_position
        self.state = 0
        self.size = (200,50)
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCREEN_WIDTH - self.rect.width) // 2, SCREEN_HEIGHT * button_position)

    def resize(self,width_scale:float,height_scale:float,info_struct:object):
        self.size = (width_scale * self.size[0], height_scale * self.size[1])
        self.image = pygame.transform.scale(self.image,self.size)
        self.image_hit = pygame.transform.scale(self.image_hit,self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = ((info_struct.screen_width - self.rect.width) // 2, info_struct.screen_height * self.button_position)

    def draw(self,surface:object):
        if self.state:
            surface.blit(self.image_hit,self.rect.topleft)
        else:
            surface.blit(self.image,self.rect.topleft)
