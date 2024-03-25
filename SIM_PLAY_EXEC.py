import numpy as np
import sys
import os
from scipy.stats import norm
from SIM_FUNCTIONS import *
from SIM_TIME import *
from SIM_PLAYBOOK import *

class Execute:
    def __init__(self, game_state):
        self.game_state = game_state
        self.play = Play(game_state)
        
    def execute_play(self):
        play_clock_used = self.game_state.time.offensive_tempo() if self.game_state.time.isClockRunning else 0
        play_choice = SimFunctions.play_choice()

        interception = False
        incompletion = False

        method_name = play_choice.replace(" ", "_")
        play_method = getattr(self.play, method_name, None)

        if play_choice in ['short pass', 'medium pass', 'deep pass', 'bomb pass']:
            play_result = play_method()
            if isinstance(play_result, tuple):
                yards_gained, interception, incompletion = play_result
            else:
                yards_gained = play_result  # Assume it only returns yards gained
            self.game_state.update_play(yards_gained, play_clock_used, play_choice, interception, incompletion)

            if self.game_state.possession == self.game_state.home_team and self.game_state.down <= 4:
                if incompletion == False:
                    self.game_state.home_comps += 1
                else:
                    self.game_state.home_incomps += 1
            else:
                if incompletion == False:
                    self.game_state.away_comps += 1
                else:
                    self.game_state.away_incomps += 1
            
            if self.game_state.possession == self.game_state.home_team:
                self.game_state.home_plays += 1
            else:
                self.game_state.away_plays += 1

        elif play_choice in ['run']:
            play_result = play_method()
            if isinstance(play_result, tuple):
                yards_gained, interception, incompletion = play_result
            else:
                yards_gained = play_result  # Assume it only returns yards gained
            self.game_state.update_play(yards_gained, play_clock_used, play_choice, interception, incompletion)
                
            if self.game_state.possession == self.game_state.home_team:
                self.game_state.home_plays += 1
            else:
                self.game_state.away_plays += 1    

        elif play_choice in ['punt', 'field goal']:
            sptm_result = play_method()
            if isinstance(sptm_result, tuple):
                yards_gained, sptm_result = sptm_result
            else:
                yards_gained = sptm_result
            self.game_state.update_play(yards_gained, play_clock_used, play_choice, False, False, sptm_result)

    def execute_extrapt(self):
        play_choice = SimFunctions.pat_choice()
        if play_choice == 'extra point':
            sptm_result = self.play.extra_point()
            self.game_state.update_play(0, 0, play_choice, False, False, sptm_result)
        else:
            self.execute_extrapt()

    def execute_kickoff(self):
        print("Executing kickoff...")
        play_choice = SimFunctions.kickoff_choice()
        print(f"Play choice: {play_choice}")
        if play_choice == "kickoff":
            yards_gained, sptm_result = self.play.kickoff()
            print(f"Kickoff result: yards_gained={yards_gained}, sptm_result={sptm_result}")
            self.game_state.update_play(0, 0, play_choice, False, False, sptm_result)
        else:
            print(f"Invalid choice: '{play_choice}'")
            self.execute_kickoff()


