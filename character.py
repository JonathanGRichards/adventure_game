class Character():
 # Create a character​

  def __init__(self, char_name, char_description):
    self.name = char_name
    self.description = char_description
    self._conversation = None

# Describe this character​

  def describe(self):
    print( self.name + " is here!")
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
      print("[" + self.name + " says]: " + self.conversation)
    else:
      print(self.name + " doesn't want to talk to you")

  # Fight with this character​

  def fight(self, combat_item):
    print(self.name + " doesn't want to fight with you")

    return True

class Enemy(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self._weakness = None

  @property
  def weakness(self):
    return self._weakness
  @weakness.setter
  def weakness(self, item_weakness):
    self._weakness = item_weakness

  def fight(self, combat_item):
    if combat_item == self.weakness:
      print("You fend " + self.name + " off with the " + combat_item )
      return True
    else:
        print(self.name + " crushes you, puny adventurer")
        return False
