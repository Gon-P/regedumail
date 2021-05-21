import colorama
import random
import sys

def bannerTop():
    banner = '''
       _ _    _ _______ _____  _____  ____  _   _ 
      | | |  | |__   __/ ____|/ ____|/ __ \| \ | |
      | | |  | |  | | | (___ | |  __| |  | |  \| |
  _   | | |  | |  | |  \___ \| | |_ | |  | | . ` |
 | |__| | |__| |  | |  ____) | |__| | |__| | |\  |
  \____/ \____/   |_| |_____/ \_____|\____/|_| \_|
                                                  
'''

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]

    return ''.join(colored_chars)