import convert_maze_char

def convert_maze(maze):
    """Convert an ASCII maze to a box-drawing maze."""
    height = len(maze)
    width = len(maze[0])
    box_maze = []

    for y in range(height):
        box_row = []
        for x in range(width):
            if maze[y][x] == '+':
                box_char = convert_maze_char.determine_box_char(maze, x, y, width, height)
                box_row.append(box_char)
            elif maze[y][x] == '|':
                box_row.append('│')
            elif maze[y][x] == '-':
                box_row.append('─')
            else:
                box_row.append(maze[y][x])  # Keep spaces and other characters as-is
        box_maze.append("".join(box_row))

    return "\n".join(box_maze)

# Example usage with the initial ASCII maze
ascii_maze = [
    "+-+-+-+-+-+-+-+-+",
    "|               |",
    "+ + +-+-+-+-+ + +",
    "| | |         | |",
    "+ +-+ +-+ +-+ + +",
    "| |   |   |     |",
    "+ +-+ + +-+ +-+ +",
    "| |   | |   |   |",
    "+ + +-+ + +-+-+-+",
    "| | |   | |     |",
    "+-+-+-+-+-+-+-+-+"
]

print(convert_maze(ascii_maze))
