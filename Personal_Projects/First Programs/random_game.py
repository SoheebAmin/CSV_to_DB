# Program actually written ~August 2019. This is the second program I wrote, around the time I completed my first programming course. 
# There is a lot of repeated code here, but the game actually works quite well and is still fun to play. No really, run it with python and give it a try.

#starting "funds" for the diceroll game.
you = 200
computer = 200

import time
import random

#function to start the game. 
def random_game():
  global you
  global computer
  if you >= 350:
      return "You Win! Great Job!"
  if computer >= 350:
      return "You Lose. Too Bad!"
  print('Lets play a game. Its a betting game between you and me. It is very simple. We both have $200 to start, and we each roll dice. Based on our number, we can do a few things. Lets divide the rolls in to MAIN and FOLLOW UP rolls.\n\nIf the MAIN roll number is 1-3, you can chose to give me half your funds, or roll again in a FOLLOW UP role. What happens then depends on the number. 1 means you give me all your funds. 2 means two-thirds. 3 and 4 mean we go by the original half I was going to take. 5 means you keep two-thirds, and 6 means you can keep everything.\n\nIf you roll between 4-6 in your MAIN role, you get half of my money. Then you can choose to do a FOLLOW UP role which will work like the opposite of the losing situation. So, 6 means you get all my funds, 5 means you get two-thirds, 4 and 3 means you get just the original half, 2 means you get one-third, and 1 means I keep all my funds.\n\nIf all of this is confusing, just know this: MAIN ROLL decides if you get half my funds or I get half yours. Then an optional FOLLOW UP role decides if your gains/loss are more, less, or the same as the first roll\n\nOkay lets begin. type "roll" WITH THE QUOTES to do your MAIN role.')

  # calls the main roll function, which stars the first stage of the game.
  main_roll()


# this function is the default stage of the game.
def main_roll():
  global you
  global computer
  if you >= 350:
       print("You Win!")
       return
  if computer >= 350:
       print("You Lose!")
       return

  # the user rolls. The loop ensures the string 'roll' is entered.
  while True:
      try:
          roll = eval(input())
      except NameError:
          print("You forgot the quotes")
          continue
      if roll != "roll":
          print("Sorry, your response can only be roll at this point")
          continue
      else:
          break
  if roll == "roll":
    print("")
    randomized = random.randint(1,6)
    time.sleep(3)
    print("You rolled a " + str(randomized))
    time.sleep(3)
    print("")
  
  # the function with the results and next possible actions.
  another_roll_function(randomized)

# the stage in which the user can choose to further multiply their win or loss.
def another_roll_function(roll):
  global you
  global computer

# different messages based on whether the user is being asked to try to win more, or lose less.
  if roll <= 3:
    print("Aw man. You lost half your funds. So your funds are cut in half. Unless you want to do an optional FOLLOW UP roll to maybe salvage some, or perhaps lose even more. Want to try? If so, type yes (with quotes), or else type no (with quotes) to do another MAIN roll.")
  else:
    print("Alright you got more than 3. So you get half of my funds. But, you do an optional FOLLOW UP roll to get even more. Be aware that if it goes bad, you'll get little to nothing. If you want to try, type yes (with quotes), or else type no (with quotes).")
  
  # the user chooses whether to partake in the extra, higher-risk roll. The user is prompted until the right input is given.
  while True:
      try:
          another_roll = eval(input())
      except NameError:
          print("You forgot the quotes")
          continue
      if another_roll != "no" and another_roll != "yes":
          print("Sorry, your response can only be yes or no with quotes")
          print(another_roll)
          continue
      else:
          break
  
  # If the user opts out of the extra roll, their give up half their funds, or get half of the computer's.
  if another_roll == "no":
    
    # The loss scenario text and updates.
    if roll <= 3: 
      print("Okay so you chose to lose half. Lets update the current funds.")
      computer = computer + (you*0.5)
      you = you*0.5
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
      print("")
      if you >= 350:
        print("You Win!")
        return
      if computer >= 350:
        return
      print("Now roll again for your MAIN roll")

    # The win scenario text and updates.
    if roll > 3:
      print("")
      print("Okay so you chose to take half from me. Lets update the current funds")
      print("")
      you = you + (computer*0.5)
      computer = computer*0.5
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
      print("")
      print("Now roll again for your MAIN roll")
  
  # called if user opts into optional roll.
  if another_roll == "yes":
      print("")
      optional_roll(roll)

  # called if user opts out of optional roll.    
  main_roll() 
  
