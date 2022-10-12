# Importing the good stuff.
import random
from random import randint
import time
from colorama import init, Fore

# . Initializng the dice min and max values.
min_val = 1
max_val = 6

# * Initializes Colorama
init(autoreset=True)

# / Defining the countdown function when closing.
def countdown(Time):
    while Time:
        mins, secs = divmod(Time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        Time -= 1  

# * Print out the credits.
print(Fore.BLUE + 
"                                           *********************************\n"                                                        
"                                           *     The Dice Rolling Game     *")
print(Fore.YELLOW + "                                           *     Made by - Almog Beni      *\n"
"                                           *********************************\n")

# * Print out the instructions.
print(                                    
"                                              The instructions are simple.\n"
"                                    Your'e playing against the computer a Dice Rolling game\n"
"                                        If you guessed the number right - YOU WIN")
print(Fore.RED + "                                                    Else - YOU LOSE.")
print("                                                       Good Luck!\n")




# ! Game Loop.
while True:
    try:
        cube = random.randint(1,6)
        userInput2 = int(input("Please enter your guessing (1-6): "))
        while userInput2 > 6 or userInput2 == 0:
            userInput2 = int(input(Fore.RED + "Invalid input. Please enter your guessing (1-6): "))
        print(Fore.LIGHTCYAN_EX + "Rolling the dice...")
        countdown(3)
        print(Fore.GREEN + "And the number is: ", cube)
        if cube == userInput2:
            print(Fore.GREEN + "You guessed right!")
            print(Fore.LIGHTYELLOW_EX + "Exiting program...")
            countdown(3)
            break
        else:
            print(Fore.LIGHTBLUE_EX + "You didn't guessed the number right.\n"
            "Keep guessing!")
    except ValueError:
        print(Fore.LIGHTBLUE_EX + "\nInvalid input. Please enter your guessing (1-6): ")