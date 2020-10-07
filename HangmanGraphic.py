import re
hangman_image = """
1 2 2 2 2 2 2 2 2
1               3
1               3
1               4
1             4   4
1               4
1             8 5 9
1            8  5  9
1               5
1              6 7
1             6   7
1 1
1   1
1    1
1     1"""

def draw_hangman(failed_attempts):
    current_hangman = hangman_image
    current_hangman = re.sub('[1-{}]'.format(failed_attempts), '*', current_hangman)
    current_hangman = re.sub('[{}-9]'.format(failed_attempts + 1), ' ', current_hangman)
    print(current_hangman)