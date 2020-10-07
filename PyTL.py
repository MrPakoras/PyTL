# Python Tier List
# > Allows users to create Tier Lists
# > Rename/Recolour tiers
# > Save file (can be imported to be updated)
# > Image can be exported

import pygame as pg
import os

pg.init()

window = pg.display.set_mode((540,960))
pg.display.set_caption('PyTL - Tier List Maker in Python [v0]')
clock = pg.time.Clock()

defcols = [(134, 52, 235),(52, 89, 235),(52, 235, 147),(235, 235, 52),(235, 156, 52),(235, 79, 52)] # Default colours for tiers
defranks = ['S', 'A', 'B', 'C', 'D', 'F'] # Default ranks for tiers

# Converting from .webp from MAL asset download to .jpg
nth = 0
rootdir = './images/'
for dirName, subdirList, fileList in os.walk(rootdir):
	for fname in fileList:
		if fname.endswith('.webp'):
			wp = rootdir+fname
			n = rootdir+fname.replace('.webp','.jpg')
			os.rename(wp,n) # Replaces file with renamed file
			print('>> Renamed'+wp+' to '+n)
			nth += 1
		else:
			pass
print('\n>> '+str(nth)+' files renamed.\n\n')

tiers = 0

# Class for each row of a tier
class Tier():
	def __init__(self, n, name=None, colour=None): # Arg=something - Default parameter for argument
		tiers += 1 # Is there a way of counting the number of objects created?
		self.n = n

		if name is None: # If parameter is None, then set default value
			name = defranks[n]
		if colour is None:
			colour = defcols[n]

		self.name = name # Pygame textbox input field to enter name
		self.colour = colour # RGB tuple to select colour

		self.surf = pg.Surface((100, 200))
		self.surf.fill(colour)
	
	# Example Tier when name/colour are specified: tier(None,'Top Tier',(122, 202, 65)) - pass None to n
	# Changing tier attributes: tier(n).colour or tier(n).name

t = Tier(0)
print(t.colour)

# Game
crashed = False

while not crashed:

	window.fill((255, 255, 255)) # Needs to be drawn above surfaces

	for event in pg.event.get():
		if event.type == pg.QUIT:
			crashed = True

		print(event)
    
	
	
	
	window.blit(t.surf, (0,0)) # Draws surface at coords (tuple)
	pg.display.update()
	clock.tick(60) # 60fps


pg.quit()
quit()