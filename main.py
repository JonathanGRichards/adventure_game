from room import Room
from character import Enemy
# Set player mortality status
dead = False

# Create rooms for the setting
kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"
ballroom = Room("ballroom")
ballroom.description = "A vast room with a shiny wooden floor"
dining_hall = Room("dining_room")
dining_hall.description = "A large room with ornate golden decorations"

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

# Add inhabitants to rooms

dave = Enemy("Dave", "A smelly zombie")
dining_hall.set_character(dave)
dave.conversation = "Hi my name is Dave, Id like to eat your brain."
dave.weakness= "cheese"


current_room = dining_hall
while dead == False:
      print("\n")
      current_room.get_details()
      inhabitant = current_room.get_character()
      command = input("> ")
      # Check whether a direction was typed
      if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command)
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
                  if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        current_room.set_character(None)
                  else:
                        # What happens if you lose?
                        print("Oh dear, you lost the fight.")
                        dead = True
            else:
                  print("There is no one here to fight with")

# Game over message
if dead == True:
      print("GAME OVER - YOU DIED - YOU LOSE")
