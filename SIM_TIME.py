import os
import sys
import time
import numpy as np
from termcolor import colored
from SIM_FUNCTIONS import *
from SIM_PLAY_EXEC import *

class Time:
    def __init__(self, game_state):
        self.game_state = game_state
        self.exec = Execute(game_state)
        self.qtr_len = 900
        self.play_clock = 40  # Default play clock time
        self.quarter = 1
        self.isClockRunning = False
        self.isEndQuarter = False
        self.isEndGame = False
        self.isTimeoutCalled = False
        self.isTwoMinWarning = False
        self.isHalftime = False

    def update_game_clock(self, play_choice, play_clock_used):
        total_time = self.play_duration(play_choice) + play_clock_used

        if self.isClockRunning and play_choice != 'kickoff':
            self.qtr_len -= play_clock_used  # Use the passed-in value
            self.qtr_len -= self.play_duration(play_choice)
            self.game_state.drive_time += play_clock_used + self.play_duration(play_choice)

        elif not self.isClockRunning and play_choice != 'kickoff':
            self.game_state.drive_time += self.play_duration(play_choice)
            self.qtr_len -= self.play_duration(play_choice)
            self.start_clock()

        elif play_choice == 'kickoff':
            self.qtr_len -= self.play_duration(play_choice)
            self.stop_clock()
        
        elif not self.isClockRunning or self.isClockRunning and total_time < 120 <= self.qtr_len:
            if not self.isTwoMinWarning:
                self.isTwoMinWarning = True

    def offensive_tempo(self):
        print(f"""
[  FAST ] [  TEMP ] [  NORM ] [ SLOW  ]
[ 10-15 ] [ 15-25 ] [ 25-35 ] [ 35-39 ] """)
        
        while True:
            tempo = input("CHOOSE TEMPO: ").lower().strip()
            if tempo == 'fast':
                return np.random.randint(10,15)
            elif tempo == 'temp':
                return np.random.randint(15,25)
            elif tempo == 'norm':
                return np.random.randint(25,35)
            elif tempo == 'slow':
                return np.random.randint(35,40)
            else:
                print("INVALID INPUT")

    def play_duration(self, play_choice):
        if play_choice == 'run':
            return np.random.randint(4, 10)
        elif play_choice == 'short pass':
            return np.random.randint(4, 10)
        elif play_choice == 'medium pass':
            return np.random.randint(6, 10)
        elif play_choice == 'deep pass':
            return np.random.randint(6, 10)
        elif play_choice == 'bomb pass':
            return np.random.randint(7, 10)
        elif play_choice == 'punt':
            return np.random.randint(7, 12)
        elif play_choice == 'field goal':
            return np.random.randint(5, 10)
        elif play_choice == 'extra point':
            return 0
        elif play_choice == 'kickoff':
            return 0

    def halftime(self):
        if self.quarter == 2 and self.qtr_len <= 0:
            if not self.game_state.isTouchdown:
                SimFunctions.scroll_print("--- HALFTIME ---")
                self.isHalftime = True
                self.game_state.home_team.timeouts = 3
                self.game_state.away_team.timeouts = 3
                self.second_half()
    
    def second_half(self):
        # Explicitly handle transitioning to the third quarter
        self.quarter = 3
        self.qtr_len = 900  # Reset the quarter length for the second half
        self.stop_clock()  # Ensure the clock is stopped at the start of the half
        SimFunctions.scroll_print("--- START OF 2ND HALF ---")
    
    def reset_quarter(self):
        if not self.game_state.isTouchdown:
            self.quarter += 1
            self.qtr_len = 900
            self.stop_clock()
    
    def end_game(self):
        self.isEndGame = self.quarter > 4
        SimFunctions.scroll_print("THATS THE END OF THE GAME.")

    def stop_clock(self):
        self.isClockRunning = False

    def start_clock(self):
        self.isClockRunning = True

    def two_minute_decision(self):
        decision = input("TAKE IT TO THE TWO MINUTE? (yes/no): ").strip().lower()
        while decision not in ["yes", "no"]:
            print("Invalid response. Please answer 'yes' or 'no'.")
            decision = input("TAKE IT TO THE TWO MINUTE? (yes/no): ").strip().lower()

        if decision == "yes":
            self.qtr_len = 120
            self.two_minute_warning()
        elif decision == "no":
            if self.isClockRunning and self.qtr_len < 135:
                chance_of_delay = np.random.rand()
                if chance_of_delay < 0.3:
                    SimFunctions.scroll_print(f"{self.game_state.possession} DIDN'T GET THE PLAY OFF IN TIME.")
                    self.qtr_len = max(120, self.qtr_len - 15)
                    self.two_minute_warning()
                else:
                    # Select a random play choice properly before decrementing `self.qtr_len`
                    pass

    def quarter_decision(self):
        # Check if quarter naturally ends
        if self.qtr_len <= 0:
            self.isEndQuarter = True
            self.reset_quarter()
            # Optionally, handle end-of-quarter logic here (e.g., switching sides, resetting certain states)

        decision = input("TAKE IT TO THE QUARTER? (yes/no): ").strip().lower()
        while decision not in ["yes", "no"]:
            print("Invalid response. Please answer 'yes' or 'no'.")
            decision = input("TAKE IT TO THE QUARTER? (yes/no): ").strip().lower()

        if decision == "yes":
            self.qtr_len = 0
            self.isEndQuarter = True
        elif decision == "no":
            if self.isClockRunning and self.qtr_len < 15:
                chance_of_delay = np.random.rand()
                if chance_of_delay < 0.3:  # Example probability
                    SimFunctions.scroll_print(f"{self.game_state.possession} DIDN'T GET THE PLAY OFF IN TIME.")
                    self.qtr_len = 0
                    self.isEndQuarter = True
                    self.reset_quarter()
                else:
                    # Assuming the existence of a method to execute the last play of the quarter
                    pass

    def two_minute_warning(self):
        SimFunctions.scroll_print("---  TWO MINUTE WARNING  ---")
        self.isTwoMinWarning = True
        self.stop_clock()

    def use_timeout(self, team):
        if team.timeouts > 0:
            self.isTimeoutCalled = True
            team.timeouts -= 1
            self.stop_clock()
            # Other timeout logic here (e.g., stop the clock)
            SimFunctions.scroll_print(f"{team} CALLS A TIMEOUT!")
            SimFunctions.scroll_print(f"TIMEOUTS REMAINING: {team.timeouts}")
            time.sleep(2)
        else:
            print(f"{team} HAS NO TIMEOUTS REMAINING!")
    
    def handle_user_input(self):
        user_input = input("1-HOME TIMEOUT, 2-AWAY TIMEOUT, ENTER TO CHOOSE PLAY: ")
        if user_input == '1':
            # Home team calls a timeout
            if self.game_state.home_team.timeouts > 0:
                self.use_timeout(self.game_state.home_team)
        elif user_input == '2':
            # Away team calls a timeout
            if self.game_state.away_team.timeouts > 0:
                self.use_timeout(self.game_state.away_team)
        else:
            pass
