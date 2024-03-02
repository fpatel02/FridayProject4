# FridayProject4

fridayProject4 has the objective of recreating Friday projects 1-3 with the help of generative AI. The steps of the code for Friday Project 1 are as follows:

    Part 1:
        import random: We import the random module. This will help add some fun by randomly choosing words later.
        def play_madlibs(): This defines a function called play_madlibs() where our game logic will live.
        if name == "main": This ensures that the play_madlibs() function runs only when you directly execute this script.
    Part 2:
        story_template: This variable stores your Mad Libs story. Use placeholders like {adjective1}, {noun}, etc., for the words that the player will fill in. Feel free to get creative with your story!
    Part 3:
        We use the input() function to get words from the player. Each type of word (adjective, noun, verb) gets its own variable.
    Part 4:
        .format(): This powerful string method replaces the placeholders in the story_template with the actual words provided by the player.
    Part 5:
        We use lists, dictionaries, and the random.choice() to have the program randomly select words the the player has input.

The steps of the code for Friday Project 2 are as follows:

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
    Print feedback:
        We display a message based on whether the answer was correct.
    Print answer (for demonstration, remove in a real quiz bowl):
        We print the actual answer from the question list (for demonstration purposes). This should be removed in a real quiz bowl setting.
    End message: We thank the user for playing.