import random

# Define some sample questions (tossup and bonus)
questions = {
    "tossup": [
        "What is the capital of France?",
        "Who painted the Mona Lisa?",
        "What is the tallest mountain in the world?"
    ],
    "bonus": [
        "Name three colors of the primary rainbow.",
        "What year did World War II begin?",
        "What is the chemical symbol for gold?"
    ]
}

# Define difficulty levels (optional)
difficulty_levels = ["Easy", "Medium", "Hard"]

# Welcome message
print("Welcome to the Python Quiz Bowl!")

# Get user input for difficulty (optional)
# difficulty_level = input("Choose a difficulty level (Easy, Medium, Hard): ")

# Randomly select a question type (tossup or bonus)
question_type = random.choice(list(questions.keys()))

# Randomly select a question from the chosen type
question = random.choice(questions[question_type])

# Print the question
print(f"{question_type.title()}: {question}")

# Get user answer (replace with actual answer checking logic for a real quiz bowl)
user_answer = input("Enter your answer: ")

# Simple answer check (replace with more robust logic)
if user_answer.lower() == "paris" and question_type == "tossup":
    print("Correct!")
else:
    print("Sorry, that's incorrect.")

# Print the answer (for demonstration purposes, remove in a real quiz bowl)
print(f"The answer is: {questions[question_type][0]}")  # Get first element (answer)

print("Thanks for playing!")