class Game:
    def __init__(self):
        self.maze = None

    def create_wall(self):
        return Wall()
    
    def create_door(self,side1,side2):
        door=Door(side1,side2)
        return door  
    
    def create_room(self, id):
        return Room(id)

    def create_maze(self):
        return Maze()
    
    def make2RoomsMazeFM(self):
        self.maze = self.create_maze()
        room1 = self.create_room(1)
        room2 = self.create_room(2)
        door = self.create_door(room1,room2)
        room1.south=door
        room2.north=door
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)
        return self.maze
    
    def make2RoomsMaze(self):
        self.maze = Maze()
        room1 = Room(1)
        room2 = Room(2)
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)

        door=Door(room1,room2)
        room1.south = door
        room2.north = door
        return self.maze

class BombedGame(Game):
    def create_wall(self):
        return BombedWall()

class MapElement:
    def __init__(self):
        pass
    def entrar(self):
        pass

class Hoja(MapElement):

    def accept(self, visitor):
        visitor.visitHoja(self)

class Decorator(Hoja):
    
    def __init__(self, component):
        self.component = component

class Maze(MapElement):
    def __init__(self):
        self.rooms = []
    
    def addRoom(self, room):
        self.rooms.append(room)
    
    def entrar(self):
        self.rooms[0].entrar()  

class Room(MapElement):
    def __init__(self,id):
        self.north = Wall()
        self.east = Wall()
        self.west = Wall()
        self.south = Wall()
        self.id = id
    
    def entrar(self):
        print("You enter room", self.id)

class Door(MapElement):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.opened = False
    def entrar(self):
        if self.opened:
            self.side2.entrar()
        else:
            print("The door is locked")
    
class Wall(MapElement):
    def __init__(self):
        pass # Walls don't need additional attributes
    def entrar(self):
        print("You can't go through walls")

class BombedWall(Wall):
    def __init__(self):
        self.active = False   
    def entrar(self):
        if self.active:
            print("the bomb has detonated")
        else:
            return super().entrar()


    
game=BombedGame()
game.make2RoomsMazeFM()

# Implementor (Maze Form)
class MazeForm(ABC):
    """
    The Implementor interface declares the operations common to all concrete
    implementations.
    """

    @abstractmethod
    def draw_cell(self):
        pass

    @abstractmethod
    def get_cell_sides(self):
        pass


class SquareMazeForm(MazeForm):
    """
    Concrete Implementor for square-shaped maze cells.
    """

    def draw_cell(self):
        print("Drawing a square cell.")

    def get_cell_sides(self):
        return 4


class HexagonMazeForm(MazeForm):
    """
    Concrete Implementor for hexagon-shaped maze cells.
    """

    def draw_cell(self):
        print("Drawing a hexagon cell.")

    def get_cell_sides(self):
        return 6


# Abstraction (Maze)
class Maze(ABC):
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementor hierarchy and delegates all of the real work to this object.
    """

    def __init__(self, maze_form: MazeForm):
        self._maze_form = maze_form

    @abstractmethod
    def create_maze(self):
        pass

from abc import ABC, abstractmethod

# Maze (Subject)
class Maze(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def enter(self):
        pass


# Real Maze (Real Subject)
class RealMaze(Maze):
    """
    The RealSubject contains some core business logic. Usually, RealSubject
    objects are capable of doing some useful work which may also be very slow
    or sensitive.
    """

    def enter(self):
        print("Entering the maze through the main entrance.")


# Tunnel Proxy (Proxy)
class TunnelProxy(Maze):
    """
    The Proxy has an interface identical to the RealSubject. The proxy
    controls access to the real subject and may be responsible for creating
    and deleting it.
    """

    def __init__(self, real_maze: RealMaze):
        self._real_maze = real_maze

    def enter(self):
        if self._check_access():
            print("Entering the maze through the tunnel.")
            self._real_maze.enter()
        else:
            print("Access denied. The tunnel is closed.")

    def _check_access(self):
        # Here we can implement any access control logic
        # For example, check if the tunnel is open or closed
        is_open = True  # For demonstration purposes
        return is_open


# Client
class Client:
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, we
    can introduce a proxy at the child class level.
    """

    def __init__(self, maze: Maze):
        self._maze = maze

    def enter_maze(self):
        self._maze.enter()


# Usage
real_maze = RealMaze()
tunnel_proxy = TunnelProxy(real_maze)

# Using the main entrance
client = Client(real_maze)
client.enter_maze()

# Using the tunnel proxy
client = Client(tunnel_proxy)
client.enter_maze()

