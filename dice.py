import random
from colorama import Fore
import pyautogui as auto

nums = [1,2,3,4,5,6]
score = 0
print(" ----------------------------------------------------------------------------")
print(Fore.RED, "             Welcome To The Game!! (Made By TechRebel.)                             ")
print(Fore.WHITE, "----------------------------------------------------------------------------")
print(Fore.BLUE, "IF U ROLL A ONE U LOSE ALL YOU SCORE AND BECOMES 0, IF U WANT TO STOP AT ANY POINT YOU WILL NOT LOSE YOUR SCORE\n")
print(Fore.BLUE, "IF YOUR SCORE ADDS UP TO 50, YOU WIN!!!")
run = True
while run:

    user_choice = input(Fore.YELLOW + "Do you want to roll the dice? [Enter 'Y' or Press 'Enter' to continue OR Enter 'N' to quit: ").upper()
    if score >= 50:
        run = False
        print(Fore.GREEN, "YOUR SCORE IS ", score, "....YOU WIN!!!")
    if user_choice == 'Y' or user_choice == "":
        roll = random.choice(nums)
        print(Fore.LIGHTMAGENTA_EX, "You rolled a : ",roll)
        score = score + int(roll)
        if roll == 1:
            print(Fore.GREEN, "Unlucky! You rolled a one.. Your score is 0")
            break
            run == False
        else:
            continue
    elif user_choice == 'N':
        run = False
        print(Fore.LIGHTBLUE_EX, "Your score is ", score)
    else:
        print("PLEASE ENTER (Y) or (N)")
