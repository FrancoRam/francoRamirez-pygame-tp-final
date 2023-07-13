import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_label import Label


class FormGameOver(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

          
        self.boton4 = Button(master=self,x=0,y=450,w=200,h=40,color_background=None,color_border=None,image_background="images\gui\set_gui_01\Pixel_Border\Elements\Element05s.png",on_click=self.on_click_boton1,on_click_param="form_menu_principal",text="BACK MENU",font="Comicsansms",font_size=20,font_color=C_BLACK)
        self.label_title_menu = Label(master=self,x=125,y=100,w=450,h=60,color_background=None,color_border=None, image_background="images\gui\set_gui_01\Paper\Frames\Frames_Menu03_b.png", text="OPS, GAME OVER!", font="Comicsansms",font_size=40, font_color=(110, 44, 0))
        
        self.lista_widget = [self.boton4,self.label_title_menu]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()