# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    # print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!
def ghost(wordlist):
    print 'Welcome to Ghost!'
    print 'Player 1 goes first.'
    print "Current word fragment:''"
    winner = 1;
    # if word type is list
    # word = [];

    # if word type is string
    word_string = '';
    player = 1;
    while(True):
        input_valid = 1;
        inwordlist = False;
        
        ## input letter from player
        input_message = 'Player '+ str(player) + ' says letter:'
        letter = raw_input(input_message);
        
        ## if letter valid
        if (letter in string.ascii_letters) == False:
            input_valid = 0;
            print letter, 'is not a valid input. Please type the letter again.'
            print ''

        ## if valid, update word and continue
        if input_valid == 1:
            ## if word type is list
            # word.append(letter);
            
            # save the string as type string
            word_string += string.lower(letter);

            print ''

            ## print current word fragment
            print "Current word fragment: '"+ word_string + "'"

            ## The following one is for type list
##            print "Current word fragment:'",
##            for n in range(len(word)):
##                print word[n],
##            print "'"

            word_length = len(word_string);

            for n in range(len(wordlist)):
                if string.find(wordlist[n],word_string) == 0:
                    wordis = wordlist[n];
                    inwordlist = True;
                    break


            ## if no word begins with word_string
            if inwordlist == False:
                print 'Player ' + str(player)+ " loses because no word begins with '" + word_string + "'"
                break
            
            ## if word_string is a word and its length is greater than 3
            elif wordis == word_string and word_length > 3:
                print 'Player ' + str(player) + " loses because '"+ word_string + "' is a word!"
                break
            

            ## if no winner, change player and game continues
            player = 3 - player;
            print 'Player '+ str(player) +"'s turn."

    player = 3 - player;
    print 'Player ' + str(player) + ' wins!'
    return None
            


ghost(wordlist);









    

