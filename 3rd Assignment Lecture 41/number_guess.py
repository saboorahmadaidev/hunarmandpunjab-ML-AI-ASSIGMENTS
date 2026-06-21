# Number Guessing Game
import random
num = random.randint(1, 50)
attempts = 0
while True:
    guess = int(input('Guess a number 1-50: '))
    attempts += 1
    if guess == num:
        print('Correct! Attempts:', attempts)
        break
    elif guess < num:
        print('Higher')
    else:
        print('Lower')
