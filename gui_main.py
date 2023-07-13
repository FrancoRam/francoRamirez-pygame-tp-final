import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import Form
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB
from gui_form_menu_C import FormMenuC
from gui_form_menu_principal import FormMenuPrincipal
from gui_form_menu_game_l1 import FormGameLevel1
from gui_form_menu_game_l2 import FormGameLevel2
from gui_form_menu_game_l3 import FormGameLevel3
from gui_form_levels import FormMenuLevels
from gui_form_settings import FormMenuSettings
from gui_form_game_over import FormGameOver
from gui_form_game_complete import FormGameComplete


flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
info = pygame.display.Info()





form_menu_principal = FormMenuPrincipal(name="form_menu_principal", master_surface=screen,x=150,y=50,w=700,h=600,color_background="black",color_border=None,active=True)
form_menu_A = FormMenuA(name="form_menu_A",master_surface=screen,x=150,y=50,w=700,h=600,color_background="black",color_border=None,active=False)
form_menu_B = FormMenuB(name="form_menu_B",master_surface=screen,x=150,y=50,w=700,h=600,color_background="black",color_border=None,active=False)
form_menu_C = FormMenuC(name="form_menu_C",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=None,active=False)

form_menu_levels = FormMenuLevels(name="form_menu_levels",master_surface=screen,x=150,y=50,w=700,h=600,color_background="black",color_border=None,active=False)
form_menu_settings = FormMenuSettings(name="form_menu_settings",master_surface=screen,x=150,y=50,w=700,h=600,color_background="black",color_border=(14, 98, 81),active=False)

form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background="black",color_border="black",active=False)
form_game_L2 = FormGameLevel2(name="form_game_L2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background="black",color_border="black",active=False)
form_game_L3 = FormGameLevel3(name="form_game_L3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background="black",color_border="black",active=False)

form_game_over = FormGameOver(name="form_game_over",master_surface=screen,x=150,y=50,w=700,h=600,color_background="black",color_border=None,active=False)
form_game_complete = FormGameComplete(name="form_game_complete",master_surface=screen,x=150,y=50,w=700,h=600,color_background="black",color_border=None,active=False)
pygame.init()

while True:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()

    if(aux_form_active != None):
        aux_form_active.update(lista_eventos,keys,delta_ms)
        aux_form_active.draw()

    pygame.display.flip()




    


  



