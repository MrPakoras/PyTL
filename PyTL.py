# Python Tier List
# > Allows users to create Tier Lists
# > Rename/Recolour tiers
# > Save file (can be imported to be updated)
# > Image can be exported

# // Integer division is much faster than math.floor() apparently
# https://stackoverflow.com/questions/40777772/python-integer-division-operator-vs-math-floor

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
imgfiles = 0

rootdir = './images/'
for dirName, subdirList, fileList in os.walk(rootdir):
	for fname in fileList:
		if fname.endswith('.webp'):
			wp = rootdir+fname
			n = rootdir+fname.replace('.webp','.jpg')
			os.rename(wp,n) # Replaces file with renamed file
			print('>> Renamed'+wp+' to '+n)
			nth += 1
			imgfiles += 1 # Number of images to import
		elif fname.endswith('.jpg'):
			imgfiles += 1

		else:
			pass
print('\n>> '+str(nth)+' files renamed.')
print('>> Number of Images:   '+str(imgfiles)+'\n\n')
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
		else:
			pass

		self.name = name # Pygame textbox input field to enter name
		self.colour = colour # RGB tuple to select colour


		self.rankbox = pg.Surface((100, 200)) # Surface for tier ranks
		self.rankbox.fill(colour)

		font = pg.font.Font('freesansbold.ttf', 32)
		self.text = font.render(name, True, (0,0,0)) # Text layer

		colour2 = []
		[colour2.append((2*x)//10) for x in colour]# Reduce each element in colour tuple by half
		colour2 = tuple(colour2) # Convert list back into tuple

		# colour2 = list(colour)
		# colour2.append(0.1) # Adding alpha channel
		# colour2 = tuple(colour2)

		self.imgbox = pg.Surface((width-400,200)) # Surface for images to be placed in
		self.imgbox.fill(colour2)
	
	# Example Tier when name/colour are specified: tier(None,'Top Tier',(122, 202, 65)) - pass None to n
	# Changing tier attributes: tier(n).colour or tier(n).name


### Class for all the image tiles
class cards: # Gonna call them 'cards' so I dont get confused with all the image variables lol
	def __init__(self, image):
		pass


pickbox = pg.Surface((300, height)) # Surface for images to load into and picked from
pickbox.fill((30, 30, 30))


tlist = [Tier(y) for y in range(6)]


### Game Loop
crashed = False

while not crashed:

	window.fill((0, 0, 0)) # Needs to be drawn above surfaces

	for event in pg.event.get():
		if event.type == pg.QUIT:
			crashed = True

		#print(event)
   
	[window.blit(x.rankbox, (0,0+tlist.index(x)*height//len(tlist))) for x in tlist] # Draws surface at coords (tuple), which is below each previous surface
	# ^^ Draw surface for surface in list of Tiers, at position below previous surface, and adjust height so all frrames fit on window
	#[window.blit(x.text, x.rankbox) for x in tlist] # Text on Tier rank
	[window.blit(x.imgbox, (100,0+tlist.index(x)*height//len(tlist))) for x in tlist]
	# Same as above but for imgboxes

	window.blit(pickbox, (width-300, 0)) # Draws surface for images to be loaded into

	# recno = 0 # Rectangle number (counts rectangles drawn)
	# for loop in range(imgfiles):
	# 	rprop = 
	# 	pg.draw.rect(pickbox,(50,50,50),rprop)

	
	pg.display.update()
	clock.tick(60) # 60fps


pg.quit()
quit()