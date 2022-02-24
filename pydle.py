from src.grid import draw_grid
from src.parse import get_word

word = get_word()
amount = 6

draw_grid(word)

while amount != 0:
    guess = input().lower()
    draw_grid(word, True)

    while len(guess) != len(word):
        guess = input().lower()
        draw_grid(word, True)

    amount = amount - 1

    if guess == word:
        print('You won!')
        exit()

print(f'You lose.\nThe word was {word}')