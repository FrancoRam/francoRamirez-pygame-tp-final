import pygame
from constantes import *
from auxiliar import Auxiliar


class Plataform:
    # def __init__(self, x, y,width, height,  type=1):
        
    #     #self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/tileset/forest/Tiles/{0}.png",1,18,flip=False,w=width,h=height)
    #     self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images\Textures-16.png",1,18,flip=False,w=width,h=height)
    #     self.image = self.image_list[type]
    #     self.rect = self.image.get_rect()
    #     self.rect.x = x
    #     self.rect.y = y
    #     self.collition_rect = pygame.Rect(self.rect)
    #     self.ground_collition_rect = pygame.Rect(self.rect)
    #     self.ground_collition_rect.height = GROUND_COLLIDE_H

    # def draw(self,screen):
    #     screen.blit(self.image,self.rect)
    #     if(DEBUG): 
    #         pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
    #         pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)



    # def __init__(self, x, y,width, height,  type=1):
    #     #self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/tileset/forest/Tiles/{0}.png",1,18,flip=False,w=width,h=height)
    def __init__(self, x, y,width, height,  type=1) -> None:
#        path, columnas,filas, tam_w, tam_h, flip=False
        self.image = Auxiliar.getSurfaceFromSpriteSheet_2("images\Textures-16.png",32,32,width, height)[type]
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ground_collition_rect = pygame.Rect(self.rect.x,self.rect.y, self.rect.w, ANCHO_COLISIONADOR_PLATAFORMA)
        self.rect_piso = pygame.Rect(0,ALTO_VENTANA * 0.9, ANCHO_VENTANA, ANCHO_COLISIONADOR_PLATAFORMA)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if(DEBUG):
            #pygame.draw.rect(screen, "red", self.rect)
            pygame.draw.rect(screen, "blue",self.ground_collition_rect)
            pygame.draw.rect(screen, "blue", self.rect_piso)
        #self.image = self.animation[self.frame]
        
        