import json
from abc import ABC, abstractmethod

# Maze Form (from the previous example)
class MazeForm(ABC):
    @abstractmethod
    def draw_cell(self):
        pass

    @abstractmethod
    def get_cell_sides(self):
        pass


class SquareMazeForm(MazeForm):
    def draw_cell(self):
        print("Drawing a square cell.")

    def get_cell_sides(self):
        return 4


class HexagonMazeForm(MazeForm):
    def draw_cell(self):
        print("Drawing a hexagon cell.")

    def get_cell_sides(self):
        return 6


# Maze Builder
class MazeBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts
    of the Maze objects.
    """

    @abstractmethod
    def build_maze(self, maze_data):
        pass

    @abstractmethod
    def get_maze(self):
        pass


class ConcreteMazeBuilder(MazeBuilder):
    """
    The Concrete Builder constructs and assembles parts of the product by
    implementing the Builder interface.
    """

    def __init__(self):
        self.maze = None

    def build_maze(self, maze_data):
        form = maze_data["form"]
        if form == "square":
            self.maze = SquareMaze(SquareMazeForm())
        elif form == "hexagon":
            self.maze = HexagonMaze(HexagonMazeForm())
        else:
            raise ValueError("Invalid maze form specified.")

        self.maze.create_maze()

    def get_maze(self):
        return self.maze


# Maze (from the previous example)
class Maze(ABC):
    def __init__(self, maze_form: MazeForm):
        self._maze_form = maze_form

    @abstractmethod
    def create_maze(self):
        pass


class SquareMaze(Maze):
    def create_maze(self):
        print("Creating a square maze.")
        self._maze_form.draw_cell()
        print(f"Each cell has {self._maze_form.get_cell_sides()} sides.")


class HexagonMaze(Maze):
    def create_maze(self):
        print("Creating a hexagon maze.")
        self._maze_form.draw_cell()
        print(f"Each cell has {self._maze_form.get_cell_sides()} sides.")


# Director
class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence.
    """

    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    def construct(self, maze_data):
        if self._builder is None:
            raise ValueError("Builder not set.")

        self._builder.build_maze(maze_data)
        return self._builder.get_maze()


# Usage
with open("maze_data.json", "r") as file:
    maze_data = json.load(file)

director = Director()
builder = ConcreteMazeBuilder()
director.set_builder(builder)

maze = director.construct(maze_data)
