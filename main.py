import pygame as pg
import sys
from settings import *
from scene import Scene


class App:
	def __init__(self):
		self.win = pg.display.set_mode(WIN_RES)

		self.clock = pg.time.Clock()
		self.time = 0
		self.dt = 1/TARGET_FPS

		self.scene = Scene(self)


	def render(self):
		self.win.fill(BG_COLOR)
		self.scene.render(self.win)
		pg.display.flip()


	def handle_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					pg.quit()
					sys.exit()


	def get_time(self):
		self.time = pg.time.get_ticks()*0.001


	def update(self):
		self.scene.update()


	def run(self):
		while True:
			self.get_time()
			self.handle_events()
			self.update()
			self.render()
			self.dt = self.clock.tick(TARGET_FPS)*0.001
			pg.display.set_caption(f"{self.clock.get_fps():0.2f}")



if __name__ == '__main__':
	app = App()
	app.run()



