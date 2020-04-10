# CS50 Assignment: Houses

This is one of the few CS50 projects that provides no boilerplate code and was written from scratch by myself. It requires a CS50 specific module that allows SQL code to be executed by python, aptly named cs50. It can be pip installed with python -m pip cs50.

There are two .py files which were created. Firstly, import.py takes the CSV data, breaks up the name to match the schema of the students relation, and then runs CS50's script which generates SQL code from python to populate the relation. Secondly, roster.py...

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

I have provided the sample csv file that CS50 provides, and a students_pre_import.db file that only contains a stududents relation with its schema. Also present is the students_imported.db file which was filled in by the code executed in import.py

## Assignment Details

The actual Houses assignment can be found [here](https://cs50.harvard.edu/x/2020/psets/7/houses "Houses Link").
