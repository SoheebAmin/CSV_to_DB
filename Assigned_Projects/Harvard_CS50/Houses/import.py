import sys
import csv
import cs50

# Ensures correct usage. 
if len(sys.argv) != 2:
    sys.exit("Usage: python import.py input.csv")
if ".csv" not in sys.argv[1]:
    sys.exit("You must load a CSV file")

# opens students.db for SQLite.
db = cs50.SQL("sqlite:///students.db")

# open csv file and copy data
csvfile = open(sys.argv[1], newline='')
reader = csv.reader(csvfile)

# breaks name into first, middle, and last:
# for row in reader:
#    if row[0]

for row in reader:
    db.execute("INSERT INTO students (house) VALUES(?)", row[1])


