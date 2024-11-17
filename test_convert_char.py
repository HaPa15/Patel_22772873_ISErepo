import unittest
from convert_maze_char import determine_box_char

class TestMazeConversion(unittest.TestCase):
    def test_basic_horizontal_line(self):
        ascii_maze = ['+-+-+-+-+-+-+-+-+', '|               |', '+ + +-+-+-+-+ + +', '| | |         | |', '+ +-+ +-+ +-+ + +', '| |   |   |     |', '+ +-+ + +-+ +-+ +', '| |   | |   |   |', '+ + +-+ + +-+-+-+', '| | |   | |     |', '+-+-+-+-+-+-+-+-+']
        # Ensure the conversion function returns the correct box-drawing characters for horizontal lines
        expected_output = "┌"
        self.assertEqual(determine_box_char(ascii_maze, 0, 0, 17, 11), expected_output)

if __name__ == '__main__':
    unittest.main()
