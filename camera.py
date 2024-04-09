import pygame as pg
import math

class Camera:
	def __init__(self, app):
		self.app = app

		self.position = (500, -100)
		self.smoothness = 2

		self.target = self.position


	def check_controls(self):
		keys = pg.key.get_pressed()

		x, y = self.target

		speed = 256*self.app.dt

		vel = [0, 0]

		if keys[pg.K_w]:
			vel[1] -= 1

		if keys[pg.K_s]:
			vel[1] += 1

		if keys[pg.K_a]:
			vel[0] -= 1

		if keys[pg.K_d]:
			vel[0] += 1
		
		vx, vy = vel

		mod = math.sqrt(vx**2 + vy**2)/speed

		if mod == 0:
			return

		vx = vx / mod
		vy = vy / mod

		self.target = x + vx, y + vy



	def update(self):
		self.check_controls()		

		# Target position
		tx, ty = self.target
		# Camera position
		cx, cy = self.position

		# Calculate the smooth step
		cx += (tx-cx)*(10/self.smoothness)*self.app.dt
		cy += (ty-cy)*(10/self.smoothness)*self.app.dt

		# Update the camera position
		self.position = (cx, cy)



