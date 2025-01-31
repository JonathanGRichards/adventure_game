from character import Enemy

dave = Enemy("Dave", "A smelly zombie")

dave.describe()
dave.conversation = "Hi my name is Dave, Id like to eat your brain."
dave.talk()
dave.weakness= "cheese"
print("What will fight with?")
fight_with = input("\n> ")
dave.fight(fight_with)
print(dave.name)
