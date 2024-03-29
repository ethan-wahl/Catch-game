import pygame, simpleGE, random

#!/usr/bin/env python3


# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:33:42 2024

@author: ethan
"""

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init(scene)
        self.setImage("coin.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
        
    def reset(self):
        self.y = 10
        
        self.x = random.randint(self.screenWidth)
        
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class Tornado(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("EF3.png")
        self.setSize(50,50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("TC.png")
        
        self.sndTor = simpleGE.sound("tor.wav")
        self.tornado = Tornado(self)
        self.coin = Coin(self)
        
        self.sprites = [self.tornado, 
                        self.coin]
                
    def process(self):
        if self.coin.collidesWith(self.tornado):
            self.sndcoin.play()
        
def main():
    game = Game()
    game.start()