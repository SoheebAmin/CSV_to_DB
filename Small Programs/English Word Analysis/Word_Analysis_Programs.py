# Opens the dictionary. Insert your dictionary path here.
dictionary = open(r"c:/MyCode/Small Programs/English Word Analysis/all_eng_word_not.txt", "r")

# stips newlines and removes possessives, placing each word as an item in a list.
raw_words = []
for word in dictionary.readlines():
    word = word.strip()
    if word[-2:] != "'s":
        raw_words.append(word)

# ensures there is list loaded from a dictionary
if raw_words == []:
    raise Exception("dictionary not provided, or did not load into list")


# provides the list of possible choices of programs.
while (True):
    print("""
    Choose which dictionary analysis program to run:\n
    1. Substring Full Search: Finds all dictionary words that have your substring in them.\n
    2. Substring Start Search: Finds all dictionary words that start with your substring. \n
    3. Substring End Search: Finds all dictionary words that end with your substring. \n
    4. Letters in Order: Find all dictionary words that have the letters in the provided order, regardless of if consecutive. \n
    5. Letters Out of Order: Finds all dictionary words that have the provided letters, in any order. \n
    6. Super String: Finds all dictionary words contained in the string you provided. \n 
    """)
    print("Which Program would you like to run? Please enter the number: ", end = "")
    try:
        program_choice = int(input())
    except ValueError:
        print("Please enter a number")
        continue
    # confirms compliance, else re-prompts.
    if program_choice < 1 or program_choice > 6:
        print("Sorry, please pick a number from the program list")
        continue
    else:
        break
    
# asks for text, while confirming it is only alphabetical, or else re-prompts.
while (True):    
    print ("Please provide your text: ", end = "")
    input_string= input()
    if input_string.isalpha() == False:
        print("Please use only letters")
        continue
    else:
        break

##############################################################################################################################

# Program 1. Substring Full Search: Finds all dictionary words that have your substring in them.

def substring_full_search(input_string):
# counter for the number of words found
    i = 0
    # matches provided string against each dictionary word, checking if "input_string" exists in "word".
    for word in raw_words:
        if  input_string in word:
            print (f"{word}")
            i+=1
    # returns final count and confirmation.
    print(f"\n{i} words were found with {input_string} as a substring.\n")
    return 0

##############################################################################################################################

#Program 2. Finds all dictionary words that start with your substring.

def substring_start_search(input_string):
    # counter for the number of words found
    i = 0
    
    # matches provided string against each dictionary word, checking if "input_string" is the start of "word".
    for word in raw_words:
        #the point in which we are checking the input_string
        if  input_string == word[0:len(input_string)] and word[-2:] != "'s":
            i+=1
            print (f"{word}")
    # returns final count and confirmation.
    print(f"\n{i} words were found that start with {input_string}.\n")
    return 0

##############################################################################################################################

# Program 3. Substring End Search: Finds all dictionary words that end with your substring.

def substring_end_search(input_string):
    # counter for the number of words found
    i = 0
    
    # matches provided string against each dictionary word, checking if "input_string" is the end of "word".
    for word in raw_words:
        #the point in which we are checking the input_string
        matchpoint = len(word) - len(input_string)
        if  input_string == word[matchpoint:]:
            i+=1
            print (f"{word}")
    # returns final count and confirmation.
    print(f"\n{i} words were found that end in {input_string}.\n")
    return 0

##############################################################################################################################

# Program 4. Find all dictionary words that have the letters in the provided order, regardless of if consecutive.
def letters_in_order(input_string):
    # counter for the number of words found
    i = 0
    # checks to see if input letters exist in order in the dictionary words.
    for word in raw_words:
        if all(letter in word for letter in input_string):
            letters_index = [word.index(letter) for letter in input_string]
            if letters_index == sorted(letters_index):
                print(f"{word}")
                i+=1
    # returns final count and confirmation.
    print(f"\n{i} words were found that have all the letters of {input_string} in order.\n")
    return 0


##############################################################################################################################

# Program 5. Finds all dictionary words that have the provided letters, in any order.

def letters_out_of_order(input_string):
    # counter for the number of words found
    i = 0
    # breaks word down into letters, and return dictionary words that have all of the provided letters.
    for word in raw_words:
        if  all(x in word for x in input_string):
            print (f"{word}")
            i+=1
    # returns final count and confirmation.
    print(f"\n{i} words were found that have all the letters: {input_string}.\n")
    return 0

##############################################################################################################################

# Program 6. Finds all dictionary words contained in the string you provided.

def superstring(input_string):
    # counter for the number of words found
    i = 0
    # matches provided dictionary words against provided string, checking if "word" exists in "input_string".
    for word in raw_words:
        if  word in input_string and word[-2:] and word != input_string:
            print (f"{word}")
            i+=1
    # returns final count and confirmation.
    print(f"\n{i} words were found inside {input_string}.\n")
    return 0

##############################################################################################################################

# calls the selected function.
if program_choice == 1:
    substring_full_search(input_string)
if program_choice == 2:
    substring_start_search(input_string)
if program_choice == 3:
    substring_end_search(input_string)
if program_choice == 4:
    letters_in_order(input_string)
if program_choice == 5:
    letters_out_of_order(input_string)
if program_choice == 6:
    superstring(input_string)