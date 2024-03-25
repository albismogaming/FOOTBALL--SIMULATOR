import time
import sys
import os
import string
import numpy as np
import threading

class SimFunctions:
    @staticmethod
    def scroll_print(word, delay=0.0001):
        alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + string.whitespace
        accumulated_output = ""  # String to accumulate the output
        for char in word:
            if char not in alphabet:
                accumulated_output += char  # Add non-alphabet characters directly
            else:
                for letter in alphabet:
                    print(accumulated_output + letter, end='\r', flush=True)
                    time.sleep(delay)
                    if letter.lower() == char.lower():
                        accumulated_output += char  # Add the correct alphabet character
                        break
            time.sleep(delay)  # Short pause after each character
            sys.stdout.flush()

        print(accumulated_output)  # Print the final word

    def print_loading_dots(word, duration=2, interval=1):
        end_time = time.time() + duration
        sys.stdout.write(word)
        while time.time() < end_time:
            sys.stdout.write(".")
            sys.stdout.flush()  # Make sure the dot is immediately printed to the terminal
            time.sleep(interval)
        print()  # Print a newline character to move to the next line

    def play_choice():
        play_choice = input('CHOOSE A PLAY: ').lower().strip()
        return play_choice
    
    def pat_choice():
        play_choice = input('PAT ATTEMPT: ').lower().strip()
        return play_choice
    
    def kickoff_choice():
        play_choice = input("TYPE KICKOFF TO COMMENCE THE GAME!: ").lower().strip()
        return play_choice

    def ordinal(n):
        return "%d%s" % (n,"TSNRHTDD"[(n//10%10!=1)*(n%10<4)*n%10::4])

    def time_format(secs):
        mins = int(secs // 60)
        rem_secs = int(secs % 60)
        formatted = f'{mins:02d}:{rem_secs:02d}'
        return formatted
    
    def wait():
        time.sleep(0.1)

    def game_intro():
        print("Press Enter to skip the intro or wait for it to finish...")

        # Define the intro text
        intro_text = """Welcome, sports fans, to today's highly anticipated matchup in our simulation league! The teams have been preparing all season for this moment, and the energy in the stadium is electric. Fans from both sides are filling the stands, the anticipation building with every passing second. Today's game features a showdown between two of the league's top teams, each boasting a roster filled with talent and determination. Will the home team leverage their field advantage and passionate supporters to claim victory, or will the visiting team execute their strategy flawlessly and silence the crowd? The players are lining up, the referees are ready, and the whole season comes down to this. It's time for the kickoff! So grab your snacks, settle in, and get ready for an unforgettable game filled with thrilling plays, incredible athleticism, and moments that will be talked about for years to come."""

        # Start scrolling text in a separate thread
        thread = threading.Thread(target=SimFunctions.scroll_print(), args=(intro_text,))
        thread.start()

        try:
            # For Windows, use msvcrt.getch()
            import msvcrt
            while thread.is_alive():
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b'\r':  # Enter key is pressed
                        print("\nSkipping intro. Let's jump straight into the action!")
                        return
        except ImportError:
            # For Unix-like systems, use input() as a fallback
            input()  # Pressing Enter will skip the intro
            if thread.is_alive():
                print("\nSkipping intro. Let's jump straight into the action!")
                return

        thread.join() 