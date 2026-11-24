import sys


print("Mincer the future")
player_name = ("Mincer")
print("type Mincer to play the game")
player_name = input("Enter your name: ")
if player_name == "Mincer":
    print("Welcome to the game, Mincer!")
else:
    print("You died!")
    print("Didn't you read the instructions? You have to be Mincer to play this game.")
print("You are in a dark room. There is a door to your left and right.")
player_choice = input("Which door do you choose? (left/right): ")
if player_choice == "left":
    print("You find a treasure chest filled with gold!")
    print("You touch it in excitement, but suddenly the chest explodes and you die!")
    sys.exit()
else:
    print("You choose the right door and walk into a trap!")
    print("The trap gives way to a trapdoor that leads to a room that you cannot see in")
print("you are asked a riddle by a cold voice. The 2nd floor is a home the third is a prison. What am I?")
player_choices = input("Enter your answer: ")
if player_choices == "That doesn't make sense":
    print("I asked for a answer not a question.")
    print("You died!")
    sys.exit()
elif player_choices == "stranger":
    print("Correct! You may proceed to the next room.")
else:
    print("Incorrect! You died!")
    sys.exit()
print("You enter the next room and find a key on the floor.")
player_choice = input("Do you pick up the key? (yes/no): ")
if player_choice == "yes":
    print("A bolder smashes down on you and you die!")
    sys.exit()
else:
    print("You wisely leave the key alone and continue on your journey.")
print("There are 8 pathways in front of you that you can see sunlight from; which one do you choose?")
player_choice = input("Enter a number from 1 to 8: ")
if player_choice == "1":
    print("You walk down the path thinking that you are safe, but you die from the poisonous gas in the hallway!")
    sys.exit()
elif player_choice == "2":
    print("You walk down the path and find a hidden treasure!")
    print("You open the treasure chest and find a magical sword that kills you!")
    sys.exit()
elif player_choice == "3":
    print("You walk down the path and find a mysterious artifact!")
    print("You touch it and it teleports a kid from the 1800s who is possessed by a demon and he takes the artifact")
    print("He says The future of hell belongs to me as he makes earth turn into a hell where you escape to the end of tunnel")
    print("To find that you have nothing to live for and you die from a hellfire that burns your soul and body to ashes!")
    sys.exit()
elif player_choice == "4":
    print("You walk down to make friends with a stranger, but he turns out to be a alien that is supposed to warn the planet")
    print("he says I am sorry but my species is supposed to kill you but you have a mental breakdown and kill him")
    print("As you see the skies taken over by leviathons ready to feast on your planet")
    sys.exit()
elif player_choice == "5":
    print("You walk down the path and find a friendly creature!")
    print("you live years with the creature and you think that you have lived a good life, and are ready to die")
    print("but the creature uses its sentient powers to make you live forever and you are forced to live in a world and watch its end")
    sys.exit()
elif player_choice == "6":
    print("You walk down the path and find a dangerous trap!")
    print("It traps you in time and space and you are forced to live every possible outcome of your life")
    print("you come back to your original self but have a realization that there is no point of knowledge as the only way to happiness")
    print("is ingnorance and you die from the realization that you have no purpose in life but to be a cog")
    sys.exit()
elif player_choice == "7":
    print("You walk down the path and find a mysterious door!")
    print("It teleports you back home and you find that mysterious voice from earlier says I always come back as you look back to see nothing")
    print("You win")
elif player_choice == "8":
    print("You walk down the path and find a dead end that is magical!")
    print("It makes your mind consume millions of possible dead ends in your life as you have a mental breakdown and are found in the hospital")
    print("every second you live life while imagining a dead end and you die from the mental breakdown")
    sys.exit()
else:
    print("You die from starvation cause of your confusion!") 