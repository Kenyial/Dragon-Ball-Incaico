from pygame.sprite import Sprite
import pygame
import time


class pelea(Sprite):
    
    def __init__(self, konum,screen):
        Sprite.__init__(self)
        self.durus = [pygame.image.load("jugador1/1.PNG")]
        self.yrs = [pygame.image.load("jugador1/2.PNG"), pygame.image.load("jugador1/3.PNG"),pygame.image.load("jugador1/4.PNG"),pygame.image.load("jugador1/5.PNG")]
        self.gc = [pygame.image.load("jugador1/6.PNG")]
        self.atak1=pygame.image.load("jugador1/atak/atak.PNG")
        self.aniatak1 = [pygame.image.load("jugador1/atak/1.PNG"),pygame.image.load("jugador1/atak/2.PNG"),pygame.image.load("jugador1/atak/3.PNG"),pygame.image.load("jugador1/atak/4.PNG")]
        self.aniatak2 = [pygame.image.load("jugador1/atak2/1.PNG"),pygame.image.load("jugador1/atak2/2.PNG")]

        self.image = self.durus[0]
        self.image.set_colorkey((255,255,255))
        
        self.rect =  self.image.get_rect()
        self.surface = screen
        self.prf = pygame.image.load("jugador1/prf/1.bmp")
        self.prf.set_colorkey((255,255,255))
        self.sari = (0,255,0)
        self.can = 150
        self.blit = screen.blit
        self.rect.x, self.rect.y = konum
        self.say = 0
        self.atak2= False
        self.atak1=False
        self.ynr = False
        self.olum = False
        
    def update(self):
        
        if self.olum == False:
            #Movimiento de Imagenes hacia atras
            
            if pygame.key.get_pressed()[pygame.K_a]:
                if self.say >= 4:
                    self.say = 0
                self.rect.x -= 4
                self.atak1 = False
                self.image = pygame.transform.flip(self.yrs[self.say],1,0)
                self.image.set_colorkey((255,255,255))
                self.say += 1
                self.atak2 = False
                
            #Primer Jugador Movimiento de Imagenes hacia delante
            
            if pygame.key.get_pressed()[pygame.K_d]:
                if self.say >= 4:
                    self.say = 0
                self.rect.x += 4
                self.image = self.yrs[self.say]
                self.say += 1
                self.atak1 = False
                self.atak2 = False
                self.image.set_colorkey((255,255,255))
                
            
                    
           #Primer Jugador Golpes que va a dar
            if pygame.key.get_pressed() [pygame.K_j]:
                     if self.ynr == False:
                        if self.say >= 2:
                            self.say = 0
                        self.image = self.aniatak2[self.say]
                        self.say+=1
                            
                        self.image.set_colorkey((255,255,255))    
                        self.atak1 = True
                        if self.say == 2:
                            self.atak1 = True
                        else:
                            self.atak1 = False
                        
                     if self.ynr == True:
                        if self.say >= 2:
                            self.say = 0
                        self.image = pygame.transform.flip(self.aniatak2[self.say],1,0)
                        self.say+=1
                        
                        self.image.set_colorkey((255,255,255))    
                        if self.say == 2:
                            self.atak1 = True
                        else:
                            self.atak1 = False
                        
            #Primer Jugador Golpes que va a dar
            if pygame.key.get_pressed() [pygame.K_g]:
                    if self.ynr == False:
                        if self.say >= 4:
                            self.say = 0
                        self.image = self.aniatak1[self.say]
                        self.say+=1
                        if self.say == 3:
                            self.atak2 = True
                        else:
                            self.atak2 = False
                        self.image.set_colorkey((255,255,255))    
                        
                    if self.ynr == True:
                        
                       
                        if self.say >= 4:
                            self.say = 0
                        self.image = pygame.transform.flip(self.aniatak1[self.say],1,0)
                        self.say+=1
                       
                        self.image.set_colorkey((255,255,255))
                        if self.say == 3:
                            self.atak2 = True
                        else:
                            self.atak2 = False
                        self.image.set_colorkey((255,255,255))    
                    
                
                
        
    def pos (self):
         return self.rect.x,self.rect.y

          
    def draw (self):
        if self.can > 0 :
            
            pygame.draw.rect(self.surface, self.sari, (80,10,self.can,15), 0)
    def eventdown(self, event):
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_q:
                 self.blit(self.atak1,(1,150))
    def x (self):
        return self.rect.x
    def canr (self,sayi):
         self.can = self.can-sayi
         
            
class Atak (Sprite):
     def __init__(self, konum):
          
        self.durus = [pygame.image.load("jugador1/atak/atak.PNG")]
        self.image = self.durus[0]
        self.rect =  self.image.get_rect()
        self.rect.x, self.rect.y = konum
        self.say = 0    

        
        
             
