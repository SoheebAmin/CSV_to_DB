# NOTE: This program is the first one I wrote on my own. I didn't even understand newlines, and wrote way more
# code than necessary since I didn't know when to use loops optimally. So laugh, and know that I am laughing with yoU!

# function that defines the game, starting with intructions. 
def lets_play_a_game():
  w = 0
  l = 0

  # this is how I handled making newlines before I knew what they were.
  print("Hello. Lets play a game where you provide a number, and I'll tell you what that number is when timed by 3 and then divided by 2. Then, I'll do it with your number, then you with mine, for 3 rounds.") 
  print("")
  
  #The following condition only applies to the Python 2.7 version of the game, since int division only returned ints before Python 3.
  #print("Oh and one more thing. To make things easy, we are ignoring all decimals, so just act like they don't exist in the answer, and I'll do the same.")
  #print("")
  
  print("We'll do this 3 times. If you get at least 2 right, you win! If not, you lose. Okay, so lets start. Gimme a number. I'd suggest not making it too big.")

  # gets a number from the user
  number = eval(input())
  
  # Updates the number to 3x then /2.
  print("Okay, here is your new number")
  number = (number*3)/2
  print(number)

  # sets what the answet the user needs to calculate.
  next_answer = (number*3)/2

  # checks input against answer, awarding a win if correct, or loss if incorrect.
  print("Now you need to multiply it by 3 and divide it by 2")
  number2 = eval(input())
  if number2 == next_answer:
    print("Good job! Seems like you got it.")
    w += 1
  else:
      print("Nope, the correct answer was " + str(next_answer) + ". Its okay, you can still win if you get the next two right.")
      l +=1
  
  # updates the number to the new one to be calculated by the user.
  print("")
  print("Onto the next one. Now I'll take the " + str(next_answer) + " and update it. You need to take that number and multiply it by 3 and divide by 2 again.")
  next_answer = (next_answer*3)/2
  print(next_answer)

  # checks input against answer, awarding a win if correct, or loss if incorrect.
  print("Your turn ")
  next_answer = (next_answer*3)/2
  number3 = eval(input())
  if number3 == next_answer:
    print("Good job! A point for you.")
    w += 1
  else:
    print("Nope, the correct answer was " + str(next_answer) + ". Too bad.")
    l +=1

  # updates the number to the new one to be calculated by the user.
  print("")
  print("Last one now. Now I'll take the " + str(next_answer) + " and update it.")
  next_answer = (next_answer*3)/2
  print(next_answer)

  # checks input against answer, awarding a win if correct, or loss if incorrect.
  print("Your turn ")
  next_answer = (next_answer*3)/2
  number3 = eval(input())
  if number3 == next_answer:
    print("Strong finish, getting that final point")
    w += 1
  else:
    print("Nope, the correct answer was " + str(next_answer) + ". Ending things on a loss is so sad.")
    l +=1
  
  # gives the final score of the game, and a message
  print("")
  print("And that concludes our game! Here is your score:")
  print("")
  print("You got " + str(w) + " right and " + str(l) + " wrong.") 
  if w == 3:
    print("Wow a perfect score. Did you cheat or something?")
  if w == 2:
    print("You won, but just barely. Hey, a wins a win, right?")
  if w == 1:
    print("Aw too bad, one short winning, but also its only one right as well, hehe")
  if w == 0:
    print("Oh, so I go through all this effort to make a game for you and can't even get a single question right? I hope for your sake it was on purpose.")
  print("")
  print("Thanks for playing!")
  return ""
    
#calls function to play the game.
print(lets_play_a_game())