import unittest
from main import convert_maze

class TestMazeConversion(unittest.TestCase):
    def test_basic_horizontal_line(self):
        ascii_maze = ["+-+-+"]
        # Ensure the conversion function returns the correct box-drawing characters for horizontal lines
        expected_output = " ─── "
        self.assertEqual(convert_maze(ascii_maze), expected_output)

    def test_basic_vertical_line(self):
        ascii_maze = ["|", "|", "|"]
        expected_output = '''│
│
│'''
        self.assertEqual(convert_maze(ascii_maze), expected_output)

    def test_corner_intersections(self):
        ascii_maze = ["+ +", "| |", "+-+"]
        # Ensure the function detects the corner intersections properly
        expected_output = '''   
│ │
└─┘'''
        self.assertEqual(convert_maze(ascii_maze), expected_output)

    def test_complex_structure(self):
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
        expected_output = '''┌───────────────┐
│               │
│   ┌───────    │
│ │ │         │ │
│ ├─┘ ┌─  ┌─    │
│ │   │   │     │
│ ├─  │ ┌─┘ ┌─  │
│ │   │ │   │   │
│ │ ┌─┘ │ ┌─┴───┤
│ │ │   │ │     │
└─┴─┴───┴─┴─────┘'''
        # Remove leading spaces and extra newlines in the expected output to match actual output formatting
        self.assertEqual(convert_maze(ascii_maze), expected_output)

if __name__ == '__main__':
    unittest.main()
