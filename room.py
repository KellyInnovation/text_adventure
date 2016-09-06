from sys import exit
import random
import math

from game import GamePlay

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
		self.games = GamePlay()
		self.happy_animal = []

	def start(self):
		print("Welcome to Pet Place")
		print("You are in the lobby of Pet Place.")
		print("The room is bright, with black and white tiles checkered on the floor.")
		print("Pictures of animals line the walls.")
		print("You hear animals behind closed doors.")
		print("Will you help the owner take care of the animals? Yes, or No?")
		
		help_pets = input(">  ")

		if help_pets.lower() == "yes":
			print("Great, let's get started!")
			self.lobby()
		elif help_pets.lower() == "no":
			print("You didn't even try.")
			self.self.games.leave()
		else:
			print("Yes or No?")
			self.start()	

	def earn_item(self):
		print("In order to buy the specialty item, the store needs you to solve the following problem: ")
		x = random.randrange(1,10)
		y = random.randrange(1,10)
		answer = x + y
		print("%d + %d" % (x, y))

		player_answer = input("What is the answer? \n > ")

		try:
			player_answer = int(player_answer)
		except ValueError:
			print("Please enter a numerical answer.")
			self.earn_item()


		if player_answer == answer:
			print("Great job!")
			if self.specialty_room == "toy_room":
				print("You earned a Red Ball!")
				self.inventory.append("Red Ball")
				self.lobby()
			elif self.specialty_room == "grocery_room":
				print("You earned Bird Seed!")
				self.inventory.append("Bird Seed")
				self.lobby()
			elif self.specialty_room == "grooming_room":
				print("You earned a Small Brush")
				self.inventory.append("Small Brush")
				self.lobby()
			self.specialty_room = None
		else:
			print("Try again.")
			self.earn_item()


	def specialty_item_room(self):
		print("What would you like to do?")
		while True:
			menu_selection = self.games.get_menu_selection(self.SPECIALTY_ROOM_MENU)

			if menu_selection == "0":
				break
			elif menu_selection == "1":	
				self.earn_item()
			else: 
				self.games.display_selection_error(menu_selection)
	
	def toy_room(self):
		self.specialty_room = "toy_room"

		print("Welcome to the Toy Store!")
		print("You see a bright, red ball one of the animals would love.")

		self.specialty_item_room() 

	def grocery_room(self):
		self.specialty_room = "grocery_room"

		print("Welcome to the Grocery Store!")
		print("You see a bag of bird seed one of the animals would love.")

		self.specialty_item_room() 

	def grooming_room(self):
		
		self.specialty_room = "grooming_room"
		
		print("Welcome to the Groooming Store!")
		print("You see a small, brush one of the animals would really enjoy.")

		self.specialty_item_room() 
		

	def use_specialty_item(self):
		while True:
			print("You have the following specialty items: ")
			print("Type which item you would like to use.")

			if len(self.inventory) == 0:
				print("You do not have any specialty items yet.")
				print("0: to go back.")
			else:
				print("0: Save items for later.")
				for inventory_item in self.inventory:
					print(inventory_item)

			use = input("\n What would you like to use? \n  >  ")

			if use == "0":
				print("Your special items will be saved for use in different rooms.\n")
				break
		
			#elif use.lower() != "red ball" or "bird seed" or "small brush":
				#print("Please type the name of an item in your inventory.\n")
				#self.use_specialty_item()

			elif use.lower() == "red ball":
				if self.animal_room == "golden_retriever_room":
					print("The ball was a great idea for the golden retriever.")
					print("Great job!  The puppy really loved playing with you\n\n")
					self.happy_animal.append("Golden Retriever")
					self.inventory.remove("Red Ball")
					self.animal_room = None
					self.winner()
				elif self.animal_room == "peacock_room":
					print("The peacock gets angry and pops the ball.")
					print("He really wanted food.")
					self.games.leave()
				elif self.animal_room == "bunny_room":
					print("The ball bounces and smushes the poor bunny.")
					self.games.leave()
		
			elif use.lower() == "bird seed":
				if self.animal_room == "peacock_room":
					print("Great Job! The peacock was very hungry.")
					print("You watch as the peacock spreads his feathers wide.\n\n")
					self.happy_animal.append("Peacock")
					self.inventory.remove("Bird Seed")
					self.animal_room = None
					self.winner()
				elif self.animal_room == "golden_retriever_room":
					print("The golden retriever breathes in the bird seed.")
					print("She can't stop sneezing.")
					self.games.leave()
				elif self.animal_room == "bunny_room":
					print("The bunny thinks the seed is litter.")
					print("The bunny is even more of a mess.")
					self.games.leave()
		
			elif use.lower() == "small brush":
				if self.animal_room == "bunny_room":
					print("That bunny sure was a mess.")
					print("Great job! You brushed the bunny.")
					print("The bunny sniffs you and likes the petting.\n\n")
					self.happy_animal.append("Bunny")
					self.inventory.remove("Small Brush")
					self.animal_room = None
					self.winner()
				elif self.animal_room == "golden_retriever_room":
					print("The golden retriever eats the brush.")
					print("She doesn't feel very good.")
					self.games.leave()
				elif self.animal_room == "peacock_room":
					print("You pulled out one of his feathers!")
					print("The peacock is mad and squawking!")
					self.games.leave()

			else:
				print("Please select enter the name of an item in your inventory.")
				self.use_specialty_item()

	def animal_room_choice(self):
		print("What would you like to do?")
		while True:
			menu_selection = self.games.get_menu_selection(self.ANIMAL_ROOM_MENU)

			if menu_selection == "0":
				break
			elif menu_selection == "1":	
				self.use_specialty_item()
			else: 
				self.games.display_selection_error(menu_selection)

	def golden_retriever_room(self):
		self.animal_room = "golden_retriever_room"

		print("As you open the door, you hear excited barks.")
		print("Inside this room is a golden retriever, with soft, golden fur.")
		print("This playful puppy is so excited to see you.")

		self.animal_room_choice()

	def peacock_room(self):
		self.animal_room = "peacock_room"

		print("Inside, there is a beautiful peacock fanning its tail feathers.")
		print("He is pecking the ground with his azure, blue head.")

		self.animal_room_choice()

	def bunny_room(self):
		self.animal_room = "bunny_room"

		print("As soon as you walk in, a fluffy bunny hops over to see you.")
		print("The bunny looks cute, but a little messy.")

		self.animal_room_choice()

	def lobby(self):
		print("\nThere are six doors in the lobby.")
		print("\n")
		print("Which door do you open?")

		while True:
			menu_selection = self.games.get_menu_selection(self.ROOM_DOOR_MENU)

			if menu_selection == "0":
				self.games.leave()
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
				self.games.display_selection_error(menu_selection)

	def winner(self):
		if self.happy_animal == ["Golden Retriever", "Peacock", "Bunny"]:
			print("Congratulations!  You won the game.")
			print("All of the animals are so happy!")
			print("""\
**********************************************************************


				      
                  aaiittllttiiaa
              k a i t llyyll t i a k
            k a i t l yynnyy l t i a k					  
          k a i t l y nn  nn y l t i a k						
        k a i t l y n        n y l t i a k  
       k a i t l y n          n y l t i a k 
      k a i t l y n            n y l t i a k

                          .".
                         /  |
                        /  /
                       / ,"
           .-------.--- /
          "._ __.-/ o. o\  
             "   (    Y  )
                  )     /
                 /     (
                /       Y
            .-"         |
           /  _     \    \ 
          /    `. ". ) /' )
         Y       )( / /(,/
        ,|      /     )
       ( |     /     /
        " \_  (__   (__        
            "-._,)--._,)

*********************************************************************
			""")

			exit(0)
		else:
			self.lobby()


