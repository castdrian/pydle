import os
from tabulate import tabulate
from src.logic import apply_colors

def draw_blank_grid(word: str):
    os.system('cls||clear')
    print('Pydle\nWordle, but Python\n')
    
    grid_data = []
    column_data = []

    for x in range(len(word)): column_data.append('?')
    for y in range(6): grid_data.append(column_data)

    print(tabulate(grid_data, tablefmt = 'fancy_grid'))


def update_grid(word: str, guess_list: list[str]):
    os.system('cls||clear')
    print('Pydle\nWordle, but Python\n')

    grid_data = []
    column_data = []

    for x in range(len(word)): column_data.append('?')
    for y in range(6): grid_data.append(column_data)

    for idx, val in enumerate(guess_list):
        word_data = apply_colors(word, val)
        grid_data[idx] = word_data

    print(tabulate(grid_data, tablefmt = 'fancy_grid'))

