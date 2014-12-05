import pygame
from pygame.locals import *
import random 

class Block(object):

	BLACK = (0,0,0)
	WHITE = (255,255,255)

	def __init__(self, color,level,score):
		self.colorran1 = random.randrange(0,255)
		self.colorran2 = random.randrange(0,255)
		self.colorran3 = random.randrange(0,255)
		self.colorran = (self.colorran1, self.colorran2, self.colorran3)
		self.level = level
		self.grid = self.create_grid(self.level)
		self.score = score
		self.ranrow   = random.randrange(0,level)
		self.rancol   = random.randrange(0,level) 
		self.Chk_pass = False
		self.grid[self.ranrow][self.rancol] = 1


	def constant(self):
		self.numgrid = [0,0,2,3,4,5,6,7,8,9,10]
		self.sizegrid = [0,0,298,194,143,113,93,80,69,62,56]
		self.sizemargin = [0,0,15,14,13,12,11,10,9,8,7]


	def create_grid(self, level):
		grid = []
		for row in range(level):
			grid.append([])
			for column in range(level):
				grid[row].append(0)
		return grid


	def is_clicked(self,pos,level):
		self.pos = pos
		column = self.pos[0] // (self.sizegrid[level]+self.sizemargin[level])
		row = self.pos[1] // (self.sizegrid[level]+self.sizemargin[level])
		print("Click ", pos, "Grid coordinates: ", row, column)
		if (row==self.ranrow) and (column==self.rancol) :
			print("self.score : ", self.score)
			self.Chk_pass = True
			self.is_pass()	
		self.grid = self.create_grid(self.level)
		self.grid[self.ranrow][self.rancol] = 1 		


	def is_pass(self):
		if self.Chk_pass == True: return True
		else : return False


	def render(self, surface, level, score):
		for row in range(self.level):
			color = self.colorran
			for column in range(self.level):
				color = self.colorran
				if self.grid[row][column] == 1 :
					if (self.colorran3 > 205):
						color = (self.colorran1, self.colorran2, self.colorran3-50+self.score)
					else :
						color = (self.colorran1, self.colorran2, self.colorran3+50-self.score)
			
				pygame.draw.rect(surface,
            					color,
            					[(self.sizemargin[level] + self.sizegrid[level])*column + self.sizemargin[level],
            					(self.sizemargin[level] + self.sizegrid[level])*row + self.sizemargin[level],
            					self.sizegrid[level],self.sizegrid[level]])
			