class SquareMaze(Maze):
    """
    Refined Abstraction for square-shaped mazes.
    """

    def create_maze(self):
        print("Creating a square maze.")
        self._maze_form.draw_cell()
        print(f"Each cell has {self._maze_form.get_cell_sides()} sides.")


class HexagonMaze(Maze):
    """
    Refined Abstraction for hexagon-shaped mazes.
    """

    def create_maze(self):
        print("Creating a hexagon maze.")
        self._maze_form.draw_cell()
        print(f"Each cell has {self._maze_form.get_cell_sides()} sides.")


# Usage
square_maze_form = SquareMazeForm()
square_maze = SquareMaze(square_maze_form)
square_maze.create_maze()
print()

hexagon_maze_form = HexagonMazeForm()
hexagon_maze = HexagonMaze(hexagon_maze_form)
hexagon_maze.create_maze()

from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    """
    The Command interface declares an execute method that should be implemented
    by all concrete commands.
    """

    @abstractmethod
    def execute(self):
        pass


# Concrete Commands
class OpenDoorCommand(Command):
    """
    Concrete command for opening a door.
    """

    def __init__(self, door):
        self._door = door

    def execute(self):
        self._door.open()


class CloseDoorCommand(Command):
    """
    Concrete command for closing a door.
    """

    def __init__(self, door):
        self._door = door

    def execute(self):
        self._door.close()


# Receiver (Door)
class Door:
    """
    The Receiver class contains the actual implementation of the operations
    associated with opening and closing the door.
    """

    def open(self):
        print("Opening the door.")

    def close(self):
        print("Closing the door.")


# Invoker (Player)
class Player:
    """
    The Invoker class is responsible for executing commands. It holds a
    reference to a command object and can execute the command by calling its
    execute method.
    """

    def __init__(self):
        self._open_command = None
        self._close_command = None

    def set_open_command(self, command):
        self._open_command = command

    def set_close_command(self, command):
        self._close_command = command

    def open_door(self):
        if self._open_command:
            self._open_command.execute()
        else:
            print("No open command set.")

    def close_door(self):
        if self._close_command:
            self._close_command.execute()
        else:
            print("No close command set.")


# Usage
door = Door()
open_command = OpenDoorCommand(door)
close_command = CloseDoorCommand(door)

player = Player()
player.set_open_command(open_command)
player.set_close_command(close_command)

player.open_door()  # Output: Opening the door.
player.close_door()  # Output: Closing the door.
class Direction:
    """
    The Singleton class defines the `get_instance` method that serves as an
    alternative to the constructor and lets clients get the same instance every
    time.
    """

    class __Direction:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

    _instances = {}

    def __init__(self):
        raise RuntimeError("Cannot instantiate Direction directly.")

    @classmethod
    def get_instance(cls, name):
        """
        Returns the singleton instance of the Direction class with the given
        name.
        """
        if name not in cls._instances:
            cls._instances[name] = cls.__Direction(name)
        return cls._instances[name]


# Usage
north = Direction.get_instance("North")
east = Direction.get_instance("East")
west = Direction.get_instance("West")
south = Direction.get_instance("South")

# Trying to create another instance with the same name
another_north = Direction.get_instance("North")

print(north)  # Output: North
print(east)  # Output: East
print(west)  # Output: West
print(south)  # Output: South

print(north is another_north)  # Output: True
from abc import ABC, abstractmethod

# State Interface
class DoorState(ABC):
    """
    The State interface declares methods that all Concrete State objects should
    implement.
    """

    @abstractmethod
    def open(self, door):
        pass

    @abstractmethod
    def close(self, door):
        pass


# Concrete State Classes
class OpenState(DoorState):
    """
    Concrete State for an open door.
    """

    def open(self, door):
        print("The door is already open.")

    def close(self, door):
        print("Closing the door.")
        door.set_state(ClosedState())


class ClosedState(DoorState):
    """
    Concrete State for a closed door.
    """

    def open(self, door):
        print("Opening the door.")
        door.set_state(OpenState())

    def close(self, door):
        print("The door is already closed.")


# Context (Door)
class Door:
    """
    The Context maintains an instance of a Concrete State subclass that defines
    the current state.
    """

    def __init__(self):
        self._state = ClosedState()

    def set_state(self, state):
        self._state = state

    def open(self):
        self._state.open(self)

    def close(self):
        self._state.close(self)


# Usage
door = Door()

door.open()  # Output: Opening the door.
door.close()  # Output: Closing the door.
door.open()  # Output: Opening the door.
door.open()  # Output: The door is already open.
door.close()  # Output: Closing the door.
door.close()  # Output: The door is already closed.
