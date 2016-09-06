from sys import exit

from room import Rooms



class GamePlay():
	"""docstring for Game"""
	def __init__(self):
		self.happy_animal = []
		self.rooms = Rooms()

	def leave(self):
		print("The animals are sad.  Please leave Pet Place.")
		exit(0)

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
			self.rooms.lobby()
		elif help_pets.lower() == "no":
			print("You didn't even try.")
			self.leave()
		else:
			print("Yes or No?")
			self.start()

	def winning(self):
		if self.happy_animal == "Golden Retriever" and "Peacock" and "Bunny":
			print("Congratulations!  You won the game.")
			print("All of the animals are so happy!")
			print("""
			**********************************************************************

											   ______
					                    ~——----  ___ --———-~
							          /	   ~——---   ---—~    \
							        /	 /    ~—------~    \   \
							      /	   /    /   ~---~   \    \   \
							    /	 /    /   /       \   \    \   \
							   |    |  	 |   |         |   |    |   |
							   |    |    |   |         |   |    |   |
							   |    |    |   |         |   |    |   |



							   /\      /\
					          /  \    /  \
					         |    |  |    |
					          \   /___\   /
					          /           \
					         |    O   O   |
					          \     ?    /             
					            \   ~   /   ____——_____
					              |     \__/            \
 				                 /                        \
				                |			          	   |O
				                |__________________________|   

			""")

	def play(self):
		while not self.leave() and not self.winning:
			pass




