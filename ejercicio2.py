"""
Raul Jimenez
Bryann Alfaro
Donaldo Garcia
"""
import random


def evaluate_token(token, isEven):
    """
    Funcion que evalua el token
    """
    if token == 10 and isEven:
      return False
    elif token == 11 and not isEven:
      return False
    elif token % 2 == 0 and isEven:
      return True
    elif token % 2 != 0 and not isEven:
      return True
    else:
      return False

funds = 100
wager = 5
total_games = 1000

for _ in range(total_games):
    token = random.randint(1, 100)
    isEven = random.choice([True, False])

    if evaluate_token(token, isEven):
        funds += wager
    else:
        funds -= wager

print(f"Funds: {funds}")

# task 1: la probabilidad de que gane la casa es de 52%

