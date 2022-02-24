import os
from typing import Optional

def draw_grid(word: str, clear: Optional[bool] = None):
    if clear:
        os.system('cls||clear')

    print('Pydle\nWordle, but Python\n')
    
    for i in range(6):
        print('\u2B1C' * len(word))
    print('\n')