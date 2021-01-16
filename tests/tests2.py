import pygame as pg

pg.init()

window = pg.display.set_mode((540,960))
pg.display.set_caption('PyTL - Tier List Maker in Python [v0]')
clock = pg.time.Clock()

defcols = [(134, 52, 235),(52, 89, 235),(52, 235, 147),(235, 235, 52),(235, 156, 52),(235, 79, 52)] # Default colours for tiers

class tier:
	def __init__(self, n, colour=None):

		if colour is None:
			colour = defcols[n]

		self.surf = pg.Surface((100, 200))
		self.surf.fill(colour)

t = tier(2)

crashed = False

while not crashed:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			crashed = True

		print(event)



	window.fill((255, 255, 255))
	window.blit(t.surf, (0,0))
	pg.display.update()
	clock.tick(60) # 60fps


pg.quit()