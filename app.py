import pygame
from random import choice

# Constants
RES = WIDTH, HEIGHT = 1200, 900
TILE = 50
cols, rows = WIDTH // TILE, HEIGHT // TILE

# Initialize Pygame
pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

# Cell class to represent each cell in the maze
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
    
    def draw_current_cell(self):
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(sc, pygame.Color('white'),
                         (x + 2, y + 2, TILE - 2, TILE - 2))
    
    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.visited:
            pygame.draw.rect(sc, pygame.Color('white'),
                             (x, y, TILE, TILE))
        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), 
                             (x, y), (x + TILE, y), 3)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), 
                             (x + TILE, y), 
                             (x + TILE, y + TILE), 3)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), 
                             (x + TILE, y + TILE),
                             (x , y + TILE), 3)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), 
                             (x, y + TILE), (x, y), 3)
    
    def check_cell(self, x, y):
        # Ensure the cell is within bounds and return the cell if valid
        if 0 <= x < cols and 0 <= y < rows:
            return grid_cells[x + y * cols]
        return None
    
    def check_neighbors(self):
        neighbors = []
        # Check for unvisited neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = self.check_cell(self.x + dx, self.y + dy)
            if neighbor and not neighbor.visited:
                neighbors.append(neighbor)
        return choice(neighbors) if neighbors else None   

def remove_walls(current, next):
    # Remove walls between two cells
    dx = current.x - next.x
    dy = current.y - next.y
    if dx == 1:  # current is to the right of next
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:  # current is to the left of next
        current.walls['right'] = False
        next.walls['left'] = False
    if dy == 1:  # current is below next
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:  # current is above next
        current.walls['bottom'] = False
        next.walls['top'] = False 

# Create a grid of cells
grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []
colors, color = [], 40
running = True
paused = False

while running:
    sc.fill(pygame.Color('#a6d5e2'))  # Fill background
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Pause/Resume on spacebar
                paused = not paused
    
    if not paused:
        current_cell.visited = True
        current_cell.draw_current_cell()
        [cell.draw() for cell in grid_cells]  # Draw all cells
        [pygame.draw.rect(sc, colors[i], 
                          (cell.x * TILE + 2, cell.y * TILE + 2,
                           TILE - 4, TILE - 4), border_radius=8) for i, cell in enumerate(stack)] 
        
        next_cell = current_cell.check_neighbors()
        if next_cell:
            next_cell.visited = True
            stack.append(current_cell)
            colors.append((min(color, 255), 0, 103))
            color += 1
            remove_walls(current_cell, next_cell)
            current_cell = next_cell
        elif stack: 
            current_cell = stack.pop()
        else:
            # Maze generation complete notification
            font = pygame.font.SysFont(None, 48)
            # text = font.render('Maze Generation Complete!', True, pygame.Color('black'))
            # sc.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(30)  

pygame.quit()
