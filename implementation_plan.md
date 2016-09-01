#Implementation Plan

##Development Order
1) Create menus for selection
2) Define if loops for each room 
3) General game requirements (win, lose, ...)
4) Saving and restarting

##Class: Rooms

###All Rooms
Choice to leave the room

###Supply Rooms
Grooming = Brush - Green Door
Food = Bird Seed - Orange Door
Toys = Ball - Red Door

Choices
Leave Room
Get Supply
Requires correctly answering math problem

###Animal Rooms
Bunny - Purple Door
Peacock - Blue Door
Golden Retriever - Yellow Door

Choices
Leave Room
Take Care of Animal
Select Item for use

###Starting Room
Lobby

Choices
Exit Game 
Choose a Room

##Class: Game

###Start
Reference Starting Room
Initial Prompt to Play

###End
Save and Quit
Lose

###Winning
Bunny = brushing
Peacock = bird seed
Golden Retriever = Ball

Win after helping all 3 animals.

###Lose
Use wrong item with the animal




##Version 2
Levels based on age
At higher levels, lose if wrong on math problems.
Time limit
Grooming, Feeding, and Toy Items for each animal.
Limit to inventory at a time.