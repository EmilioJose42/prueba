import unittest
from unittest.mock import patch, Mock
from laberinto import Maze, Room # type: ignore
from LivingBeings import Player, LazyBug, AggressiveBug # type: ignore

# Assuming you have the following classes:
# Room, Maze, Character, LazyBug, AggressiveBug

class MazeTestCase(unittest.TestCase):
    def setUp(self):
        # Create a maze with 4 rooms
        self.room1 = Room()
        self.room2 = Room()
        self.room3 = Room()
        self.room4 = Room()
        self.maze = Maze([self.room1, self.room2, self.room3, self.room4])

        # Create a character
        self.character = Player()

        # Create a lazy bug and an aggressive bug
        self.lazy_bug = LazyBug()
        self.aggressive_bug = AggressiveBug()

        # Add the character and bugs to the maze
        self.maze.add_character(self.character)
        self.maze.add_bug(self.lazy_bug)
        self.maze.add_bug(self.aggressive_bug)

    def test_character_movement(self):
        # Test character movement between rooms
        with patch.object(self.character, 'move', wraps=self.character.move) as mock_move:
            self.character.move(self.room1, self.room2)
            mock_move.assert_called_once()
            self.assertEqual(self.character.current_room, self.room2)

    def test_lazy_bug_behavior(self):
        # Test lazy bug behavior
        with patch('builtins.print') as mock_print:
            self.lazy_bug.perform_actions()
            expected_output = [
                "The lazy bug is slowly walking.",
                "The lazy bug is not interested in attacking.",
                "The lazy bug is sleeping."
            ]
            mock_print.assert_has_calls([unittest.mock.call(output) for output in expected_output])

    def test_aggressive_bug_behavior(self):
        # Test aggressive bug behavior
        with patch('builtins.print') as mock_print:
            self.aggressive_bug.perform_actions()
            expected_output = [
                "The aggressive bug is quickly walking.",
                "The aggressive bug is attacking!",
                "The aggressive bug is not sleeping."
            ]
            mock_print.assert_has_calls([unittest.mock.call(output) for output in expected_output])

    def test_character_bug_interaction(self):
        # Test character and bug interaction
        self.character.current_room = self.room1
        self.lazy_bug.current_room = self.room1
        self.aggressive_bug.current_room = self.room1

        with patch('builtins.print') as mock_print:
            self.character.interact_with_bugs()
            expected_output = [
                "The lazy bug is slowly walking.",
                "The lazy bug is not interested in attacking.",
                "The aggressive bug is quickly walking.",
                "The aggressive bug is attacking!"
            ]
            mock_print.assert_has_calls([unittest.mock.call(output) for output in expected_output])

if __name__ == '__main__':
    unittest.main()
