#Write a program that reads the contents of a text file 
# (you can use this file - sometext.txt  Download sometext.txt). 
# The program should create a dictionary in which the keys are the 
# individual words found in the file and the values are the number 
# of times each word appears. For example, if the word “the” appears 
# 128 times, the dictionary would contain an element with 'the' as the 
# key and 128 as the value. The program should display the frequency 
# of each word.

import csv

text = open('sometext.txt','r')

dictionary = dict()

for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Split the line into words
    words = line.split(' ')
                         
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in dictionary:
            # Increment count of word by 1
            dictionary[word] = dictionary[word] + 1
        else:
            # Add the word to dictionary with count 1
            dictionary[word] = 1
  
# Print the contents of dictionary for the user
for key in list(dictionary.keys()):
    print(key, ':', dictionary[key])

#print(d)

text.close()
