class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}

    def add_connection(self, direction, connected_room):
        self.connections[direction] = connected_room

    def get_description(self):
        return self.description


class Game:
    def __init__(self, player, starting_room):
        self.player = player
        self.current_room = starting_room

    def move(self, direction):
        # Check if the requested direction is a valid connection from the current room
        if direction in self.current_room.connections:
            # Move the player to the connected room in the specified direction
            self.current_room = self.current_room.connections[direction]
            print("You moved to", self.current_room.name)
            print(self.current_room.get_description())
        else:
            # If the direction is not valid, inform the player
            print("You can't go that way!")

    def play(self):
        # Print initial game information
        print("Welcome to the Text Adventure Game!")
        print("You are currently in", self.current_room.name)
        print(self.current_room.get_description())

        while True:
            # Get player input
            command = input("What do you want to do? ").lower()

            if command == "quit":
                # If the player chooses to quit, end the game loop
                print("Thanks for playing!")
                break

            elif command.startswith("go "):
                # If the player wants to move, extract the direction from the command
                direction = command.split()[1]
                # Call the move method with the specified direction
                self.move(direction)

            else:
                # If the command is not recognized, inform the player
                print("I don't understand that command.")


# Create rooms
room1 = Room("Room 1", "You are in a dark room.")
room2 = Room("Room 2", "You are in a bright room.")
room3 = Room("Room 3", "You are in a spooky room.")

# Connect rooms
room1.add_connection("east", room2)
room2.add_connection("west", room1)
room2.add_connection("north", room3)
room3.add_connection("south", room2)

# Create player
player_name = input("Enter your name: ")
player = Player(player_name)

# Create game
game = Game(player, room1)
game.play()
