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

The steps of the code for Friday Project 3 are as follows:
    import random: We import the random module to randomly select questions.

Sample questions:

We define a dictionary named questions to store tossup and bonus questions.
You can expand these dictionaries with more questions and categories.
Difficulty levels (optional):

We define a list difficulty_levels (commented out) to add difficulty options.
You can modify this to adjust question selection based on difficulty.
Welcome message: We print a welcome message to the user.

Difficulty selection (optional): (Commented out)

We prompt the user to choose a difficulty level using input().
You can add logic to select questions based on the chosen difficulty.
Random question type:

We convert the questions dictionary keys to a list using list(questions.keys()).
We use random.choice() to pick a random question type ("tossup" or "bonus").
Random question selection:

We access the chosen question type in the questions dictionary.
We use random.choice() again to pick a random question from that list.
Print the question:

We format the output using f-strings to display the question type and the actual question.
User answer:

We use input() to get the user's answer.
Simple answer check (replace with more robust logic):

We perform a basic check for a specific answer ("Paris" for the tossup example).
In a real quiz bowl, you'd need a more sophisticated answer checking system.
Print feedback:
We display a message based on whether the answer was correct.
Print answer (for demonstration, remove in a real quiz bowl):
We print the actual answer from the question list (for demonstration purposes). This should be removed in a real quiz bowl setting.
End message: We thank the user for playing.