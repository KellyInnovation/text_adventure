from sys import exit

class Game():
	"""docstring for Game"""
	def __init__(self):
		self.score = 0
		
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
			start()
		elif help_pets.lower() == "no":
			print("You didn't even try.")
			self.leave()
		else:
			print("Yes or No?")
			self.start()

	def winning(self):
		if score = 3:
			print("Congratulations!  You won the game.")
			print("All of the animals are so happy!")
			print("""


			""")

	def play(self):
		while not self.leave() and not self.winning:
			pass

def get_menu_selection(menu_items):
	print("\n")
	for menu_item in menu_items:
		print(menu_item)

	return input("\nPlease select an option from above. \n  >  ")

def display_selection_error(menu_selection):
	if menu_selection.isdigit():
		print("\n{} is an invalid option, please try again"
			.format(menu_selection))
	else:
		print("\n{} is not a number.  Please select from the options above."
			.format(menu_selection))

if __name__ == '__main__':
	game()

