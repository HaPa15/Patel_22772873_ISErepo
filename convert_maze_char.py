def determine_box_char(maze, x, y, width, height):
    """Determine the box-drawing character based on connections."""
    top = y > 0 and maze[y - 1][x] in ('|', '+')
    bottom = y < height - 1 and maze[y + 1][x] in ('|', '+')
    left = x > 0 and maze[y][x - 1] in ('-', '+')
    right = x < width - 1 and maze[y][x + 1] in ('-', '+')

    if top and bottom and left and right:
        return '┼'
    elif top and bottom and right:
        return '├'
    elif top and bottom and left:
        return '┤'
    elif left and right and bottom:
        return '┬'
    elif left and right and top:
        return '┴'
    elif left and right:
        return '─'
    elif top and bottom:
        return '│'
    elif bottom and right:
        return '┌'
    elif bottom and left:
        return '┐'
    elif top and right:
        return '└'
    elif top and left:
        return '┘'
    else:
        return ' '  # Handle edge cases where none match

