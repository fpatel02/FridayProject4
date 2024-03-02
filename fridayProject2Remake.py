import random

def generate_powerball_numbers():
  """Generates 5 random numbers (1-69) and 1 random Powerball number (1-26) for a Powerball lottery entry"""

  # Generate 5 random numbers between 1 and 69 (inclusive)
  numbers = random.sample(range(1, 70), 5)

  # Generate 1 random Powerball number between 1 and 26 (inclusive)
  powerball = random.randint(1, 26)

  # Sort the regular numbers in ascending order (optional, but some players prefer it this way)
  numbers.sort()

  # Return the list of winning numbers
  return numbers, powerball

# Get the winning numbers
winning_numbers, powerball_number = generate_powerball_numbers()

# Print the winning numbers in a user-friendly format
print("Winning numbers:", winning_numbers)
print("Powerball number:", powerball_number)
