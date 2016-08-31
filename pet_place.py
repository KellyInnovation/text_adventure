from sys import exit

def start():
	print("You are in the lobby of Pet Place.")
	print("There is a first floor and a second floor, each with three doors.")
	print("On which floor do you start?")

	floor = input(">  ")

def sadness(why):
	print(why, "The animals are sad and get sick.")
	exit(0)

def initial():
	print("Welcome to Pet Place")
	print("Will you help the owner take care of the animals?")
	
	help_pets = input(">  ")

	if help_pets == "yes":
		print("Great, let's get started.")
		start()
	elif help_pets == "no":
		sadness("You didn't even try.")
	else:
		print("I can't understand you.  Leave Pet Place.")
		exit(0)

initial()