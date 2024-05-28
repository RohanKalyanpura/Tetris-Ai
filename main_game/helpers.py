def convert_shape_format(piece):
    positions = []
    format = piece.shape[piece.rotation % len(piece.shape)]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((piece.x + j, piece.y + i))
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions

def valid_space(piece, grid):
    accepted_positions = [[(x, y) for x in range(10) if grid[y][x] == (0, 0, 0)] for y in range(20)]
    accepted_positions = [x for sub in accepted_positions for x in sub]
    formatted = convert_shape_format(piece)
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def remove_piece_from_grid(grid, piece):
    grid_copy = [row[:] for row in grid]  # Make a copy of the grid
    piece_positions = convert_shape_format(piece)
    for pos in piece_positions:
        x, y = pos
        if y > -1:
            grid_copy[y][x] = (0, 0, 0)  # Set these positions to black
    return grid_copy

def instant_drop(piece, grid):
    while valid_space(piece, grid):
        piece.y += 1
    piece.y -= 1
