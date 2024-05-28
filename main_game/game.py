import pygame
from piece import Piece
from shadow_piece import ShadowPiece
from grid import create_grid, clear_rows
from helpers import convert_shape_format, valid_space, check_lost, instant_drop
from drawing import draw_text_middle, draw_grid, draw_next_shape, draw_held_shape, draw_window, draw_shadow
from constants import TOP_LEFT_X, PLAY_WIDTH, PLAY_HEIGHT
import random

def get_shape():
    from shapes import shapes
    return Piece(5, 0, random.choice(shapes))

def main_menu(win):
    run = True
    while run:
        win.fill((0, 0, 0))
        draw_text_middle('Press Any Key To Play', 20, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)
    pygame.quit()

def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    hold_piece = None
    hold_used = False
    clock = pygame.time.Clock()
    fall_time = 0
    level_time = 0
    score = 0
    move_left = False
    move_right = False
    move_counter = 0

    while run:
        grid = create_grid(locked_positions)
        fall_speed = 0.27
        side_move_speed = 0.1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
                elif event.key == pygame.K_SPACE:
                    instant_drop(current_piece, grid)
                    change_piece = True
                elif event.key == pygame.K_c:
                    if not hold_used:
                        if hold_piece is None:
                            hold_piece = current_piece
                            current_piece = next_piece
                            next_piece = get_shape()
                        else:
                            current_piece, hold_piece = hold_piece, current_piece
                        hold_piece.x, hold_piece.y = 5, 0
                        hold_piece.rotation = 0
                        hold_used = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False

        move_counter += clock.get_rawtime()
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if move_left and move_counter / 1000 >= side_move_speed:
            current_piece.x -= 1
            if not valid_space(current_piece, grid):
                current_piece.x += 1
            move_counter = 0

        if move_right and move_counter / 1000 >= side_move_speed:
            current_piece.x += 1
            if not valid_space(current_piece, grid):
                current_piece.x -= 1
            move_counter = 0

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            hold_used = False
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_window(win, grid, score)
        draw_shadow(current_piece, grid, win)
        draw_next_shape(next_piece, win)
        draw_held_shape(hold_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False
            draw_text_middle("YOU LOST", 20, (255, 255, 255), win)
            pygame.display.update()
            pygame.time.delay(1500)
