import pygame
from tiles import Tile
from settings import Settings

settings = Settings()
class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = -0 # how much the world has move to the left

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'X':
                    x = col_index * settings.tile_size
                    y = row_index * settings.tile_size
                    tile = Tile((x,y), settings.tile_size)
                    self.tiles.add(tile)


    def run(self):
        self.tiles.update(self.world_shift) 
        self.tiles.draw(self.display_surface)