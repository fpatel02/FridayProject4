import random

def madlibs():
    """The main function to play MadLibs"""

    # Create lists of different word types
    adjectives = ["silly", "gigantic", "smelly", "bright", "noisy"]
    nouns = ["dog", "house", "tree", "banana", "car"]
    verbs = ["ran", "jumped", "shouted", "laughed", "exploded"]

    # Get player input for different story elements
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    number = input("Enter a number: ")

    # Build the story with random word choices
    story = f"{name} went to the {random.choice(adjectives)} {random.choice(nouns)} in {place}.\n" \
            f"They saw {number} {random.choice(nouns)} and {random.choice(verbs)} loudly!"

    # Print the complete MadLibs story
    print(story)

# Start the game!
if __name__ == "__main__":
    madlibs() 