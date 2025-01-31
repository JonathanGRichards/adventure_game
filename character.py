class Character():
 # Create a character​

  def __init__(self, char_name, char_description):
    self.name = char_name
    self.description = char_description
    self._conversation = None

# Describe this character​

  def describe(self):
    print(f"{self.name} is here!")
    print( self.description)

  # Set what this character will say when talked to​
  @property
  def conversation(self):
    return self._conversation

  @conversation.setter
  def conversation(self, conversation):
    self._conversation = conversation
  # Talk to this character​

  def talk(self):
    if self.conversation is not None:
      print(f"[{self.name} says]:{self.conversation}")
    else:
      print(f"{self.name} doesn't want to talk to you")

  # Fight with this character​

  def fight(self, combat_item):
    print(f"{self.name} doesn't want to fight with you")

    return True

class Enemy(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self._weakness = None
    self._inventory = None

  @property
  def weakness(self):
    return self._weakness
  @weakness.setter
  def weakness(self, item_weakness):
    self._weakness = item_weakness
  
  @property
  def inventory(self):
    return self._inventory

  @inventory.setter
  def inventory(self, item_inventory):
    self._inventory = item_inventory

  def fight(self, combat_item):
    if combat_item == self.weakness:
      print(f"You fend {self.name} off with the {combat_item}")
      return True
    else:
        print(f"{self.name} crushes you, puny adventurer")
        return False
    
class Friend(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self._strength = None
    self._inventory = None

  @property
  def strength(self):
    return self._strength
  
  @strength.setter
  def strength(self, item_strength):
    self._strength = item_strength

  @property
  def inventory(self):
    return self._inventory

  @inventory.setter
  def inventory(self, item_inventory):
    self._inventory = item_inventory

  def console(self, action):
    if action == self.strength:
      print(f"You approach {self.name} and give them strength with a {action}")
      return True
    else:
      print(f"{self.name} stares blankly into space...")
      return
