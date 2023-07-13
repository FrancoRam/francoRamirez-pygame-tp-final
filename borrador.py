import pygame
from pygame.locals import *

#limpio el gui_main.py
#creo el gui_button.py (boton)


#guid_Widget (gráfica)

class Widget:
    def __init__(self,master_surface, x,y,w,h, color_background,
                 color_border) -> None:
        self.master_surface = master_surface

        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.color_background = color_background
        self.color_border = color_border
    def render(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

#gui_buttom
class Button(Widget):
    def __init__(self, master_surface, x,y,w,h, color_background,
                 color_border, on_click, on_click_parameter, text,font,font_size,font_color) -> None: #master_surface es la screen
        super().__init__(self,master_surface, x,y,w,h, color_background,
                 color_border)
        pygame.font.init()
        self.on_click = on_click
        self.on_click_parameter = on_click_parameter
        self.text = text
        self.font_sys = pygame.font.SysFont(font, font_size)
        self.font = font
        self.font_size = font_size
        self.font_color = font_color


    def render(self):
        image_text = self.font_sys.reder(self._text, self.font_color, self.color_background)
        self.slave_surface.fill((255,0,0))
        self.slave_surface = pygame.surface.Surface((self.w,self.h))
        self.slave_rect = self.slave_surface.get_rect()

        self.slave_surface.blit(image_text, (10,10))
    def update(self):
        self.render()
    def draw(self):

        self.master_surface.blit(self.slave_surface, self.slave_rect)