# This is the optional wild card round the user can opt into, either to try to decrease a loss or increase a win.
def optional_roll(roll):
  
  # the text to be displayed if user is a loser on the defensive.
  if roll <= 3:
    print("Okay so you are trying to reduce your loss, but remember a bad roll can make it worse. The numbers once again are:")
    print("1 means you give me all your funds.")
    print("2 means two-thirds.") 
    print("3 and 4 mean no change and I take half.")
    print("5 means you keep two-thirds.") 
    print("6 means you can keep everything.")
    print("")
    print("Okay type roll (with quotes) to roll")
  
  # text to display is the user is a winner on the offensive.
  else: 
    print("Okay so you are trying to multiply your winnings! You can also lose them if you roll low. Here are the numbers again:")
    print("1 means you get nothing.")
    print("2 means you get one-third.") 
    print("3 and 4 mean no change and you take half.")
    print("5 means get two-thirds.") 
    print("6 means you get everything.")
    print("")
    print("Okay type roll (with quotes) to roll")

  # user does the optional roll.
  while True:
        try:
            roll2 = eval(input())
        except NameError:
            print("You forgot the quotes")
            continue
        if roll2 != "roll":
            print("Sorry, your response can only be roll at this point")
            continue
        else:
            break
  if roll2 == "roll":
      print("")
      randomized = random.randint(1,6)
      time.sleep(3)
      print("You rolled a " + str(randomized))
      time.sleep(3)
      print("")
      optional_game_results(roll, randomized)

#This function deals with all fpossible scenarios for optional rolls. The 'roll' input determines if the game was offensive or defensive, and 'roll2' determins the results of the game.
def optional_game_results(roll, roll2):
  global you
  global computer
  
  # if the first roll was a loss.
  if roll <= 3:

    # prints the text for the results of every roll, and updates accordingly.
    if roll2 == 1:
      print("You just lost all of your funds to me.")
      computer = computer + you
      you = you*0
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
    if roll2 == 2:
      print("You just lost two-thirds of your funds to me.")
      computer = computer + (you*0.666)
      you = (you*0.333)
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
    if roll2 == 3 or roll2 == 4:
      print("Okay there's no change. You lose half")
      computer = computer + (you*0.5)
      you = you*0.5
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
    if roll2 == 5:
      print("You only lost one third now.")
      computer = computer + (you*0.333)
      you = (you*0.666)
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
    if roll2 == 6:
      print("Wow you saved yourself. No loss now.")
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))

  # if the first roll was a win.    
  else:

    # prints the text for the results of every roll, and updates accordingly.
    if roll2 == 1:
      print("You didn't get any of my funds.")
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
    if roll2 == 2:
      print("You only got one-third of my funds")
      you = you + (computer*0.333)
      computer = (computer*0.666)
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
    if roll2 == 3 or roll2 == 4:
      print("Okay there's no change. You get half")
      you = you + (computer*0.5)
      computer = computer*0.5
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
    if roll2 == 5:
      you = you + (computer*0.666)
      computer = (computer*0.333)
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
      print("You got two-thirds of my funds")
    if roll2 == 6:
      print("You just took all of my funds!")
      you = you + computer
      computer = computer*0
      print("Your funds = $" + str(you))
      print("My funds = $" + str(computer))
  print("")
  
  # check to see if win conditions are not met before showing text for another roll.
  if you <= 350 and computer <= 350:
    print("Okay now time for you to do another MAIN roll. Just type roll (with quotes)")
  else:
    print("")
  
  # calls main roll, which either will end the game, or do the next roll.
  main_roll()

# starts the program
random_game()