import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_label import Label


class FormMenuPrincipal(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        
        #self.volume_incremental = Button(master=self,x=20,y=60,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\set_gui_01\Pixel_Border\Elements\Element05s.png",on_click=self.on_click_volume_incremental,on_click_param="",text="SUMA +",font="comicsansms",font_size=30,font_color="Brown")   #van a manejar el volumen
        #self.volume_decrement = Button(master=self,x=20,y=120,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\set_gui_01\Pixel_Border\Elements\Element05s.png",on_click=self.on_click_volume_decrement,on_click_param="",text="RESTA -",font="comicsansms",font_size=30,font_color="Brown") #van a manejar el volumen
        #self.txt1 = TextBox(master=self,x=200,y=100,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",text="Text",font="Verdana",font_size=30,font_color=C_BLACK)
        #self.pb1 = ProgressBar(master=self,x=200,y=200,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 3, value_max=8)
        
        self.boton_banner = Label(master=self,x=125,y=100,w=450,h=60,color_background=None,color_border=None, image_background="images\gui\set_gui_01\Paper\Frames\Frames_Menu03_b.png", text="TERRA", font="Comicsansms",font_size=40, font_color=(110, 44, 0))

        self.boton_levels = Button(master=self,x=110,y=340,w=150,h=60,color_background=None,color_border=None,image_background="images\gui\set_gui_01\Pixel_Border\Elements\Element05s.png",on_click=self.on_click_boton3,on_click_param="form_menu_levels",text="Levels",font="comicsansms",font_size=30,font_color="Brown")

        self.boton3 = Button(master=self,x=110,y=270,w=150,h=60,color_background=None,color_border=None,image_background="images\gui\set_gui_01\Pixel_Border\Elements\Element05s.png",on_click=self.on_click_boton3,on_click_param="form_game_L1",text="PLAY",font="comicsansms",font_size=30,font_color="Brown")
        self.boton4 = Button(master=self,x=270,y=270,w=150,h=60,color_background=None,color_border=None,image_background="images\gui\set_gui_01\Pixel_Border\Elements\Element05s.png",on_click=self.on_click_boton3,on_click_param="form_menu_B",text="Score",font="comicsansms",font_size=30,font_color="Brown")
        self.boton5 = Button(master=self,x=430,y=270,w=150,h=60,color_background=None,color_border=None,image_background="images\gui\set_gui_01\Pixel_Border\Elements\Element05s.png",on_click=self.on_click_boton3,on_click_param="form_menu_settings",text="Settings",font="comicsansms",font_size=30,font_color="Brown")

        
        
        pygame.mixer.init()
        ## volume / music
        self.flag_boton = "images/gui/set_gui_01/Standard/Buttons/audioPlus.png"
        self.boton_volume = Button(master=self,x=460,y=545,w=80,h=50,color_background=None,color_border=None,image_background="images\gui\set_gui_01\Pixel_Border\Elements\Element05s.png",on_click=self.on_off_volume,on_click_param="volume",text="OFF",font="comicsansms",font_size=14,font_color="Brown")
        self.boton_on_of = Label(master=self,x=550,y=550,w=40,h=40,color_background=None,color_border=None, image_background=self.flag_boton, text="", font="Comicsansms",font_size=40, font_color=(110, 44, 0))

        self.volume = 0.2
        self.flag_volume = True
        ##
        pygame.mixer.music.load("music_terra.wav")
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)


        self.lista_widget = [self.boton3,self.boton4,self.boton5,self.boton_banner, self.boton_volume, self.boton_on_of, self.boton_levels] 

    def on_off_volume(self, parametro):
        if self.flag_volume:
            pygame.mixer.music.pause()
            self.boton_volume._text ="ON"
            self.boton_volume._font_color = "Red"
            self.flag_volume = False
        else:
            pygame.mixer.music.unpause()
            self.boton_volume._text = "OFF"
            self.boton_volume._font_color = "Brown"
            self.flag_volume = True

    def on_click_volume_incremental(self, parametro):
        #if self.volume >= 0 and self.volume <= 1: 
        self.pb1.value += 1
        self.volume = self.volume + 0.1

    def on_click_volume_decrement(self, parametro):
        #if self.volume >= 0 and self.volume <= 1:
        self.pb1.value -= 1
        self.volume = self.volume - 0.1

    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()