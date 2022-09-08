'''count down inputed time'''

from time import sleep
from ascii_numbers import ascii_gen


def countdown(n: int):
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    for time in range(n, 0, -1):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        ascii_gen(time)
        sleep(1)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print("COUNTDOWN FINISHED!")



print('\n')
timer = int(input('Enter length of countdown: '))
countdown(timer)
