
#promps user for a string to search against all English words.
print("Give the letters you want to find in a word: ", end="")
letters = input()

# counter for the number of words found
i = 0

# open dictionary of words, strip newline, iterate over each word, and match against provided string.
dictionary = open("all_eng_word.txt", "r")
for word in dictionary.readlines():
    word = word.strip()
    if  letters in word and word[-2:] != "'s":
        i+=1
        print (f"{word}")


#prints results and their count.
print(f"{i} words were found with {letters}.")