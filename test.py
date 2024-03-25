import sys
import time

def print_loading_dots(word, duration=2, interval=1):
  end_time = time.time() + duration
  sys.stdout.write(word)
  while time.time() < end_time:
    sys.stdout.write(".")
    sys.stdout.flush()  # Make sure the dot is immediately printed to the terminal
    time.sleep(interval)
print()  # Print a newline character to move to the next line


print_loading_dots("LOADING")