class Rakip (Sprite):
     def __init__(self, konum,screen):
          
        self.durus = [pygame.image.load("jugador2/1.PNG")]
        self.image = self.durus[0]
        self.image.set_colorkey((255,255,255))
        self.rect =  self.image.get_rect()
        self.can = -150
        self.prf = pygame.transform.flip(pygame.image.load("jugador2/prf/1.bmp"),1,0)
        self.prf.set_colorkey((255,255,255))
        self.image.set_colorkey((255,255,255))
        self.rect.x, self.rect.y = konum
        self.say = 0
        self.olum = False
        self.atak = False
        self.atak2 = False
        
        self.atak1=False
        self.ynr = False
        self.kacc = False
        self.ates1= False
        self.ates2 = False
        self.ynr = False        
        self.surface = screen
        self.sari = (0,255,0)
        self.uzak1 = 0
        self.uzak2 = False
        self.atak3 = False
        self.set_colorkey = ((255,255,255))
        
        #Llamadas de Imagenes
        self.dead = [pygame.image.load("jugador2/dead/1.PNG"),pygame.image.load("jugador2/dead/2.PNG"),pygame.image.load("jugador2/dead/3.PNG")
                     ,pygame.image.load("jugador2/dead/4.PNG"),pygame.image.load("jugador2/dead/5.PNG"),pygame.image.load("jugador2/dead/6.PNG")]
        self.yr = [pygame.image.load("jugador2/yr/1.PNG"),pygame.image.load("jugador2/yr/2.PNG"),pygame.image.load("jugador2/yr/3.PNG")
                     ,pygame.image.load("jugador2/yr/4.PNG"),pygame.image.load("jugador2/yr/5.PNG"),pygame.image.load("jugador2/yr/6.PNG")]
        self.yumruk =[pygame.image.load("jugador2/atak1/1.PNG"),pygame.image.load("jugador2/atak1/2.PNG"),pygame.image.load("jugador2/atak1/3.PNG")]
        self.yumruk2 =[pygame.image.load("jugador2/atak2/1.PNG"),pygame.image.load("jugador2/atak2/2.PNG"),pygame.image.load("jugador2/atak2/3.PNG"),pygame.image.load("jugador2/atak2/4.PNG")]
        
    
     def update(self):
         #Movimiento de Imagenes.., o bueno el jugador 2, hacia delante
        if self.olum == False:
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                
                if self.say >= 4:
                    self.say = 0
                    
                self.rect.x -= 4
                
                self.image = pygame.transform.flip(self.yr[self.say],1,0)
                self.image.set_colorkey((255,255,255))
                self.say += 1
                
         #Movimiento de Imagenes.., o bueno el jugador 2, hacia atras dice       
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                
                if self.say >= 4:
                    self.say = 0
                    
                self.rect.x += 4
                self.image = self.yr[self.say]
                self.say += 1
                
                self.image.set_colorkey((255,255,255))
            #Golpes de los jugadores del segundo jugador    
            if pygame.key.get_pressed()[pygame.K_k]:
                
                 if self.ynr == True:
                    if self.say >= 4:
                        self.say = 0
                
                    self.image = self.yumruk2[self.say]
                    self.say += 1
                        
                    self.image.set_colorkey((255,255,255))
                    if self.say == 2:
                        self.atak2 = True
                    else:
                        self.atak2= False
                        
                     
                 if self.ynr == False:
                    if self.say >= 4:
                        self.say = 0
                
                    self.image = pygame.transform.flip(self.yumruk2[self.say],1,0)
                    self.say += 1
                    
                    self.image.set_colorkey((255,255,255))
                    if self.say == 2:
                        self.atak2 = True
                    else:
                        self.atak2= False
                        
            #Golpes del segundo jugador precionando L
            if pygame.key.get_pressed()[pygame.K_l]:
                
                if self.ynr == True:
                    if self.say >= 3:
                        self.say = 0
                        
                    
                    self.image = self.yumruk[self.say]
                    self.say += 1
                    if self.say == 2:
                        self.atak1 = True
                    else:
                        self.atak1= False
                        
                    
                    
                    self.image.set_colorkey((255,255,255))
                    
                if self.ynr == False:
                    if self.say >= 3:
                        self.say = 0
                
                    self.image = pygame.transform.flip(self.yumruk[self.say],1,0)
                    self.say += 1
                    
                    if self.say == 2:
                        self.atak1 = True
                    else:
                        self.atak1= False
                        
                    self.image.set_colorkey((255,255,255))
       
     def pos (self):
         return self.rect.x,self.rect.y

          
     def draw (self):
         
        if self.uzak1 > 70 and  self.uzak1<96 :
            
            self.uzak2 = True
        if self.uzak1 >=97:
            self.uzak1 = 0
            self.uzak2 = False
            
        if self.can < 0 : 
            pygame.draw.rect(self.surface, self.sari, (920,10,self.can,15), 0)
        else:
            if self.ynr == True:
                if self.olum == False:
                    if self.say >= 4:
                        self.say = 0
                        self.olum = True
                    self.rect.x -= 5
                    self.atak1 = False
                    self.image = self.dead[self.say]
                    self.image.set_colorkey((255,255,255))
                    self.say += 1
                    self.atak2 = False 
                
            if self.ynr == False:
                
                if self.olum == False:
                    if self.say >= 4:
                        self.say = 0
                        self.olum = True
                    self.rect.x += 5
                    self.atak1 = False
                    self.image = pygame.transform.flip(self.dead[self.say],1,0)
                    self.image.set_colorkey((255,255,255))
                    self.say += 1
                    self.atak2 = False 
     def eventdown(self, event):
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_q:
                 self.blit(self.atak1,(1,150))
     def x (self):
        return self.rect.x
     def canr (self,sayi):
         self.can = self.can-sayi