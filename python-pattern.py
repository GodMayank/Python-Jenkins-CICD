import time
import sys

def print_moving_spiral(rows):
    while True:
        spaces = rows - 1
        for i in range(rows):
            sys.stdout.write(' ' * spaces + '*' * (2 * i + 1) + '\n')
            sys.stdout.flush()
            time.sleep(0.1)
            spaces -= 1

        spaces = 0
        for i in range(rows - 1, -1, -1):
            sys.stdout.write(' ' * spaces + '*' * (2 * i + 1) + '\n')
            sys.stdout.flush()
            time.sleep(0.1)
            spaces += 1

        time.sleep(0.5)  # Pause before restarting the pattern

print_moving_spiral(10)
