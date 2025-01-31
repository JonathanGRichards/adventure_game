from room import Room
from character import Enemy, Friend
from item import Item
import time
# Set player mortality status
dead = False
# Create an item 'sword'
sword = Item("sword", "A sharp and shiny sword")
# Create an item 'hug'
hug = Item("hug", "A Warm and comforting hug")
# Create an item 'key'
key = Item("key", "A golden key with a skeleton on it")

# Set player inventory
inventory = [hug]

# Create rooms for the setting
kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"
ballroom = Room("ballroom")
ballroom.description = "A vast room with a shiny wooden floor"
dining_hall = Room("dining room")
dining_hall.description = "A large room with ornate golden decorations"
treasure_room = Room("treasure room")
treasure_room.description = "A room filled with treasures beyond your wildest dreams"
treasure_room.locked = True  # Lock the treasure room

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")
dining_hall.link_room(treasure_room, "east")


# Add inhabitants to rooms

# Create a zombie character
dave = Enemy("Dave", "A smelly zombie")
dining_hall.set_character(dave)
dave.conversation = "Hi my name is Dave, Id like to eat your brain."
dave.weakness= "sword"
# Assign the item to the zombie
dave.inventory = key

# Create a butler character
butler = Friend("Jeeves", "A helpful butler")
ballroom.set_character(butler)
butler.strength = "hug"
butler.conversation = "I'm sad, lonely and weak. There is only one thing that will give me strength and console me."
# Assign the item to the butler
butler.inventory = sword

# Check if an item name is in the inventory
def is_item_in_inventory(item_name):
    return any(item.name == item_name for item in inventory)

#Set Starter room
current_room = kitchen

#Welcome script
time.sleep(1)
username = input("What is your character name? ")
print(f"Welcome to adventure {username}")
time.sleep(1)
print(f"You find yourself in the {current_room.name} of a strange house. Your goal is to find what treasures you can! ")
time.sleep(4)
print("You can type north, east, south or west to move around the rooms of house")
time.sleep(4)
print("If you run into a character you can talk to them, console them, or fight them")
time.sleep(4)
print("Type 'check inventory' to see what useful items you may have")
time.sleep(4)
print(f"Good luck {username}")
time.sleep(1)

#Gamplay loop
while not dead:
      print("\n")
      current_room.get_details()
      if current_room == treasure_room:
            print("And then a skeleton popped out")
            break
      inhabitant = current_room.get_character()
      if inhabitant is not None:
            inhabitant.describe()
      command = input("> ")
      # Check whether a direction was typed
      if command in ["north", "south", "east", "west"]:
            #Check if next rooms is locked
            next_room = current_room.move(command)
            if next_room.locked:
                  print("The door is locked. You need a key to unlock it.")
                  if is_item_in_inventory("key"):
                        print("You use the key to unlock the door.")
                        next_room.unlock()
                        current_room = next_room
                  else:
                        print("You don't have the key.")
            else:
                  current_room = next_room
      elif command == "talk":
            if inhabitant is not None:
                  inhabitant.talk()
            else:
                  print("There is no one here to talk to")
      elif command == "fight":
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                  # Fight with the inhabitant, if there is one
                  print("What will you fight with?")
                  fight_with = input("\n> ")
                  if inhabitant.fight(fight_with) == True and is_item_in_inventory(fight_with):
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        # Add the enemy's inventory item to the player's inventory
                        inventory.append(inhabitant.inventory)
                        print(f"{inhabitant.name} dropped a {inhabitant.inventory.name}!")
                        #Clear the ememy from the room
                        current_room.set_character(None)
                  else:
                        # What happens if you lose?
                        if fight_with == 'sword':
                              print('No sword in inventory')
                        print("Oh dear, you lost the fight.")
                        dead = True
            elif inhabitant is not None and isinstance(inhabitant, Friend):
                   inhabitant.fight(fight_with = '')
            else:
                    print("There is no one here to fight with")
      elif command == "console":
            if inhabitant is not None and isinstance(inhabitant, Friend):
                  # Ask the player what they want to console with
                  print("What will you console with?")
                  console_with = input("\n> ")
                  # Check if the console action is successful and the item is in the inventory
                  if inhabitant.console(console_with) == True and is_item_in_inventory(console_with):
                        # Successful console action
                        print("You have consoled the friend!")
                        # Add the friend's inventory item to the player's inventory
                        inventory.append(inhabitant.inventory)
                        print(f"[{inhabitant.name} says]: You gave me strength! Take this item, it may come in handy! ")
                        print(f"You received a {inhabitant.inventory.name}")
                        # Clear the friend's inventory
                        inhabitant.inventory = None
                  else:
                        # Unsuccessful console action
                        print("That didn't work.")
            else:
                        # No one to console
                        print("There is no one here to console")
      elif command == "check inventory":
        if inventory:
            print("You have the following items in your inventory:")
            for item in inventory:
                print(f"- {item.name}: {item.description}")
        else:
            print("Your inventory is empty.")

# Game over message
if dead == True:
      print(f"GAME OVER {username}- YOU DIED - YOU LOSE")
else:
      print(f"WELL DONE {username} YOU COMPLETED THE GAME - YOU WIN")
