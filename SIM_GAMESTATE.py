# DEFINES THE GAMESTATE FOR THE SIMULATION
import numpy as np
from termcolor import colored
from SIM_FUNCTIONS import *
from SIM_PLAYBOOK import *
from SIM_SCOREBOARD import *
from SIM_BOXSCORE import *
from SIM_TIME import *

class GameState:
    def __init__(self, home_team, away_team):
        self.station = 'FOX'
        self.home_team = home_team
        self.home_plays = 0
        self.home_comps = 0
        self.home_incomps = 0

        self.away_team = away_team
        self.away_plays = 0
        self.away_comps = 0
        self.away_incomps = 0

        self.boxscore = BoxScore(home_team, away_team)
        self.isCoinTossWinner = None
        self.isCoinTossLoser = None
        self.isKicking = None
        self.isReceiving = None
        self.possession = None

        self.down = 1
        self.yds_fd = 10
        self.yardline = 35

        self.time = Time(game_state=any)
        self.isTouchdown = False
        self.isFieldGoal = False
        self.isSafety = False

        self.drive_time = 0
        self.drive_plays = 0
        self.drive_yards = int(0)

    def coin_toss(self):
        # Introduce the coin toss phase with a bit of flair
        SimFunctions.scroll_print("WELCOME TO MID-FIELD FOR THE COIN TOSS!")
        SimFunctions.scroll_print(f"{self.away_team} YOU ARE THE VISTING TEAM, YOU WILL CALL THE TOSS.")

        # Capture the away team's call
        print()
        selection = input("CALL IT IN THE AIR -- (HEADS/TAILS)?: ").lower().strip()
        while selection not in ['heads', 'tails']:
            print("Please choose 'Heads' or 'Tails'.")
            selection = input("CALL IT IN THE AIR -- (HEADS/TAILS)?: ").lower().strip()

        # Simulate the coin toss
        result = np.random.choice(['heads', 'tails'])
        SimFunctions.scroll_print(f"THE COIN IS IN THE AIR....AND IT IS {result.upper()}!")

        # Determine the winner of the coin toss
        if result == selection:
            self.isCoinTossWinner = self.away_team
            self.isCoinTossLoser = self.home_team
        else:
            self.isCoinTossWinner = self.home_team
            self.isCoinTossLoser = self.away_team

        # Announce the winner and their choice
        print()
        SimFunctions.scroll_print(f"{self.isCoinTossWinner} WINS THE TOSS!")
        decision = input(f"{self.isCoinTossWinner}, YOU HAVE THE OPTION TO KICK OR RECEIVE -- (KICK/RECEIVE)?: ").lower().strip()
        while decision not in ['kick', 'receive']:
            print("Invalid choice. Please type 'kick' or 'receive'.")
            decision = input(f"{self.isCoinTossWinner}, YOU HAVE THE OPTION TO KICK OR RECEIVE -- (KICK/RECEIVE)?: ").lower().strip()

        if decision == "receive":
            self.isReceiving = self.isCoinTossWinner
            self.isKicking = self.isCoinTossLoser
            SimFunctions.scroll_print(f"{self.isReceiving} HAS ELECTED TO KICKOFF.")
        else:
            self.isReceiving = self.isCoinTossLoser
            self.isKicking = self.isCoinTossWinner
            self.possession = self.isKicking
            SimFunctions.scroll_print(f"{self.isReceiving} WILL RECEIVE THE BALL.")

        # Optional: Briefly pause before moving on to kickoff
        print()
        SimFunctions.scroll_print("SHAKE HANDS AND GOOD LUCK TO BOTH TEAMS!")
        SimFunctions.scroll_print("LETS GET READY FOR KICKOFF!")
        print()
        self.time.stop_clock()

    def update_play(self, yards_gained, play_clock_used, play_choice, interception=False, incompletion=False, sptm_result=None):
        self.time.update_game_clock(play_choice=play_choice, play_clock_used=play_clock_used)

        if play_choice in ['kickoff']:
            if sptm_result == "TOUCHBACK":
                self.change_possession()
                self.yardline = 25
                self.time.qtr_len -= 0
                self.time.stop_clock()
            elif sptm_result == "RET TD":
                self.score_touchdown(self.isReceiving)
                self.time.qtr_len -= np.random.randint(9,16)
                self.time.stop_clock()
            elif sptm_result == "RETURNED":
                self.change_possession()
                self.time.qtr_len -= np.random.randint(4,9)
                self.time.stop_clock()

        if interception:
            if self.yardline + yards_gained >= 100:
                SimFunctions.scroll_print("INTERCEPTED!")
                SimFunctions.scroll_print("---  TOUCHBACK  ---")
                self.reset_drive_summary()
                self.change_possession()
                self.yardline = 20
                self.time.stop_clock()
            else:
                SimFunctions.scroll_print("INTERCEPTED!")
                self.yardline += yards_gained
                self.reset_drive_summary()
                self.change_turnover()
                self.time.stop_clock()
        
        elif incompletion:
            self.down += 1
            self.drive_plays += 1
            self.time.stop_clock()
            if self.down > 4:
                    SimFunctions.scroll_print("TURNOVER ON DOWNS!")
                    self.reset_drive_summary()
                    self.change_turnover()
                    self.time.stop_clock()

        # Handle regular plays
        elif play_choice in ['run', 'short pass', 'medium pass', 'deep pass', 'bomb pass']:
            self.yardline += yards_gained
            self.drive_plays += 1
            self.drive_yards += yards_gained
            # Check for scoring or turnovers
            if self.yardline >= 100:
                self.score_touchdown(self.possession)
                self.time.stop_clock()

            elif self.yardline <= 0:
                self.score_safety(self.possession)
                self.time.stop_clock()
            elif yards_gained >= self.yds_fd or self.yds_fd <= 0:
                self.down = 1
                self.yds_fd = 10
                SimFunctions.scroll_print("FIRST DOWN!")
            else:
                self.down += 1
                self.yds_fd -= yards_gained
                if self.down > 4:
                    SimFunctions.scroll_print("TURNOVER ON DOWNS!")
                    self.reset_drive_summary()
                    self.change_turnover()
                    self.time.stop_clock()

        elif play_choice in ['punt', 'field goal', 'extra point']:
            if play_choice == 'punt':
                if sptm_result == "TOUCHBACK":
                    self.reset_drive_summary()
                    self.change_possession()
                    self.yardline = 20
                    self.time.stop_clock()
                elif sptm_result == "RET TD":
                    # Correctly award the touchdown to the team that returned the punt
                    scoring_team = self.away_team if self.possession == self.home_team else self.home_team
                    self.return_touchdown(scoring_team)
                    self.time.stop_clock()
                elif sptm_result in ['BLOCKED', 'OB', 'DN', 'FC', 'RT']:
                    self.reset_drive_summary()
                    self.change_turnover()
                    self.time.stop_clock()

            # Handle 'field goal' and 'extra point' outcomes
            elif play_choice == 'field goal' and sptm_result == "NO GOOD":
                self.reset_drive_summary()
                self.change_turnover()
                self.time.stop_clock()
            elif play_choice == 'field goal' and sptm_result == "GOOD":
                self.score_field_goal(self.possession)
                self.yardline = 35
                self.time.stop_clock()

            elif play_choice == 'extra point' and sptm_result == "NO GOOD":
                self.display_drive_summary()
                self.reset_drive_summary()
                self.yardline = 35
                self.time.stop_clock()
            elif play_choice == 'extra point' and sptm_result == "GOOD":
                self.score_extra_point(self.possession)
                self.yardline = 35
                self.time.stop_clock()

    def distance_to_goal(self):
        distance_to_goal = 118 - self.yardline
        return distance_to_goal

    def change_possession(self):
        self.down = 1
        self.yds_fd = 10
        self.time_pos = 0
        self.plays_pos = 0
        self.possession = self.home_team if self.possession == self.away_team else self.away_team

    def change_turnover(self):
        self.down = 1
        self.yds_fd = 10
        self.yardline = 100 - self.yardline
        self.time_pos = 0
        self.plays_pos = 0
        self.possession = self.home_team if self.possession == self.away_team else self.away_team    

    def score_touchdown(self, team):
        if team == self.home_team or team == self.away_team:
            self.isTouchdown = True
            team.add_points(6)
            self.boxscore.update_score(team, 6, self.time.quarter) 
            SimFunctions.scroll_print(f"{team} TOUCHDOWN!!!!")
    
    def return_touchdown(self, scoring_team):
            self.possession = scoring_team
            self.isTouchdown = True
            scoring_team.add_points(6)
            self.boxscore.update_score(scoring_team, 6, self.time.quarter) 
            SimFunctions.scroll_print(f"{scoring_team} TOUCHDOWN!!!!")

    def score_field_goal(self, team):
        if team == self.home_team or team == self.away_team:
            self.isFieldGoal = True
            team.add_points(3)
            self.boxscore.update_score(team, 3, self.time.quarter) 
            SimFunctions.scroll_print(f"{team} FIELD GOAL!!!!")
            self.display_drive_summary()
            self.reset_drive_summary()

    def score_extra_point(self, team):
        if team == self.home_team or team == self.away_team:
            team.add_points(1)
            self.boxscore.update_score(team, 1, self.time.quarter) 
            SimFunctions.scroll_print(f"{team} EXTRA POINT!!!!")
            self.display_drive_summary()
            self.reset_drive_summary()

    def score_safety(self, defensive_team):
        # Determine which team is on defense (not currently in possession) and award them 2 points
        defensive_team = self.away_team if self.possession == self.home_team else self.home_team
        self.isSafety = True
        defensive_team.add_points(2)
        self.boxscore.update_score(defensive_team, 2, self.time.quarter)
        SimFunctions.scroll_print(f"{defensive_team} SAFETY!!!!")
        # Change possession to the defensive team (which just scored)
        self.change_possession()

    def display_stats(self):
        home_pass_att = (self.home_comps + self.home_incomps)
        home_comp_pct = np.round(self.home_comps / home_pass_att, 3) if home_pass_att > 0 else 0

        away_pass_att = (self.away_comps + self.away_incomps)
        away_comp_pct = np.round(self.away_comps / away_pass_att, 3) if home_pass_att > 0 else 0

        print()
        print(f'{self.home_team} PLAYS: {self.home_plays}')
        print(f'{self.home_comps} / {home_pass_att}')
        print(f'{self.home_team} COMP%: {home_comp_pct}')
        print()
        print(f'{self.away_team} PLAYS: {self.away_plays}')
        print(f'{self.away_comps} / {away_pass_att}')
        print(f'{self.away_team} COMP%: {away_comp_pct}')
        print()
    
    def reset_drive_summary(self):
        self.drive_time = 0
        self.drive_plays = 0
        self.drive_yards = 0
    
    def display_drive_summary(self):
        plays = colored(self.drive_plays, 'white', attrs=['bold'])
        yards = colored(self.drive_yards, 'white', attrs=['bold'])
        times = colored(SimFunctions.time_format(self.drive_time), 'white', attrs=['bold'])

        print(f"""
{colored(f'======================', 'white', attrs=['bold'])}
--  DRIVE  SUMMARY  --
 PLAYS   YARDS   TIME                
  {plays:2}     {yards:2}     {times:4} 
{colored(f'======================', 'white', attrs=['bold'])}""")
