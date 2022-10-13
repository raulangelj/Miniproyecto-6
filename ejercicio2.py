"""
Raul Jimenez
Bryann Alfaro
Donaldo Garcia
"""
import random
import matplotlib.pyplot as plt
import matplotlib


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

def game(funds, wager, games, iterations):
    """
    Funcion que simula el juego
    """
    game = 1

    x_wager = []
    y_funds = []

    while game <= games:
        for _ in range(iterations):
            token = random.randint(1, 100)
            isEven = random.choice([True, False])

            if evaluate_token(token, isEven):
                funds += wager
            else:
                funds -= wager
            y_funds.append(funds)
            x_wager.append(game)
        game += 1
    print(f"Funds: {funds}")
    plt.plot(x_wager, y_funds)
    plt.ylabel('Dinero Total')
    plt.xlabel('Numero de apuestas')
    plt.show()


# task 1: la probabilidad de que gane la casa es de 52%

# task 3:
funds = 1000
wager = 10
# a.50 juegos, con 10 iteraciones
game(funds, wager, 50, 10)
print('========= FINISH GAME 1 ==========')
# b.50 juegos, con 1,000 iteraciones
game(funds, wager, 50, 1000)
print('========= FINISH GAME 2 ==========')
# c.10,000 juegos, con 10 iteraciones
game(funds, wager, 10000, 10)
print('========= FINISH GAME 3 ==========')