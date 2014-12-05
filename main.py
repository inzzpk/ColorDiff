import pygame
from pygame.locals import *

import gamelib
#from elements import Ball, Player
from block import Block

class ColorDiffGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(ColorDiffGame, self).__init__('ColorDiff', ColorDiffGame.WHITE)
        self.level = 2
        self.score = 0
        self.start_time = 60
        self.frame_count = 0
        self.frame_rate = 60
        self.total_seconds = 60



    def init(self):
        self.Repeat = 0
        super(ColorDiffGame, self).init()
        self.block = Block(color = ColorDiffGame.GREEN,level=self.level,score = self.score)
        self.startgame = False
        self.block.constant()
        self.render_score()

    def update(self):
        self.render_time()
        if pygame.mouse.get_pressed() == (1,0,0): # detect left click
            self.Repeat+=1
            if self.Repeat == 1:
                self.mouse_position = [self.posX,self.posY]
                self.block.is_clicked(self.mouse_position,self.level)

        else:
            self.Repeat = 0
            
            if self.block.is_pass() == True:
                self.score += 1
                print(self.score)
                if (self.score>25): self.level = 10
                elif (self.score>22): self.level = 9
                elif (self.score>18): self.level = 8
                elif (self.score>14): self.level = 7
                elif (self.score>10): self.level = 6
                elif (self.score>7): self.level = 5
                elif (self.score>4): self.level = 4
                elif (self.score>1): self.level = 3
            
                self.init()

        self.frame_count += 1
        self.total_seconds = self.start_time - (self.frame_count // self.frame_rate)
        
        if self.total_seconds < 0:
            self.done = True;
            self.total_seconds = 0
        

        
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, ColorDiffGame.GREEN)

    def render_time(self):
        self.time_image = self.font.render("Time left: {0} ".format(self.total_seconds), 0, ColorDiffGame.GREEN)
        


    def render(self, surface):
        self.block.render(surface,self.level,self.score)
        surface.blit(self.score_image, (100,640))
        surface.blit(self.time_image, (250,640))

def main():
    game = ColorDiffGame()
    game.run()

if __name__ == '__main__':
    main()