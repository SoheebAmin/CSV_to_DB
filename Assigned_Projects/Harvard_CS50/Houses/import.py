import sys
import csv
import cs50

# Ensures correct usage.
if len(sys.argv) != 2:
    sys.exit("Usage: python import.py input.csv")
if ".csv" not in sys.argv[1]:
    sys.exit("You must load a CSV file")

# opens students.db for SQLite.
db = cs50.SQL("sqlite:///students_post_import.db")

#open csv file and copy data
csvfile = open(sys.argv[1], newline='')
reader = csv.reader(csvfile, delimiter=',')
reader = list(reader)


# breaks name into first, middle, and last by splitting name and appending first, middle, and last, with None = NULL in middle if none:
i = 0
for row in reader:
    names_list = row[0].split()
    if len(names_list) == 3:
        reader[i].append(names_list[0])
        reader[i].append(names_list[1])
        reader[i].append(names_list[2])
    if len(names_list) == 2:
        reader[i].append(names_list[0])
        reader[i].append(None)
        reader[i].append(names_list[1])
    i+=1    

# checks if every column is the same length before attempting to fit it into the database.
for row in reader[1:]:
    if len(row) != 6:
        print(row)
        sys.exit("Column legnth mismatch")

# Uses CS50's db module to execute SQL that will insert the appropriate values into the table.
for row in reader[1:]:
    db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", 
                row[3], row[4], row[5], row[1], row[2])
