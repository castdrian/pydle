from src.grid import draw_blank_grid, update_grid
from src.parse import await_input, get_word
from colorama import init

word = get_word().lower()
amount = 6
guess_list = []

init(autoreset = True)
draw_blank_grid(word)

while amount != 0:
    guess = await_input(word).lower()
    amount = amount - 1
    guess_list.append(guess)

    if guess == word:
        print('You won!')
        exit()

    update_grid(word, guess_list, amount)

print(f'You lose!\nThe word was {word}')
exit()