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
game.maze.entrar() 