#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

//prototypes
int count_letters(char* provided_string);
int count_words(char* provided_string);
int count_sentences(char* provided_string);


int main(void)
{
    //get user input up to 10,000 chars, so as long as there is no newline.
    char text[10000];
    printf("Text: ");
    scanf("%[^\n]s", text);

    //put the letters, words, and sentences into vars
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    //L = average number of letters per 100 words
    float L = (letters*100)/words;

    //S is = average number of sentences per 100 words
    float S = (sentences*100)/words;

    //reading level determined by the Coleman-Liau index, explaiened in the ReadMe.
    float reading_level = (0.0588 * L) - (0.296 * S) - 15.8;

    //round grade
    reading_level = round(reading_level);

    //enable these print calls to see the letter, word, and sentence counts.

    printf("Letters: %d\n", count_letters(text));
    printf("Words: %d\n", count_words(text));
    printf("Sentences: %d\n", count_sentences(text));


    //deal with less than one and over 16
    if (reading_level < 1)
    {
        printf("Before Grade 1\n");
        return 0;
    }

    if (reading_level > 15)
    {
        printf("Grade 16+\n");
        return 0;
    }

    //pring reading level if within level range.
    if (reading_level < 15)
    {
        printf("Grade %.0f\n", reading_level);
        return 0;
    }
}

//function to count letters
int count_letters(char* provided_string)
{
    //number of letters in string
    int letters = 0;

    //counts letters in string
    for (int i = 0; i < strlen(provided_string); i++)
    {
        if (isalpha(provided_string[i]) != 0)
        {
            letters++;
        }
    }
    return letters;
}

//function to count words
int count_words(char* provided_string)
{
    // word count
    int words = 0;

    //iterate over letters and demarcates a word as space followed by a letter.
    for (int i = 0; i < strlen(provided_string); i++)
    {
        char character;
        if (provided_string[i] ==' ')
        {
            if(isalpha(provided_string[i+1]) != 0)
            {
                words++;
            }
        }
    }
    //a word is added for the first word of the sentence
    words++;
    return words;
}

//function to count sentences
int count_sentences(char* provided_string)
{
    //sentence count
    int sentences = 0;
    char character = 0;
    //iterate over letters and count . ? ! as end of sentence
    for (int i = 0; i < strlen(provided_string); i++)
    {
        character = provided_string[i];
        if (character == '.' || character == '?' || character == '!')
        {
          sentences++;
        }   
    } 
   //handles the case in which the user provided no punctuation by assuming one sentence.
    if (sentences == 0)
    {
        sentences++;
    }
    return sentences;
}