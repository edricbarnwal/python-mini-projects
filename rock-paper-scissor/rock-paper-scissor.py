

import random

assets = {"R":"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", 'P': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", 'S':"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""}

input("""WELCOME TO ( ROCK | PAPER | SCISSORS ) GAME
      \nPRESS 'ENTER' to start the game: """)

def game_play():
    
    while True:
        game_input =  input("CHOOSE 'R' For 'ROCK' | 'P' For 'PAPER' | 'S' For 'SCISSORS' | 'E' For 'EXIT': ").strip().upper()
        if game_input  == 'E':
            return False
        if game_input in ('R', 'S', 'P'):
            break
        else:
            print ("Please enter a valid input.")
    
    computer_choice =  random.choice(list(assets.keys()))

    print (f"You chose: {assets[game_input]}\n VS \n\n Computer chose: {assets[computer_choice]}")

    if (game_input == 'R' and computer_choice == 'S') or \
    (game_input == 'P' and computer_choice == 'R') or \
    (game_input == 'S' and computer_choice == 'P') : 
        print ("Result: You Win")
    
    elif game_input == computer_choice:
        print ("Result: Draw")
    else:
        print ("Result: Computer Wins")
    return True

while True:
    if not game_play():
        print("Thanks for playing.")
        break
