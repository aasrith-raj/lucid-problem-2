Problem Statement: Top Frequency Words (Data Processing)

You are given a text file containing millions of words (one word per line). Write a program that returns the top 10 most frequent words.

First to read the text file we use pandas library to read the file and we convert it to an array of words, then the next part of the code counts how many time the word is repeated in the array and make a dictionary where we store this information.

Then the next part of the code is to search for the highest count value of the word from the dictionary and the word with highest count value is placed in the new dictionary "top_words" and that top word is popped out from the dictionary so that it doesn't count its value for the next iteration. this is done 10 time so that we can find top 10 words that are frequent in the file.

Ann finally the top_words is printed out with the word and its frequency.