import pygame as pg

pg.init()

window = pg.display.set_mode((540,960))
pg.display.set_caption('PyTL - Tier List Maker in Python [v0]')
clock = pg.time.Clock()


surf = pg.Surface([100, 200])
surf.fill((120,203,65))


crashed = False

while not crashed:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			crashed = True

		print(event)



	window.fill((255, 255, 255))
	window.blit(surf, (0,0))
	pg.display.update()
	clock.tick(60) # 60fps


pg.quit()