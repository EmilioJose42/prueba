from abc import ABC, abstractmethod

class LivingBeing(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    @abstractmethod
    def notify(self, sender, event):
        pass

class ConcreteMediator(LivingBeing):
    """
    Concrete Mediators implement cooperative behavior by coordinating several
    components.
    """

    def __init__(self):
        self._lazy_bugs = []
        self._aggressive_bugs = []
        self._player = None

    def notify(self, sender, event):
        if event == "lazy":
            self._lazy_bugs.append(sender)
            print(f"{sender} is lazy.")
        elif event == "aggressive":
            self._aggressive_bugs.append(sender)
            print(f"{sender} is aggressive.")
        elif event == "player_move":
            print("Player is moving.")
            self._handle_player_move()
        elif event == "attack":
            self._handle_attack(sender)

    def _handle_player_move(self):
        for bug in self._lazy_bugs:
            print(f"{bug} is ignoring the player.")
        for bug in self._aggressive_bugs:
            print(f"{bug} is attacking the player!")

    def _handle_attack(self, attacker):
        if isinstance(attacker, Bug):
            print(f"{attacker} is attacking the player with power {attacker.power}.")
            # Handle player's health reduction
        elif isinstance(attacker, Player):
            for bug in self._aggressive_bugs:
                print(f"{attacker} is attacking {bug} with power {attacker.power}.")
                # Handle bug's health reduction

class Bug:
    """
    The Concrete Components implement various functionalities, but their
    mutual interaction is delegated to the mediator.
    """

    def __init__(self, mediator, name, behavior, power):
        self._mediator = mediator
        self._name = name
        self._behavior = behavior
        self.power = power

    def act(self):
        self._mediator.notify(self, self._behavior)

    def attack(self):
        self._mediator.notify(self, "attack")

class Player:
    """
    Another Concrete Component.
    """

    def __init__(self, mediator, power):
        self._mediator = mediator
        self.power = power

    def move(self):
        self._mediator.notify(self, "player_move")

    def attack(self):
        self._mediator.notify(self, "attack")

# Usage
mediator = ConcreteMediator()

bug1 = Bug(mediator, "Bug 1", "lazy", 10)
bug2 = Bug(mediator, "Bug 2", "aggressive", 15)
player = Player(mediator, 20)

bug1.act()
bug2.act()
player.move()

bug2.attack()
player.attack()
from abc import ABC, abstractmethod

class Bug(ABC):
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (possibly) abstract primitive
    operations.
    """

    def perform_actions(self):
        self.walk()
        self.attack()
        self.sleep()

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class LazyBug(Bug):
    """
    Concrete class implementing the primitive operations for a lazy bug.
    """

    def walk(self):
        print("The lazy bug is slowly walking.")

    def attack(self):
        print("The lazy bug is not interested in attacking.")

    def sleep(self):
        print("The lazy bug is sleeping.")


class AggressiveBug(Bug):
    """
    Concrete class implementing the primitive operations for an aggressive bug.
    """

    def walk(self):
        print("The aggressive bug is quickly walking.")

    def attack(self):
        print("The aggressive bug is attacking!")

    def sleep(self):
        print("The aggressive bug is not sleeping.")


# Usage
lazy_bug = LazyBug()
lazy_bug.perform_actions()
print()

aggressive_bug = AggressiveBug()
aggressive_bug.perform_actions()
