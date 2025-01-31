class Item():
  def __init__(self, name, description):
    self._name = name
    self._description = description

  @property 
  def name(self):
    return self._name

  @name.setter
  def name(self, item_name):
    self._name = item_name


  @property 
  def description(self):
     return self._description

  @description.setter
  def set_description(self, description):
    self._description = description

  def describe_item(self):
    print(self.description)
