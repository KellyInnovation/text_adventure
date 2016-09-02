import random

#import game
from game import get_menu_selection, display_selection_error

class Rooms():
	"""docstring for Rooms"""
	ROOM_DOOR_MENU = (
		"1: Red Door",
		"2: Orange Door",
		"3: Yellow Door",
		"4: Green Door",
		"5: Blue Door",
		"6: Purlple Door",
		"0: Leave Pet Place",
	)

	ANIMAL_ROOM_MENU = (
		"1: Use Specialty Item",
		"0: Return to Lobby",
	)

	SPECIALTY_ROOM_MENU = (
		"1: Buy Specialty Item",
		"0: Return to Lobby",
	)



	def __init__(self):
		self.inventory = []
		self.specialty_room = None
		self.animal_room = None


	def earn_item(self):
		print("In order to buy the specialty item, the store needs you to solve the following problem: ")
		x = random.randrange(1,10)
		y = random.randrange(1,10)
		answer = x + y
		print("%s + %s", % (x, y))

		player_answer = int(input("What is the answer? \n > "))

		if player_answer == answer:
			print("Great job!")
				if self.specialty_room == "toy_room":
					print("You earned a Red Ball!")
					self.inventory.append("Red Ball")
				elif self.specialty_room == "grocery_room":
					print("You earned Bird Seed!")
					self.inventory.append("Bird Seed")
				elif self.specialty_room == "grooming_room":
					print("You earned a Small Brush")
					self.inventory.append("Small Brush")
			self.specialty_room = None
			break
		else:
			print("Try again.")
			self.earn_item()


	def specialty_item_room(self):
		print("What would you like to do?")
		while True:
			menu_selection = get_menu_selection(rooms.SPECIALTY_ROOM_MENU)

			if menu_selection == "0":
				break
			elif menu_selection == "1":	
				self.earn_item()
			else: 
				display_selection_error(menu_selection)
	
	def toy_room(self):
		self.specialty_room = "toy_room"

		print("Welcome to the Toy Store!")
		print("You see a bright, red ball one of the animals would love.")

		self.specialty_room(toy_room) 

	def grocery_room(self):
		self.specialty_room = "grocery_room"

		print("Welcome to the Grocery Store!")
		print("You see a bag of bird seed one of the animals would love.")

		self.specialty_item_room(grocery_room) 

	def grooming_room(self):
		
		self.specialty_room = "grooming_room"
		
		print("Welcome to the Groooming Store!")
		print("You see a small, brush one of the animals would really enjoy.")

		self.specialty_item_room(grooming_room) 

	def available_specialty_item(self, inventory):
		print("You have the following specialty items: ")

		if len(self.inventory) == 0:
			print("You do not have any specialty items yet.")
			break
		else:
			print("0: Save items for later.")

			if self.inventory == "Red Ball":
				print("1: Red Ball")
			if self.inventory == "Bird Seed":
				print("2: Bird Seed")
			if self.inventory == "Small Brush":
				print("3: Small Brush")


	def choose_specialty_item(self):
		while True:
			menu_selection = get_menu_selection(self.available_specialty_item())

			if menu_selection == "0":
				break
			elif 


			4:"Brush"}),
		{2:"Bird Seed"}),
		{1:"Red Ball"}),


	def animal_room_choice(self):
		print("What would you like to do?")
		while True:
			menu_selection = get_menu_selection(rooms.ANIMAL_ROOM_MENU)

			if menu_selection == "0":
				break
			elif menu_selection == "1":	
				self.use_specialty_item()
			else: 
				display_selection_error(menu_selection)

	def golden_retriever_room(self):
		self.animal_room = "golden_retriever_room"

		print("As you open the door, you hear excited barks.")
		print("Inside this room is a golden retriever, with soft, golden fur.")
		print("This playful puppy is so excited to see you.")

		self.animal_room_choice(golden_retriever_room)

		if specialty_item = red_ball:
			print("Great job!  The puppy really loved playing with you")


	def peacock_room(self):
		self.animal_room = "peacock_room"

		print("Inside, there is a beautiful peacock fanning its tail feathers.")
		print("He is pecking the ground with his azure, blue head.")

		self.animal_room_choice(peacock_room)

	def bunny_room(self):
		self.animal_room = "bunny_room"

		print("As soon as you walk in, a fluffy bunny hops over to see you.")
		print("The bunny looks cute, but a little messy.")

		self.animal_room_choice(bunny_room)

	def lobby(self):
		print("There are six doors in the lobby.")
		print("\n")
		print("Which door do you open?")

		while True:
			menu_selection = get_menu_selection(rooms.ROOM_DOOR_MENU)

			if menu_selection == "0":
				break
			elif menu_selection == "1":
				self.toy_room()
			elif menu_selection == "2":
				self.grocery_room()
			elif menu_selection == "3":
				self.golden_retriever_room()
			elif menu_selection == "4":
				self.grooming_room()
			elif menu_selection == "5":
				self.peacock_room()
			elif menu_selection == "6":
				self.bunny_room()
			else: 
				display_selection_error(menu_selection)