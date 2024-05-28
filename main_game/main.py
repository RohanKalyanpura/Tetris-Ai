import pygame
from game import main_menu

# Initialize Pygame
pygame.init()

# Set up the game window
win = pygame.display.set_mode((800, 700))
pygame.display.set_caption('Tetris')

# Start the game
main_menu(win)
