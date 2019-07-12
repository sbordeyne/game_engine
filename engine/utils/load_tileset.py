import pygame


def load_tileset(img_path, tile_size):
    """
        Loads a tileset into pygame.Surface objects.

        Returns a list of pygame.Surface objects.

        args :
        * img_path : path of the source image (the tileset)
        * tile_size : a tuple of size 2 describing the size of one tile.

        returns:
        * rv : list of pygame.Surface objects, of size $tile_size
    """
    i = j = 0
    xinc, yinc, *_ = tile_size
    tile_size = (xinc, yinc)
    image = pygame.image.load(img_path)
    xmax, ymax = image.get_size()
    rv = []
    while i < xmax:
        while j < ymax:
            surf = pygame.Surface(tile_size)
            surf.blit(image, (0, 0), (i, j, i + xinc, j + yinc))
            rv.append(surf)
            j += yinc
        i += xinc
    return rv
