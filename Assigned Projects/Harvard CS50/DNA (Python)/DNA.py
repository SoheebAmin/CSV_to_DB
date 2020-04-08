#run with: python dna.py databases/large.csv sequences/10.txt

from sys import argv
import csv

#open csv file and copy data
csvfile = open(argv[1], newline='')
raw_data_list = csv.reader(csvfile, delimiter=' ')

# create a list of lists for names and sequences, separated by commas.
names_list = []
for element in raw_data_list:
    names_list.append(element[0].split(","))


# remove the STRs and turn them into their own list
str_list = names_list.pop(0)


# throw out the "name" at the start of the STR list.
str_list.pop(0)

# save sequence into a string
txtfile = open(argv[2], 'r')
sequence = txtfile.read()


# empty list that will populate to be the number of base matches in the seq per base, in order.
base_list = []

# grab sequence to test and its lengnth against each sequence that matches the legnth, and populate the base list.
for STR in str_list:
    len_str = len(STR)

    # keeps track of what position the current base letter is on
    base_position = 0

    # counts the # of times bases match
    base_matches = 0

    # keeps track of the longest sequence of that base
    lead_counter = 0

    # From each base, check the STR against each set of base letters the same legnth as the STR.
    for base in sequence:
        seq_to_check = sequence[base_position:base_position + len_str]
        # if it matches, add one to match count, and jump the legnth of the STR to see if next bunch matches.
        if seq_to_check == STR:
            base_matches += 1
            base_position += len_str
            # keep track of the longest string of sucessful STR finds.
            if base_matches > lead_counter:
                lead_counter = base_matches
        # set successful match counter to 0, and increment by a single base.
        else:
            base_matches = 0
            base_position += 1
    base_list.append(lead_counter)

# check base_count against database of people's base counts for a match. Done as a function to return once match is found.
def check_list(names_list, base_list):
    for person_base in names_list:
        i = 0
        for _ in base_list:
            if int((person_base[i+1])) != base_list[i]:
                break
            i += 1
            if i == len(base_list):
                return(person_base[0])
    return("no match")


#call previous function using the names_list and base_list to compare the names against the bases in the given sequences.
print(check_list(names_list, base_list))

#close open files
txtfile.close()
csvfile.close()
