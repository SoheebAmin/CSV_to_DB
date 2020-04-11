import sys
import cs50

# Ensures correct usage.
if len(sys.argv) != 2:
    sys.exit("Usage: python roster.py house name")

# opens students.db for SQLite.
db = cs50.SQL("sqlite:///students_post_import.db")

# Uses SQL to check which houses are in the database.
houses = db.execute(f"SELECT house FROM Students")
house = sys.argv[1]



# Ensures house exists in database by searching the dict_pairs returned by the db.execute function.
found_house = False
for dict_pair in houses:
    if house in dict_pair.values():
        found_house = True
if found_house == False:
    sys.exit(f"{house} not a house in database.")

# Uses SQL to get the students of the house + birth year in last name, then first name, order.
raw_roster = db.execute(f'SELECT first, middle, last, birth FROM students WHERE house = "{house}" ORDER BY last, first')

# Turns the roster into a list of lists with just the values from the previous query.
list_roster = []
for dicts in raw_roster:
     list_roster.append((list(dicts.values())))

# prints roster in the required format, with a conditional check on if there is a middle name.
for item in list_roster:
    if item[1] == None:
        print(f"{item[0]} {item[2]}, born {item[3]}")
    else:
        print(f"{item[0]} {item[1]} {item[2]}, born {item[3]}")