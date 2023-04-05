import pygame
import math
from queue import PriorityQueue

screenWidth = 800
screenWindow = pygame.display.set_mode((screenWidth, screenWidth))

colorRed = (255, 0, 0)
colorGreen = (0, 255, 0)
colorBlue = (0, 255, 0)
colorYellow = (255, 255, 0)
colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)
colorPurple = (128, 0, 128)
colorOrange = (255, 165 ,0)
colorGrey = (128, 128, 128)


class Spot:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = colorWhite
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == colorRed

	def is_open(self):
		return self.color == colorGreen

	def is_barrier(self):
		return self.color == colorBlack

	def is_start(self):
		return self.color == colorOrange

	def is_end(self):
		return self.color == colorBlue

	def reset(self):
		self.color = colorWhite

	def make_start(self):
		self.color = colorOrange

	def make_closed(self):
		self.color = colorRed

	def make_open(self):
		self.color = colorGreen

	def make_barrier(self):
		self.color = colorBlack

	def make_end(self):
		self.color = colorBlue

	def make_path(self):
		self.color = colorPurple

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])
		

			
def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid

def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, colorGrey, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, colorGrey, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	win.fill(colorWhite)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()
	
def heuristic(a, b):
	x1, y1 = a
	x2, y2 = b
	
	d = abs(x1 - x2) + abs(y1 - y2)
	return d


	
def main():
	totalRows = 50
	openSet = []
	closedSet = []

	start = None
	end = None 
	return 
	
	


	


