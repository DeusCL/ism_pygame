from noise import noise2
from settings import *
import numpy as np

from block import Block


def gen_noise_map(seed, shape=(256, 256), res=(8, 8)):
	np.random.seed(seed)
	return noise2(shape, res)


def get_height(noise, x, z):
	height = (noise[x, z] + 1)/2
	return int(height*HEIGHT_MULTIPLIER)


def is_empty(noise, x, y, z):
	if x >= WORLD_W or z >= WORLD_D:
		return True

	if x < 0 or z < 0:
		return True

	h = get_height(noise, x, z)

	if h != y:
		return True

	return False


def sth(noise, x, y, z):
	""" The opposite of is_empty, (something) """
	return not is_empty(noise, x, y, z)


def get_block_state(noise, x, y, z):
	""" Returns the state that the block in the given coords should have """

	outline_state = 0 # Indicates that this block shouldn't have any outlines

	empty_left = is_empty(noise, x-1, y, z)
	empty_right = is_empty(noise, x, y, z+1)

	if empty_left and not empty_right:
		outline_state = 1 # Should have top-left outline

	if empty_right and not empty_left:
		outline_state = 2 # Should have top-right outline

	if empty_left and empty_right:
		outline_state = 3 # Should have both outlines

	occs = get_occlusions(noise, x, y, z)

	return outline_state, occs


def get_occlusions(noise, x, y, z):
	""" Returns the occlusions that this block should have
	evaluating the neighbors """

	occs = list()

	if sth(noise, x, y+1, z+1):
		occs.append(2)

	if sth(noise, x-1, y+1, z):
		occs.append(3)

	if sth(noise, x-1, y+1, z+1):
		if is_empty(noise, x, y+1, z+1) and is_empty(noise, x-1, y+1, z):
			occs.append(8)

	if sth(noise, x+1, y+1, z+1):
		if is_empty(noise, x+1, y+1, z) and is_empty(noise, x, y+1, z+1):
			occs.append(6)

	if sth(noise, x-1, y+1, z-1):
		if is_empty(noise, x-1, y+1, z) and is_empty(noise, x, y+1, z-1):
			occs.append(7)

	if sth(noise, x+1, y+1, z):
		occs.append(9)

	if sth(noise, x, y+1, z-1):
		occs.append(10)

	if sth(noise, x+1, y, z+1):
		occs.append(4)

	if sth(noise, x-1, y, z-1):
		occs.append(5)

	if sth(noise, x, y-1, z-1):
		occs.append(0)

	if sth(noise, x+1, y-1, z):
		occs.append(1)

	return occs


def place_blocks(scene, noise_map):
	block_list = list()

	for xw in range(WORLD_W):
		x = xw

		for zw in range(WORLD_D):
			z = (WORLD_D-1)-zw

			height = get_height(noise_map, x, z)

			outline_state, occs = get_block_state(noise_map, x, height, z)

			block_list.append(
				Block(scene, (x, height, z), outline_state, occs)
			)

	return block_list


