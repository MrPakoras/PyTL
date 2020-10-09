# Python Tier List
# > Allows users to create Tier Lists
# > Rename/Recolour tiers
# > Save file (can be imported to be updated)
# > Image can be exported

import pygame as pg
import os, math

pg.init()
width, height = 840, 960
window = pg.display.set_mode((width, height))
#window = pg.display.set_mode(size, pg.RESIZEABLE)
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

global tiers
tiers = 0

# Class for each row of a tier
class Tier():
	def __init__(self, n, name=None, colour=None): # Arg=something - Default parameter for argument
		global tiers
		tiers += 1 # Is there a way of counting the number of objects created?
		self.n = n

		if name is None: # If parameter is None, then set default value
			name = defranks[n]
		if colour is None:
			colour = defcols[n]

		self.name = name # Pygame textbox input field to enter name
		self.colour = colour # RGB tuple to select colour

		self.rankbox = pg.Surface((100, 200)) # Surface for tier ranks
		self.rankbox.fill(colour)

		font = pg.font.Font('freesansbold.ttf', 32)
		self.text = font.render(name, True, (0,0,0)) # Text layer

		colour2 = []
		[colour2.append(math.floor(x*0.2)) for x in colour]# Reduce each element in colour tuple by half
		colour2 = tuple(colour2) # Convert list back into tuple

		self.imgbox = pg.Surface((width-400,200)) # Surface for images to be placed in
		self.imgbox.fill(colour2)
	
	# Example Tier when name/colour are specified: tier(None,'Top Tier',(122, 202, 65)) - pass None to n
	# Changing tier attributes: tier(n).colour or tier(n).name

pickbox = pg.Surface((300, height)) # Surface for images to load into and picked from
pickbox.fill((30, 30, 30))

tlist = [Tier(0), Tier(1), Tier(2), Tier(3), Tier(4), Tier(5)]
#print(t.colour)

# Game
crashed = False

while not crashed:

	window.fill((255, 255, 255)) # Needs to be drawn above surfaces

	for event in pg.event.get():
		if event.type == pg.QUIT:
			crashed = True

		#print(event)
   
	[window.blit(x.rankbox, (0,0+tlist.index(x)*math.floor(height/len(tlist)))) for x in tlist] # Draws surface at coords (tuple), which is below each previous surface
	# ^^ Draw surface for surface in list of Tiers, at position below previous surface, and adjust height so all frrames fit on window
	#[window.blit(x.text, x.rankbox) for x in tlist] # Text on Tier rank
	[window.blit(x.imgbox, (100,0+tlist.index(x)*math.floor(height/len(tlist)))) for x in tlist]
	# Same as above but for imgboxes

	window.blit(pickbox, (width-300, 0))
	pg.display.update()
	clock.tick(60) # 60fps


pg.quit()
quit()