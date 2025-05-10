import pygame
from objects.conf import FULL_HEART,EMPTY_HEART,HALF_HEART,SCREEN_HEIGHT,SCREEN_WIDTH,BACKGROUND,BUTTONS,NUMBERS

pygame.init()

def draw_numbers(info_struct,screen:object,player_score:int):
    number_list=str(player_score)
    screen_x_position = 50
    for i in range(len(number_list)):
        j=len(number_list)-1-i
        screen.blit(NUMBERS[int(number_list[j])],(info_struct.screen_width - info_struct.screen_width*(screen_x_position/1540),info_struct.screen_height-50/SCREEN_HEIGHT*info_struct.screen_height))
        screen_x_position += 25

def life(player:object,screen:object)->None:
    """shows full and empty hearts on screen based on the player life points, using scales to calculate the position of the hearts"""
    if player.HP()==3:
        screen.blit(FULL_HEART,(0,0.9125*screen.get_height()))
        screen.blit(FULL_HEART,(0.0325*screen.get_width(),0.9125*screen.get_height()))
        screen.blit(FULL_HEART,(0.065*screen.get_width(),0.9125*screen.get_height()))
    elif player.HP()==2.5:
        screen.blit(FULL_HEART,(0,0.9125*screen.get_height()))
        screen.blit(FULL_HEART,(0.0325*screen.get_width(),0.9125*screen.get_height()))
        screen.blit(HALF_HEART,(0.065*screen.get_width(),0.9125*screen.get_height()))
    elif player.HP()==2:
        screen.blit(FULL_HEART,(0,0.9125*screen.get_height()))
        screen.blit(FULL_HEART,(0.0325*screen.get_width(),0.9125*screen.get_height()))
        screen.blit(EMPTY_HEART,(0.065*screen.get_width(),0.9125*screen.get_height()))
    elif player.HP()==1.5:
        screen.blit(FULL_HEART,(0,0.9125*screen.get_height()))
        screen.blit(HALF_HEART,(0.0325*screen.get_width(),0.9125*screen.get_height()))
        screen.blit(EMPTY_HEART,(0.065*screen.get_width(),0.9125*screen.get_height()))
    elif player.HP()==1:
        screen.blit(FULL_HEART,(0,0.9125*screen.get_height()))
        screen.blit(EMPTY_HEART,(0.0325*screen.get_width(),0.9125*screen.get_height()))
        screen.blit(EMPTY_HEART,(0.065*screen.get_width(),0.9125*screen.get_height()))   
    elif player.HP()==0.5:
        screen.blit(HALF_HEART,(0,0.9125*screen.get_height()))
        screen.blit(EMPTY_HEART,(0.0325*screen.get_width(),0.9125*screen.get_height()))
        screen.blit(EMPTY_HEART,(0.065*screen.get_width(),0.9125*screen.get_height()))
    elif player.HP()<=0:
        screen.blit(EMPTY_HEART,(0,0.9125*screen.get_height()))
        screen.blit(EMPTY_HEART,(0.0325*screen.get_width(),0.9125*screen.get_height()))
        screen.blit(EMPTY_HEART,(0.065*screen.get_width(),0.9125*screen.get_height()))
        player.kill() 

def draw_text(text:str,surface:object,x:int,y:int)-> None:
    """Function to put text on screen"""
    font = pygame.font.Font('freesansbold.ttf', 30)
    textobj = font.render(text,1,(255,255,255))
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect) 

def round_over(Round_nr:int,screen:object)->None:
    """Function to mark the end of a round"""
    font = pygame.font.Font('freesansbold.ttf', 30)
    if Round_nr == -1:
        text = font.render('GAME OVER', True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
        screen.blit(text,textRect)
    else:
        round = font.render('ROUND '+str(Round_nr), True, (255,255,255), (0,0,0))
        roundrect = round.get_rect()
        roundrect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        screen.blit(round,roundrect)

def resize(info_struct:object,new_width:int,new_height:int) -> (object,list): 
    """Function to resize screen,background,enemies and player
    returns screen object and background image"""

    width_scale = new_width/info_struct.screen_width
    height_scale = new_height/info_struct.screen_height
    
    background = pygame.transform.scale(BACKGROUND,(info_struct.screen_width*width_scale,info_struct.screen_height*height_scale))
    
    for sprite in info_struct.witches:
        sprite.resize(width_scale,height_scale)

    info_struct.player.resize(width_scale,height_scale)
    
    info_struct.screen_height *= height_scale
    info_struct.screen_width *= width_scale
    screen = pygame.display.set_mode((info_struct.screen_width,info_struct.screen_height),pygame.RESIZABLE)
 
    for i in BUTTONS.values():
        i.resize(width_scale,height_scale,info_struct)
        
    return screen,background