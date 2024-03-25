from SIM_FUNCTIONS import *
from SIM_TIME import *
from termcolor import colored

class Scoreboard:
    def __init__(self, game_state):
        self.game_state = game_state

    def scoreboard(self):
        pos_home = colored(f' {self.game_state.home_team.abbreviation:3}  {self.game_state.home_team.score:2} ', 'white', 'on_light_blue', attrs=['bold']) if self.game_state.possession == self.game_state.home_team else colored(f' {self.game_state.home_team.abbreviation:3}  {self.game_state.home_team.score:2} ', 'white', 'on_black', attrs=['bold'])
        home = colored(f'{pos_home}')

        pos_away = colored(f' {self.game_state.away_team.abbreviation:3}  {self.game_state.away_team.score:2} ', 'white', 'on_light_blue', attrs=['bold']) if self.game_state.possession == self.game_state.away_team else colored(f' {self.game_state.away_team.abbreviation:3}  {self.game_state.away_team.score:2} ', 'white', 'on_black', attrs=['bold'])
        away = colored(f'{pos_away}')
        
        station = colored(f' {self.game_state.station:3} ', 'black', 'on_white', attrs=['bold'])
        quarter = colored(f' {SimFunctions.ordinal(self.game_state.time.quarter):3} ', 'yellow', 'on_black', attrs=['bold'])
        game_clock = colored(f' {SimFunctions.time_format(self.game_state.time.qtr_len):4} ', 'white', 'on_black', attrs=['bold']) if self.game_state.time.qtr_len > 120 else colored(f' {SimFunctions.time_format(self.game_state.time.qtr_len)} ', 'white', 'on_red', attrs=['bold'])
        play_clock = colored(f' {self.game_state.time.play_clock:2} ', 'yellow', 'on_black', attrs=['bold'])
        yard_line = int(self.game_state.yardline) if int(self.game_state.yardline) < 50 else 100 - int(self.game_state.yardline)

        if self.game_state.yardline < 50 and self.game_state.possession == self.game_state.home_team:
            field_side = colored(f' {self.game_state.home_team.abbreviation:3} {str(yard_line):2} ', 'white', 'on_yellow', attrs=['bold'])
        elif self.game_state.yardline < 80 and self.game_state.yardline > 50 and self.game_state.possession == self.game_state.home_team:
            field_side = colored(f' {self.game_state.away_team.abbreviation:3} {str(yard_line):2} ', 'white', 'on_yellow', attrs=['bold'])
        elif self.game_state.yardline < 50 and self.game_state.possession == self.game_state.away_team:
            field_side = colored(f' {self.game_state.away_team.abbreviation:3} {str(yard_line):2} ', 'white', 'on_yellow', attrs=['bold'])
        elif self.game_state.yardline < 80 and self.game_state.yardline > 50 and self.game_state.possession == self.game_state.away_team:
            field_side = colored(f' {self.game_state.home_team.abbreviation:3} {str(yard_line):2} ', 'white', 'on_yellow', attrs=['bold'])
        elif self.game_state.yardline == 50 and self.game_state.possession == self.game_state.home_team or self.game_state.away_team:
            field_side = colored(f' MID {str(yard_line):2} ', 'white', 'on_yellow', attrs=['bold'])

        if self.game_state.yardline >= 80 and self.game_state.possession == self.game_state.home_team:
            field_side = colored(f' {self.game_state.away_team.abbreviation:3} {str(yard_line):2} ', 'white', 'on_red', attrs=['bold'])
        elif self.game_state.yardline >= 80 and self.game_state.possession == self.game_state.away_team:
            field_side = colored(f' {self.game_state.home_team.abbreviation:3} {str(yard_line):2} ', 'white', 'on_red', attrs=['bold'])

        if self.game_state.down == 4:
            down_dist = colored(f' {SimFunctions.ordinal(self.game_state.down):3} & {int(self.game_state.yds_fd):2} ', 'white', 'on_red', attrs=['bold'])
        else:
            down_dist = colored(f' {SimFunctions.ordinal(self.game_state.down):3} & {int(self.game_state.yds_fd):2} ', 'yellow', 'on_black', attrs=['bold'])

        distance_to_goal = 100 - self.game_state.yardline
        if distance_to_goal <= 10 and self.game_state.down < 4:
            down_dist = colored(f' {SimFunctions.ordinal(self.game_state.down):3} & GL ', 'white', 'on_green', attrs=['bold'])
        elif distance_to_goal <= 10 and self.game_state.down == 4:
            down_dist = colored(f' {SimFunctions.ordinal(self.game_state.down):3} & GL ', 'white', 'on_red', attrs=['bold'])

        if self.game_state.isTouchdown:
            touchdown = colored(" --  TOUCHDOWN  -- ", 'white', 'on_yellow', attrs=['bold'])
            scoreboard = f"""
{colored(f'================================================================', 'white', attrs=['bold'])}
|{station}|{home}|{away}|{f'{quarter}{game_clock}{play_clock}'}|{touchdown}|
{colored(f'================================================================', 'white', attrs=['bold'])}  
    """
            print(scoreboard)
        
        elif self.game_state.time.isTimeoutCalled:
            timeout = colored(" --   TIMEOUT   -- ", 'black', 'on_light_yellow', attrs=['bold'])
            scoreboard = f"""
{colored(f'================================================================', 'white', attrs=['bold'])}
|{station}|{home}|{away}|{f'{quarter}{game_clock}{play_clock}'}|{timeout}|
{colored(f'================================================================', 'white', attrs=['bold'])}  
    """
            print(scoreboard)

        else:
            scoreboard = f"""
{colored(f'================================================================', 'white', attrs=['bold'])}
|{station}|{home}|{away}|{f'{quarter}{game_clock}{play_clock:2}'}|{down_dist} {field_side}|
{colored(f'================================================================', 'white', attrs=['bold'])}  
        """
            print(scoreboard)

    def quarter_score(self):
        home = colored(f' {self.game_state.home_team.abbreviation:3}  {self.game_state.home_team.score:2} ', 'black', 'on_light_grey', attrs=['bold'])
        away = colored(f' {self.game_state.away_team.abbreviation:3}  {self.game_state.away_team.score:2} ', 'black', 'on_light_grey', attrs=['bold'])
        qtr = colored(f' END OF {SimFunctions.ordinal(self.game_state.time.quarter):3} ', 'white', 'on_grey', attrs=['bold'])

        message = f"""
{colored("=" * 34, 'grey', attrs=['bold'])}
|{qtr}|{home}|{away}|
{colored("=" * 34, 'grey', attrs=['bold'])}
            """
        print()
        print(message)
        print()