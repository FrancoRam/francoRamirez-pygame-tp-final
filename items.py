import pygame
from constantes import *
from auxiliar import Auxiliar
class Items:
    def __init__(self,x,y,w,h, type=1) -> None:

        self.image = Auxiliar.getSurfaceFromSpriteSheet_2("images\icon_pack\BG 4b.png",16,22, w, h)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ground_collition_rect = pygame.Rect(self.rect.x,self.rect.y, self.rect.w, ANCHO_COLISIONADOR_PLATAFORMA)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if(DEBUG):
            pygame.draw.rect(screen, "blue",self.ground_collition_rect)
           
        


