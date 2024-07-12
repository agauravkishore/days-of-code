#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
# from art import logo

def user_choice():
  user = int(input("Pick a number between 1 and 100: "))
  return user

def level(diff):
  if diff == 'easy':
    lives = 10
  else:
    lives = 5
  return lives

# computer choice
COMP_CHOICE = random.randint(1,100)
print(COMP_CHOICE)

def game_logic():
  diff = input("Pick your difficulty: Easy or Hard ").lower()
  user_pick = user_choice()
  chance = level(diff)
  print(f"You have {chance} chances to guess the right answer")

  # print(type(chance))
  while chance > 0:
    if user_pick == COMP_CHOICE:
      print(f"You got it! Your Answer was {user_pick}")
      return user_pick
    elif user_pick > COMP_CHOICE:
      print("Too High")
      chance -= 1
      user_pick = user_choice()
    elif user_pick < COMP_CHOICE:
      print("Too Low")
      chance -= 1
      user_pick = user_choice()

  if chance == 0:
    print("You're out of chances: You lose")


game_logic()

    
    
  
