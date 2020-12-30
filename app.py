#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:52:45 2020

@author: ashish
"""

import pygame,sys

pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('Hangman')
clock= pygame.time.Clock()

white=(255,255,255)

images=[]
for i in range(7):
    image= pygame.image.load("images/hangman"+str(i)+".png")
    images.append(image)
status = 0

while True:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        
        
    window.fill(white)
    window.blit(images[status],(150,100))
    pygame.display.update()
