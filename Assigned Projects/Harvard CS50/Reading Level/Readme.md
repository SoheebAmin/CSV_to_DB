# CS50 Assignment: Readability

This is one of the few assignments from Harvard's CS50 with no boilerplate code, and it is written with one's own approach.

Given a sample input from a test, "reading_level.c" uses the [Coleman-Liau index](https://readabilityformulas.com/coleman-liau-readability-formula.php "The Coleman-Liau index") to output the reading level according to the index.

The program was originally written with features from CS50's library (cs50.h), which helps with getting user input, as well as being training wells to avoid dealing with char pointers. I rewrote some parts of the code so that it can work without this library.

## Usage

The input must be text of any length up to a 10,000 character limit. It should be without newlines, or else the sample will terminate at the newline.

```c

Input: It was almost December, and Jonas was beginning to be frightened. No. Wrong word, Jonas thought. Frightened meant that deep, sickening feeling of something terrible about to happen. Frightened was the way he had felt a year ago when an >unidentified aircraft had overflown the community twice. He had seen it both times.

Output: Grade 10

```

## Assignment Details

The actual Readability assignment can be found [here](https://cs50.harvard.edu/college/2019/fall/psets/2/readability/ "Readability").
