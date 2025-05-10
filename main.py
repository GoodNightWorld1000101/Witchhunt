from typing import Any
import pygame
import time
import random
from objects.Player import Cardmaster
from objects.witch import Witch
from objects.laser import Laser
from objects.card import Card
import sys
from fight_related_functions import*
from Movement_functions import*
from States import Game_states 
from global_variables import Global
from objects.conf import SCREEN_WIDTH,SCREEN_HEIGHT,BACKGROUND,BUTTONS
from graphic_functions import*


#Ideas/outside of coding tasks
"1.draw main menu,pause,settings and game over screens"
"2.draw new attack for blue witch"
"3.generate block/dodge for the player"
"4.after 3rd level change game view from up and down to classic platformer"
"5.give blue witch sychte type attack or following bullet that updates direction for a limited amount of time"

#TODO:
# 1.Scaling overscales some sprites and projectiles speed needs to be scaled,
# also fix boundires and make them scales.
# 2.implement heal drop.
# 3.implement boss and some music 


 
#init
pygame.init()
gs = Game_states()
info_struct= Global(SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Witch Hunt")
state = gs.main_menu
#screen menu button picture keys
start_screen_keys = ["start","settings","quit"]
pause_screen_keys = ["start","settings","main menu"]
settings_screen_keys = ["1920x1080","1600x900","1366x768"]

background= BACKGROUND



while True:
    screen.fill((0,0,0))

    if state == gs.main_menu: 

        "cursor coordinates"
        mx , my = pygame.mouse.get_pos()

        if BUTTONS["start"].rect.collidepoint((mx,my)):
            BUTTONS["start"].state = 1
            if gs.main_menu_click: 
                gs.main_menu_click = False  
                state = gs.game_on
                if info_struct.player == None:
                    info_struct.add_player()
                screen.fill((0,0,0))
        else:
            BUTTONS["start"].state = 0
        
        if BUTTONS["settings"].rect.collidepoint((mx,my)):
            BUTTONS["settings"].state = 1
            if gs.main_menu_click: 
                gs.main_menu_click = False
                state = gs.settings
        else:
            BUTTONS["settings"].state = 0
        
        if BUTTONS["quit"].rect.collidepoint((mx,my)):
            BUTTONS["quit"].state = 1
            if gs.main_menu_click: 
                gs.main_menu_click = False
                pygame.quit()
                break
        else:
            BUTTONS["quit"].state = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    gs.main_menu_click = True

        for i in start_screen_keys:
            BUTTONS[i].draw(screen)
    
    if state == gs.game_on:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    break       
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        state = gs.pause
            
        screen.blit(background,(0,0))
            
        if len(info_struct.witches)==0 and gs.enemies_alive == True:
            gs.round_won_timer=time.time()
            gs.enemies_alive = False
        
        if len(info_struct.witches)==0 or None:
            if time.time()-gs.round_won_timer<=1.5:
                round_over(gs.round,screen)
            else:
                gs.round+=1
                spawn_enemies(gs.round,info_struct)
                gs.enemies_alive = True
        
        if info_struct.player.HP()<=0:
            round_over(-1,screen)
            info_struct.reset()
            gs.reset()
            state = gs.main_menu
        else:
            move(info_struct.player,info_struct)
            life(info_struct.player,screen)
            """Draw all the Objects"""
            draw_numbers(info_struct,screen,gs.get_score())
            for i in info_struct.witches:
                i.draw(screen)
                if i.hp == -100:
                    gs.add_points(i.points)
                    i.kill()
                
            info_struct.player.draw(screen)
            info_struct.cards.draw(screen)
            info_struct.spells.draw(screen)
            info_struct.dead_witches.draw(screen)
            
            hitboks(info_struct)

            if time.time()-gs.enemy_spell_timer >= 1:
                gs.enemy_spell_timer = time.time()
                
                for i in info_struct.witches:
                    arv=random.randint(0,5)
                    if arv == 3 and (i.who == "blue" or i.who == "red"):
                        info_struct.add_spell(Laser(i.rect.x,i.rect.y))           
            
            """all Object updates"""
            move(info_struct.player,info_struct)
            info_struct.spells.update(info_struct)
            info_struct.player.Move(info_struct.screen_width,info_struct.screen_height)
            info_struct.player.update()
            info_struct.cards.update(info_struct)
            info_struct.witches.update(info_struct)
    
    elif state == gs.pause:
        screen.fill((0,0,0))
        """resolution scaling during gameplay here"""
        mx , my = pygame.mouse.get_pos()
        if BUTTONS["start"].rect.collidepoint((mx,my)):
            BUTTONS["start"].state = 1
            if gs.main_menu_click: 
                gs.main_menu_click = False
                state = gs.game_on
        else:
            BUTTONS["start"].state = 0
        
        if BUTTONS["settings"].rect.collidepoint((mx,my)):
            BUTTONS["settings"].state = 1
            if gs.main_menu_click: 
                gs.main_menu_click = False
                state = gs.settings
                
        else:
            BUTTONS["settings"].state = 0
        
        if BUTTONS["quit"].rect.collidepoint((mx,my)):
            BUTTONS["quit"].state = 1
            if gs.main_menu_click: 
                gs.main_menu_click = False
                state = gs.main_menu
        else:
            BUTTONS["quit"].state = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    gs.main_menu_click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    break
                elif event.key == pygame.K_SPACE:
                    state = gs.game_on
        for i in pause_screen_keys:
            BUTTONS[i].draw(screen)
    
    elif state == gs.settings:
        screen.fill((0,0,0))
        """resolution scaling during gameplay here"""
        mx , my = pygame.mouse.get_pos()
        if BUTTONS["1920x1080"].rect.collidepoint((mx,my)):
            BUTTONS["1920x1080"].state = 1
            if gs.main_menu_click: 
                gs.main_menu_click = False
                state = gs.pause
                screen,background = resize(info_struct,1980,1080)
                gs.current_window_size = "1920x1080"
        else:
            BUTTONS["1920x1080"].state = 0
        
        if BUTTONS["1600x900"].rect.collidepoint((mx,my)):
            BUTTONS["1600x900"].state = 1
            if gs.main_menu_click: 
                gs.main_menu_click = False
                state = gs.pause
                screen,background = resize(info_struct,1600,900)
                gs.current_window_size = "1600x900"
        else:
            BUTTONS["1600x900"].state = 0
        
        if BUTTONS["1366x768"].rect.collidepoint((mx,my)):
            BUTTONS["1366x768"].state = 1
            if gs.main_menu_click: 
                gs.main_menu_click = False
                state = gs.pause
                screen,background = resize(info_struct,1366,768)
                gs.current_window_size = "1366x768"
        else:
            BUTTONS["1366x768"].state = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    gs.main_menu_click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    break
                elif event.key == pygame.K_SPACE:
                    state = gs.game_on
        for i in settings_screen_keys:
            BUTTONS[i].draw(screen)
        

    #update display
    pygame.display.flip()