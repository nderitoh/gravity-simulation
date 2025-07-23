import math
import pygame
import os  # ✅ Always at the top

FPS = 120
WIDTH = 800
HEIGHT = 600

G = 5
SHIP_SIZE = 5
PLANET_SIZE = 50
SHIP_MASS = 5
PLANET_MASS = 100
VEL_SCALE = 100
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (122, 122, 122)
WHITE = (255, 255, 255)

import os  # Make sure this is at the top of util.py

BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "background.jpg")),
    (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(
    pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "jupiter.png")),
    (PLANET_SIZE * 2, PLANET_SIZE * 2))
