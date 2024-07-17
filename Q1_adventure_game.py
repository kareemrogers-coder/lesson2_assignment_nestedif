#Lesson 1

####Objective To practice the use of nested if statements in creating a simple text-based adventure game.

###task 1 Code correction:

##You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

###Buggy Code:

""" place = input("Choose a place: forest or cave? ")

if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!") """

#####BELOW IS THE CORRECTED VERSION:

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action =="climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": ### CHANGE "else" to "elif"
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

print("="*50)
print("="*50)

####TASK 2 (SETTING THE SCENE) 

""" Based on the corrected code from Task 1, expand the game. If the user chooses "cave", instead of printing "You find a hidden treasure!" ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision. """



place = input("New Game!!! Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action =="climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else: ## create a nested "else" that will be used to terminate game if invalid entry inputted
        print("invalid entry....GAME OVER!")
elif place == "cave":
    action2 = input("light a torch or proceed in the dark? ") ##created additional "input" for action statement #2 when "cave" is selected.
    if action2 == ("light a torch"):
        print("Follow the path until the end. The treasure awaits you fellow traveler")
    elif action2 == ("proceed in the dark"):
        print("Stumble in darkest you fool MUHAHAHA, Watch your step!!!")
    else:## create a nested "else" that will be used to terminate game if invalid entry inputted
         print("invalid entry....GAME OVER!")
       
else:## create a nested "else" that will be used to terminate game if invalid entry inputted
    print("invalid entry....GAME OVER!")

print("="*60)
print("="*60)

#TASK 3 (DEFAULT PUSH)

""" If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story. """

place = input("New Game!!! Version 3 Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action =="climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else: ## create a nested "else" with a "pass" that will be used to terminate game if invalid entry inputted
        pass ##print("invalid entry....GAME OVER!")
elif place == "cave":
    action2 = input("light a torch or proceed in the dark? ") ##created additional "input" for action statement #2 when "caveïs selected.
    if action2 == ("light a torch"):
        print("Follow the path until the end. The treasure awaits you fellow traveler")
    elif action2 == ("proceed in the dark"):
        print("Stumble in darkest you fool MUHAHAHA, Watch your step!!!")
    else:## create a nested "else" with a "pass" that will be used to terminate game if invalid entry inputted
         pass #print("invalid entry....GAME OVER!")
       
else:## create a nested "else" with a "pass" that will be used to terminate game if invalid entry inputted
    pass #print("invalid entry....GAME OVER!")
