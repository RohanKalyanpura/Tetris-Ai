import pygame
from constants import BLOCK_SIZE, TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT
from helpers import convert_shape_format, remove_piece_from_grid, valid_space
from piece import Piece

def draw_text_middle(text, size, color, surface):
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    label = font.render(text, 1, color)
    surface.blit(label, (TOP_LEFT_X + PLAY_WIDTH / 2 - (label.get_width() / 2), TOP_LEFT_Y + PLAY_HEIGHT / 2 - (label.get_height() / 2)))

def draw_grid(surface, grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, grid[y][x], (TOP_LEFT_X + x * BLOCK_SIZE, TOP_LEFT_Y + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (TOP_LEFT_X, TOP_LEFT_Y + i * BLOCK_SIZE), (TOP_LEFT_X + PLAY_WIDTH, TOP_LEFT_Y + i * BLOCK_SIZE))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (TOP_LEFT_X + j * BLOCK_SIZE, TOP_LEFT_Y), (TOP_LEFT_X + j * BLOCK_SIZE, TOP_LEFT_Y + PLAY_HEIGHT))

def draw_next_shape(shape, surface):
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    label = font.render('Next Shape', 1, (255, 255, 255))
    start_x = TOP_LEFT_X + PLAY_WIDTH + 50
    start_y = TOP_LEFT_Y + (PLAY_HEIGHT / 2 - 100)
    format = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (start_x + j * BLOCK_SIZE, start_y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    surface.blit(label, (start_x + 10, start_y - 30))

def draw_held_shape(shape, surface):
    if shape:
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        label = font.render('Held Shape', 1, (255, 255, 255))
        start_x = TOP_LEFT_X - 150
        start_y = TOP_LEFT_Y + (PLAY_HEIGHT / 2 - 100)
        format = shape.shape[shape.rotation % len(shape.shape)]
        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, shape.color, (start_x + j * BLOCK_SIZE, start_y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
        surface.blit(label, (start_x + 10, start_y - 30))

def draw_window(surface, grid, score=0):
    surface.fill((0, 0, 0))
    font = pygame.font.Font(pygame.font.get_default_font(), 40)
    label = font.render('Tetris', 1, (255, 255, 255))
    surface.blit(label, (TOP_LEFT_X + PLAY_WIDTH / 2 - (label.get_width() / 2), 30))
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    label = font.render('Score: ' + str(score), 1, (255, 255, 255))
    surface.blit(label, (TOP_LEFT_X + PLAY_WIDTH + 50, TOP_LEFT_Y + PLAY_HEIGHT / 2 - 200))
    draw_grid(surface, grid)
    pygame.draw.rect(surface, (255, 0, 0), (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 5)

def draw_shadow(piece, grid, surface):
    shadow_piece = Piece(piece.x, piece.y, piece.shape)
    shadow_piece.rotation = piece.rotation
    grid_without_piece = remove_piece_from_grid(grid, piece)
    while valid_space(shadow_piece, grid_without_piece):
        shadow_piece.y += 1
    shadow_piece.y -= 1
    shape_pos = convert_shape_format(shadow_piece)
    shadow_color = (128, 128, 128)
    for pos in shape_pos:
        x, y = pos
        if y > -1:
            pygame.draw.rect(surface, shadow_color, (TOP_LEFT_X + x * BLOCK_SIZE, TOP_LEFT_Y + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), piece.y)
