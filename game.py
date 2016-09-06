from sys import exit


class GamePlay():
	"""docstring for Game"""



	def leave(self):
		print("The animals are sad.  Please leave Pet Place.")
		exit(0)


	def winning(self):
		
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

	def get_menu_selection(self, menu_items):
		print("\n")
		for menu_item in menu_items:
			print(menu_item)

		return input("\nPlease select an option from above. \n  >  ")

	def display_selection_error(self, menu_selection):
		if menu_selection.isdigit():
			print("\n{} is an invalid option, please try again"
				.format(menu_selection))
		else:
			print("\n{} is not a number.  Please select from the options above."
				.format(menu_selection))


	#def play(self):
		#while not self.leave() and not self.winning:
			#pass




