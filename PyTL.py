# Python Tier List
# > Allows users to create Tier Lists
# > Rename/Recolour tiers
# > Save file (can be imported to be updated)
# > Image can be exported

import pygame as pg
import os

pg.init()

gameDisplay = pg.display.set_mode((540,960))
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


# Game
crashed = False

while not crashed:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			crashed = True

		print(event)
    
    # Class for each row of a tier
	class tier:
		def __init__():
			pass
		def rank(self, n, name, colour): # Left side that has the position/name/colour of tier
			self.name = defranks[n] # Pygame textbox input field to enter name
			self.colour = (defcols[n]) # RGB tuple to select colour
		def imgbox(): # Right side where images are to be placed
			pass


	
	pg.display.update()

	clock.tick(60)


pg.quit()
quit()