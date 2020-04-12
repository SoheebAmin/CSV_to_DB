# CS50 Assignment

This is one of the few CS50 projects that provides no boilerplate code and was written from scratch by myself. It requires a CS50 specific module that allows SQL code to be executed by python, aptly named cs50. It can be pip installed with python -m pip cs50.

There are two .py files which were created. Firstly, import.py takes the CSV data, breaks up the name to match the schema of the students relation, and then runs CS50's script which generates SQL code from python to populate the relation. Secondly, roster.py, which conducts an SQL query on the database and return a custom-formatted version of it.

## import.py Usage

This program command line must contain the location of a CSV database that contains the full name of a student, their house, and their birth year.

```csv

name,house,birth
Adelaide Murton,Slytherin,1982
Adrian Pucey,Slytherin,1977
Anthony Goldstein,Ravenclaw,1980
...

```

The command line of the program would look as such:

```cmd

python input.py characters.csv

```

## roster.py Usage

This demonstrates how the CS50 module can use Python to query a database. The program takes one input of the name of a house, and outputs the names of all the students in that house with their birth year, ordered by last name, then first name.

The command line and output of the program would look as such:

```cmd

python roster.py Hufflepuff

Hannah Abbott, born 1980
Susan Bones, born 1979
Cedric Diggory, born 1977
Justin Finch-Fletchley, born 1979
Ernest Macmillan, born 1980

```

I have provided the sample csv file that CS50 provides, and a students_pre_import.db file that only contains a students relation with its schema. Also present is the students_post_import.db file which was filled in by the code executed in import.py

## Assignment Details

The actual Houses assignment can be found [here](https://cs50.harvard.edu/x/2020/psets/7/houses "Houses Link").
