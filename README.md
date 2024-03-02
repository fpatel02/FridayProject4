# FridayProject4

fridayProject4 has the objective of recreating Friday projects 1-3 with the help of generative AI. The steps of the code for Friday Project 1 are as follows:

    # Create lists of different word types
    # Get player input for different story elements
    # Build the story with random word choices
    # Print the complete MadLibs story
    # Start the game!

import random: We import the random module to randomly select words for our MadLibs story.

def madlibs():: We define a function named madlibs(). This is where the core logic of the game resides.

Word lists: We create lists (adjectives, nouns, verbs) to store different types of words. You can expand these lists for more variety.

Player input: We use input() to get the following from the player:

name: A name for the story's character.
place: A setting for the story.
number: A number to add a fun element.
random.choice(): The random.choice() function selects a random element from a list. This is used to pick random words.

Building the story: We use f-strings for easy formatting of the story. We insert the player's input and random choices from our word lists.

print(story): We print the hilarious MadLibs story!

if __name__ == "__main__": madlibs(): This ensures that the madlibs() function is called only if we run the script directly (and not if it's imported as a module).