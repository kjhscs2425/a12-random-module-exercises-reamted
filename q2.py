# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = random.choice(["cat", "dog", "rat", "human", "girrafe", "tiger", "mouse","seal", "eal", "fish", "shark", "amarica", "bison",])
# Age (integer)
age = random.randint(1, 245)
# Color (at least 3 choices, string)
color = random.choice(["red", "green", "yellow", "blue", "purple", "ornage", "teal", "black", "white", "brown", "the fitness gram pacer test"])
# Weight (float)
weight = random.uniform(1, 1000)

# Print a summary of your pet using an f-string
print(f"Your pet is a {animal}, and {age} years old. its color is {color}, and it weighs {weight} pounds")