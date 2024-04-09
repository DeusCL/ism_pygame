import pygame as pg
from settings import *

from camera import Camera

import terrain_generator as tgen


class Scene:
	def __init__(self, app):
		self.app = app

		self.outline_textures = self.load_block_textures()
		self.occlusion_textures = self.load_occlusion_textures()

		self.camera = Camera(app)

		self.on_init()


	def on_init(self):
		# Generate the noise map
		noise_map = tgen.gen_noise_map(SEED)

		# Place blocks and get the list of the blocks placed
		self.terrain = tgen.place_blocks(self, noise_map)


	def load_block_textures(self):
		""" Loads the outline texture states of the block """

		imgs = [
			"block.png",
			"block_empty_left.png",
			"block_empty_right.png",
			"block_empty_leftright.png"
		]

		texs = list()

		for img in imgs:
			texs.append(
				pg.image.load(ASSETS_DIR / img).convert_alpha()
			)

		return texs


	def load_occlusion_textures(self):
		""" Loads the ambient occlusion images """

		# I didn't know how to name all these occlusion cases

		occ0 = pg.image.load(ASSETS_DIR / "occ_1.png").convert_alpha()
		occ1 = pg.transform.flip(occ0, True, False)

		occ2 = pg.image.load(ASSETS_DIR / "occ_topright_border.png").convert_alpha()
		occ3 = pg.transform.flip(occ2, True, False)

		occ4 = pg.image.load(ASSETS_DIR / "occ_face_right.png").convert_alpha()
		occ5 = pg.transform.flip(occ4, True, False)

		occ6 = pg.image.load(ASSETS_DIR / "occ_right_corner.png").convert_alpha()
		occ7 = pg.transform.flip(occ6, True, False)

		occ8 = pg.image.load(ASSETS_DIR / "occ_top_corner.png").convert_alpha()

		occ9 = pg.image.load(ASSETS_DIR / "occ_botright_border.png").convert_alpha()
		occ10 = pg.transform.flip(occ9, True, False)

		return [occ0, occ1, occ2, occ3, occ4, occ5, occ6, occ7, occ8, occ9, occ10]


	def update(self):
		self.camera.update()


	def render(self, surface):
		for block in self.terrain:
			block.render(surface)

