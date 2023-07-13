import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from bullet import Bullet
from items import Items

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.ancho = w
        self.alto = h
        self.flag_active = False

        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=100,y=3,w=100,h=30,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="Back",font="comicsansms",font_size=20,font_color="Brown")
        self.boton2 = Button(master=self,x=210,y=3,w=100,h=30,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_A",text="Pause",font="comicsansms",font_size=20,font_color="Brown")
        self.boton_shoot = Button(master=self,x=320,y=3,w=100,h=30,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_shoot,on_click_param="form_menu_B",text="Shoot",font="comicsansms",font_size=20,font_color="Brown")
        self.pb_lives = ProgressBar(master=self,x=600,y=3,w=120,h=30,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)

        

        self.widget_list = [self.boton1,self.boton2,self.pb_lives,self.boton_shoot]

        self.tiempo_juego = 60000 # 60 segundos
        self.tiempo_transcurrido = 0
        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=self.ancho,height=self.alto,path="images/locations/backgrounds-desert/4/background.png")
        self.score_lvl = 0
        self.player_1 = Player(x=0,y=400,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=50,move_rate_ms=50,jump_height=140,p_scale=0.25,interval_time_jump=300)
        self.player_1.lives = 5

        self.enemy_list = []
        self.enemy_list.append (Enemy(x=450,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
        self.enemy_list.append (Enemy(x=900,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))

        self.items_list = []
        self.items_list.append(Items(100,325, 30,30,type=112))
        self.items_list.append(Items(500,325, 30,30,type=113))
        self.items_list.append(Items(700,115, 30,30,type=114))
        
        self.plataform_list = []
        
        
        mapa = [                 
                ["izq","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"," ","x"," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," ","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq","x","x","x","x","x","x","x","x","x","x","x","x"," "," "," ","x","x","x","x","x","x","x","x","x","x"," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," ","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"," "," ","x"," ","der"],
                ["izq"," "," "," "," "," "," "," "," ","x","x","x","x","x","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],
                ["izq"," "," "," "," "," "," "," "," "," "," "," "," "," ","der"],     
                ]
        
        self.w_plataform=32
        self.h_plataform=30
        for row_num,row in enumerate(mapa):
            for column_num,column in enumerate(row):
                x = column_num * 30
                y = row_num * 30
                if column == "x":
                    self.plataform_list.append(Plataform(x,y,width=self.w_plataform,height=self.h_plataform,type=401))
                if column == "izq":
                    self.plataform_list.append(Plataform(x,y,width=self.w_plataform,height=self.h_plataform,type=970))
                if column == "a":
                    self.plataform_list.append(Plataform(x,y,width=self.w_plataform,height=self.h_plataform,type=1))
                if column == "der":
                    self.plataform_list.append(Plataform(ANCHO_VENTANA - 33 ,y,width=self.w_plataform,height=self.h_plataform,type=970))

        self.bullet_list = []

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_shoot(self, parametro):
        for enemy_element in self.enemy_list:
            self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,
                                           self.player_1.rect.centerx,self.player_1.rect.centery,20,
                                           frame_rate_ms=100,move_rate_ms=20,width=5,height=5))
            
    def on_click_shoot_player(self, parametro):
        if self.player_1.direction:
            self.directionX= ANCHO_VENTANA
            self.flag_direction = True
        else:
            self.directionX = 0
            self.flag_direction = False
        self.bullet_list.append(Bullet(self.player_1,self.player_1.rect.centerx,self.player_1.rect.centery,
                            self.directionX,self.get_center_shoot_player()[1],20,
                            frame_rate_ms=100,move_rate_ms=20,width=5,height=5))
        
    def get_center_shoot_player(self):
        self.list_aux = []

        self.list_aux.append(self.player_1.rect.centerx)
        self.list_aux.append(self.player_1.rect.centery)
        return self.list_aux
    
    
    
    def colision_player(self):
        contador = 0
        for enemigo in self.enemy_list:
            if self.player_1.collition_rect.colliderect(enemigo):
                print("IMPACTO ENEMY")
                self.enemy_list.pop(contador)
                self.score_lvl = self.score_lvl + 100
                contador += 1

    def colision_items(self):
        contador = 0
        for item in self.items_list:
            if self.player_1.collition_rect.colliderect(item):
                print("tem recolectado")
                self.items_list.pop(contador)
                self.score_lvl = self.score_lvl + 50
                contador += 1
    def game_over_metod(self):
        if self.player_1.lives <= 0:
            self.set_active("form_game_over")
            self.game_over = True
            self.in_game = False
    def init_lvl(self):
        self.enemy_list = []
        self.items_list = []
        self.player_1 = Player(x=0,y=400,speed_walk=6,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=50,move_rate_ms=50,jump_height=140,p_scale=0.25,interval_time_jump=300)
        self.score_lvl = 0
        self.player_1.lives = 5
        self.tiempo_juego = 60000 # 60 segundos
        self.tiempo_transcurrido = 0
        self.items_list.append(Items(100,325, 30,30,type=112))
        self.items_list.append(Items(500,325, 30,30,type=113))
        self.items_list.append(Items(700,115, 30,30,type=114))
        self.enemy_list.append (Enemy(x=450,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
        self.enemy_list.append (Enemy(x=900,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
        
    def update(self, lista_eventos,keys,delta_ms):
        if self.active and self.flag_active == False:
            self.init_lvl()
            self.flag_active = True
        if len(self.items_list) == 0 and len(self.enemy_list) == 0:
            self.set_active("form_game_complete")
            self.init_lvl()
            self.flag_active = True
        self.tiempo_transcurrido += delta_ms
        print(self.tiempo_transcurrido)
        if self.tiempo_transcurrido >= self.tiempo_juego or self.player_1.lives == 0:
            self.player_1.lives = 0
            self.game_over_metod()
            
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list)

        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list)

        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.on_click_shoot_player("form_menu_B")
                    #self.colision_player()
                if event.key == pygame.K_a:
                    self.colision_player()
                if event.key == pygame.K_r:
                    self.colision_items()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    pass

        self.pb_lives.value = self.player_1.lives 
        if self.pb_lives.value <= 0:
            print("game over")

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for item in self.items_list:
            item.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)