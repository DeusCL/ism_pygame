import pygame as pg
from settings import *


class Block:
	def __init__(self, scene, pos, outline_state=0, occs=None):
		self.scene = scene
		self.camera = scene.camera

		self.position = pos

		self.set_outline(outline_state)
		self.apply_occs(occs)


	def set_outline(self, state):
		outline_states = self.scene.outline_textures
		self.block_img = outline_states[state].copy()


	def apply_occs(self, occs):
		if occs is None:
			return

		for occ in occs:
			self.block_img.blit(self.scene.occlusion_textures[occ], (0, 0))


	def render(self, surface):
		CW, CH = WIN_RES[0]//2, WIN_RES[1]//2

		x, y, z = self.position

		rx = x*16 + z*16
		ry = x*8 - y*16 - z*8

		cx, cy = self.camera.position

		render_pos = CW + rx - cx, CH + ry - cy

		w, h = self.block_img.get_size()

		if render_pos[0] > WIN_RES[0] or render_pos[0] + w < 0:
			return

		if render_pos[1] > WIN_RES[1] or render_pos[1] + h < 0:
			return

		surface.blit(self.block_img, render_pos)



