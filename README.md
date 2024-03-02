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

The steps of the code for Friday Project 2 are as follows:

    # Generate 5 random numbers between 1 and 69 (inclusive)
    # Generate 1 random Powerball number between 1 and 26 (inclusive)
    # Sort the regular numbers in ascending order (optional, but some players prefer it this way)
    # Return the list of winning numbers    
    # Get the winning numbers  
    # Print the winning numbers in a user-friendly format

import random: We import the random module to generate random numbers for the lottery simulation.
def generate_powerball_numbers():: We define a function named generate_powerball_numbers(). This function generates the random lottery numbers.
Generating regular numbers:
random.sample(range(1, 70), 5): This line generates 5 unique random numbers between 1 and 69 (inclusive) using the random.sample() function.
range(1, 70) creates a sequence of numbers from 1 to 69 (but doesn't include 70).
5 is the number of items to randomly select from the sequence.
Generating Powerball number:
random.randint(1, 26): This line generates a random integer between 1 and 26 (inclusive) using random.randint(). This is the Powerball number.
Sorting (optional):
numbers.sort(): This line sorts the regular numbers in ascending order using the sort() method. You can remove this line if you don't care about the order.
Returning results:
The function returns a tuple containing two elements:
The list of 5 regular winning numbers.
The single Powerball winning number.
Calling the function:
winning_numbers, powerball_number = generate_powerball_numbers(): We call the generate_powerball_numbers() function and store the returned results (numbers and Powerball) in two separate variables.
Printing results:
We use print() statements to display the winning numbers in a user-friendly format, separating the regular numbers and the Powerball number.
