# CS50 Assignment: Readability

This is one of the few assignments from Harvard's CS50 with no boilerplate code, and instead, it is to be written from start to finish with one's own approach.

## Usage

Given a sample input from a test, "reading_level.c" uses the [Coleman-Liau index](https://readabilityformulas.com/coleman-liau-readability-formula.php "The Coleman-Liau index") to output the reading level according to the index.

The input must be text with a 10,000 character limit and no newlines, or else the sample will terminate at the newline.

>Input: It was almost December, and Jonas was beginning to be frightened. No. Wrong word, Jonas thought. Frightened meant that deep, sickening feeling of something terrible about to happen. Frightened was the way he had felt a year ago when an >unidentified aircraft had overflown the community twice. He had seen it both times. Squinting toward the sky, he had seen the sleek jet, almost a blur at its high speed, go past, and a second later heard the blast of sound that followed. Then one more time, a moment later, from the opposite direction, the same plane.
>
>Output: Grade 8`

The program was originally written with features from CS50's library (cs50.h), which helps with getting user input, as well as being training wells to avoid dealing with char pointers. I rewrote some parts of the code so that it can work without this library.

The actual Readability assignment can be found [here](https://cs50.harvard.edu/college/2019/fall/psets/2/readability/ "Readability").
