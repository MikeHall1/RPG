# Item
class Item():
#Super class for all items, weapons and equipment
	def __init__(self, name, value, description):
		self.name = name
		self.value = value
		self.description = description
	
	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self,value)

class Gold(Item):
#...think this is self explanatory
	def __init__(self, amount):
		self.amount = amount
		super().__init__(name ="Gold", description="Shiny gold coins, used to buy new shiny things", value=self.amount)

class Equipment(Item):
	def __init__(self, equipped, durability):
		self.equipped = equipped
		self.durability = durability
		super().__init__(name, value, description)

#### Weapon class/subclasses ####		
class Weapon(Equipment):
###Super class for weapons #####
	def __init__(self, damage):
		self.damage = damage
		super().__init__(name, value, description)

class Sword(Weapon):
	def __init__(self):
		super().__init__(name, value, description, damage)

class Staff(Weapon):
	def __init__(self):
		super().__init__(name, value, description, damage)
	
class Dagger(Weapon):
	def __init__(self):
		super().__init__(name, value, description, damage)
	
class Bow(Weapon):
	def __init__(self, range):
		self.range = range
		super().__init__(name, value, description, damage)

#### end of weapons ####

#### Armour class / subclasses ####
class Armour(Item):
###Super class for armor ####
	def __init__(self, defence, speed):
		super().__init__(name, value, description)
	
class HeadGear(Armour):
	def __init__(self):
		super().__init__(name, value, description, defence, speed)
		
class ChestGear(Armour):
	def __init__(self):
		super().__init__(name, value, description, defence, speed)

class Gloves(Armour):
	def __init__(self):
		super().__init__(name, value, description, defence, speed)

class Shoes(Armour):
	def __init__(self):
		super().__init__(name, value, description, defence, speed)
	
#### end of armour ####