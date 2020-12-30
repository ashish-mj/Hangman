#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:52:45 2020

@author: ashish
"""

import pygame,os,sys

pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('Hangman')
clock= pygame.time.Clock()


while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    clock.tick(60)
