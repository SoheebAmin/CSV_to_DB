# CS50 Assignment: Readability

This is one of the few assignments from Harvard's CS50 with no boilerplate code, and it is written from the ground up with my own approach.

If you happen to have the STRs (Short Tandem Repeats: a pattern of ATCG that repeats a certain number of times) of someone's DNA, and a sequence of DNA to check against, this program can actually tell if the DNA is a match of not. It is basically how real-world DNA matching happens.

## Usage

The program command line must contain the two arguments:

1- The location of a CSV database that gives STRS to check, and the names of people and their STRs being checked, along with how often they repeat. See the sample below:

```csv

name,AGATC,AATG,TATC
Alice,2,8,3
Bob,4,1,5
Charlie,3,2,5

```

2- The location of a txt file that has one long string as the sequence being checked against.

```txt


```

GGGGGACGGTTTGTCTCACGCCTGTTGGT...

The command line of the program would look as such:

```py


$ python dna.py databases/large.csv sequences/5.txt

Output: Lavender

```

I have provided the sample databases CS50 provides, along with 5 strings that have matches discoverable using the "large" database.

## Assignment Details

The actual DNA assignment can be found [here](https://cs50.harvard.edu/x/2020/psets/6/dna "DNA Link").
