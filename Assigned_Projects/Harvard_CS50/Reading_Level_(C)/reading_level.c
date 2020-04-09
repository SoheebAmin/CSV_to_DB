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
    char provided_string[10000];
    printf("Text: ");
    scanf("%[^\n]s", provided_string);

    //put the letters, words, and sentences into floats, as to be divisible in the next step.
    float letters = count_letters(provided_string);
    float words = count_words(provided_string);
    float sentences = count_sentences(provided_string);

    //L = average number of letters per 100 words.
    float L = (letters * 100)/words;

    //S is = average number of sentences per 100 words.
    float S = (sentences * 100)/words;

    //reading level determined by the Coleman-Liau index, explaiened in the ReadMe.
    float reading_level = (0.0588 * L) - (0.296 * S) - 15.8;

    //round grade to a whole number.
    reading_level = round(reading_level);

    //Print calls to see the letter, word, and sentence counts. Can be commented out.
    printf("Letters: %d\n", count_letters(provided_string));
    printf("Words: %d\n", count_words(provided_string));
    printf("Sentences: %d\n", count_sentences(provided_string));

    //return results of level under 1.
    if (reading_level < 1)
    {
        printf("Before Grade 1\n");
        return 0;
    }

    //return results of level over 16.
    if (reading_level > 15)
    {
        printf("Grade 16+\n");
        return 0;
    }

    //return results of reading levels 1 - 15.
    if (reading_level < 15)
    {
        printf("Grade %.0f\n", reading_level);
        return 0;
    }
}

//function to count the letters in the text.
int count_letters(char* provided_string)
{
    //checks if each character is alpha.
    int letters = 0;
    for (int i = 0; i < strlen(provided_string); i++)
    {
        if (isalpha(provided_string[i]) != 0)
        {
            letters++;
        }
    }
    return letters;
}

int count_words(char* provided_string)
{
    //Demarcates a word as space followed by a letter or a quote mark.
    int words = 0;
    for (int i = 0; i < strlen(provided_string); i++)
    {
        char character;
        if (provided_string[i] ==' ')
        {
            char character = provided_string[i+1];
            if (isalpha(character) != 0 || character == '"') 
            {
                words++;
            }
        }
    }
    //adds a word for the first word of the sentence.
    words++;
    return words;
}

int count_sentences(char* provided_string)
{
    //checks for . ? !, counting each one as the end of a sentence.
    int sentences = 0;
    char character = 0;
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