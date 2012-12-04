# Importamos el module pygame, sys y a la misma vez utilizamos las series de constantes cuando hacemos from
import pygame, sys
from pelea import pelea,Rakip,Atak
import random

pygame.init()
 
pencere = pygame.display.set_mode((1000,600))

#Posicion de cada Jugador
asker = pelea((0,100),pencere)
rakip = Rakip ((850,100), pencere)
atak = Atak((150,100))
sari = (112,111,111)
saat = pygame.time.Clock()

# La barra de vida de cada Jugador
def ynkntrl():
    if asker.x() > rakip.x():
        rakip.ynr =  True
        asker.ynr = True
    if rakip.x() > asker.x():
        rakip.ynr = False
        asker.ynr = False

#Para cada golpe..., el cual le baja la vida al jugador 1 y jugador 2
def kntrl ():
    if asker.can < 1 :
        asker.olum = True
    if asker.rect.collidepoint(rakip.pos()):
        if asker.atak1 == True:
            rakip.canr(-1)
        if asker.atak2 == True:
            rakip.canr(-0.25)           
        if rakip.atak1 == True:
            asker.canr(1)
        if rakip.atak2 == True:
            asker.canr (1.25)
            
    if rakip.rect.collidepoint(asker.pos()):
        
        if asker.atak1 == True:
            rakip.canr(-1)
        if asker.atak2 == True:
            rakip.canr(-0.25)           
        if rakip.atak1 == True:
            asker.canr(0.25)
        if rakip.atak3 == True:
            asker.canr(1)
        if rakip.atak2 == True:
            asker.canr (0.25)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
    pencere.fill((0,0,0))
   
    asker.update()
    
    
    
    
    kntrl()
    ynkntrl()
    # Posiciones de los Jugadores
    pencere.blit(asker.prf, (0,0))
    pencere.blit(rakip.prf, (930,0))
    pencere.blit(asker.image, asker.rect)
    asker.draw()
    pencere.blit(rakip.image, rakip.rect)
    rakip.draw()
    rakip.update()
    
   
    pygame.display.flip()
    saat.tick(14)
