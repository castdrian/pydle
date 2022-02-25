import os
from colorama import Back, Style
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

    if len(guess_list) == 1:
        if guess_list[0] == word:
            grid_data = []
            column_data = []
            word_data = [char for char in word]

            for x in range(len(word)): column_data.append('?')
            for y in range(6): grid_data.append(column_data)
            
            grid_data[len(guess_list) - 1] = word_data
            print(tabulate(grid_data, tablefmt = 'fancy_grid'))
            print('You won!')
            exit()


