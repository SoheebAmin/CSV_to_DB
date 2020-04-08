# Word Analysis Read Me

This program gives a choice of different operations that can be performed against a list of all English words. The operation is chosen via an input number at the start of the program. The operations are:

    1. Substring Full Search: Finds all dictionary words that have your substring in them.
    2. Substring Start Search: Finds all dictionary words that start with your substring. 
    3. Substring End Search: Finds all dictionary words that end with your substring. 
    4. Letters in Order: Find all dictionary words that have the letters in the provided order, regardless of if consecutive. 
    5. Letters Out of Order: Finds all dictionary words that have the provided letters, in any order. 
    6. Super String: Finds all dictionary words contained in the string you provided.

## Some things to Note

The program works with the provided dictionary in this directory. It can also work with any other list of words separated by newlines in a file. The file would just need to be placed in the "file open" function at the top of the program.

The initial word list creator has a condition to remove possessives, ("!= "'s") which can be removed.

All the called functions can be taken out as their own programs to perform the string search operations, but they would also need a line of code to store each "word" in a list, and the return value would become that list.

Regexs were not used because this program was written to practice string manipulation in loops.
