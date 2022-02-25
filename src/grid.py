import os
from colorama import Fore
from tabulate import tabulate

def draw_blank_grid(word: str):
    os.system('cls||clear')
    print('Pydle\nWordle, but Python\n')
    
    grid_data = []
    column_data = []

    for x in range(len(word)): column_data.append('?')
    for y in range(6): grid_data.append(column_data)

    print(tabulate(grid_data, tablefmt = 'fancy_grid'))


def update_grid(word: str, guess_list: list[str], amt: int):
    os.system('cls||clear')
    print('Pydle\nWordle, but Python\n')

    current_guess = guess_list[len(guess_list) - 1]
    grid_data = []
    column_data = []

    for x in range(len(word)): column_data.append('?')
    for y in range(6): grid_data.append(column_data)

    for idx, val in enumerate(guess_list):
        word_data = [char for char in val]
        grid_data[idx] = word_data

    print(tabulate(grid_data, tablefmt = 'fancy_grid'))



    """ if len(guess_list) == 1:
        if current_guess == word:
            
            word_data = []

            for char in word: word_data.append(f'{Fore.GREEN}{char}{Fore.RESET}')
            
            grid_data[len(guess_list) - 1] = word_data
            print(tabulate(grid_data, tablefmt = 'fancy_grid'))
            print('You won!')
            exit() """

