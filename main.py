def convert_maze(maze):
    # Define the maze with box-drawing characters
    box_maze = []
    height = len(maze)
    width = len(maze[0])

    for y in range(height):
        box_row = []
        for x in range(width):
            if maze[y][x] == '+':
                # Determine connections in all four directions
                top = y > 0 and maze[y - 1][x] in ('|', '+')
                bottom = y < height - 1 and maze[y + 1][x] in ('|', '+')
                left = x > 0 and maze[y][x - 1] in ('-', '+')
                right = x < width - 1 and maze[y][x + 1] in ('-', '+')

                # Determine the box-drawing character based on connections
                if top and bottom and left and right:
                    box_char = '┼'
                elif top and bottom and right:
                    box_char = '├'
                elif top and bottom and left:
                    box_char = '┤'
                elif left and right and bottom:
                    box_char = '┬'
                elif left and right and top:
                    box_char = '┴'
                elif left and right:
                    box_char = '─'
                elif top and bottom:
                    box_char = '│'
                elif bottom and right:
                    box_char = '┌'
                elif bottom and left:
                    box_char = '┐'
                elif top and right:
                    box_char = '└'
                elif top and left:
                    box_char = '┘'
                else:
                    box_char = ' '

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

# Convert and display the maze
print(convert_maze(ascii_maze))
