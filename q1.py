import random


def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """
  #YOUR CODE HERE

  colors = random.choice(["red", "green", "yellow", "blue"])
  
  sides = random.choices(["left", "right"])

  appendage = random.choices(["hand", "foot"])
  return colors, sides, appendage
  

# Here's the function call. This should print a random assortment of twister commands
for sin_twister_spinner in range(10):

  print(spin_twister_spinner())