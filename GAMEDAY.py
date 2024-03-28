from SIM_GAMESTATE import *
from SIM_TEAM import *
from SIM_PLAYBOOK import *
from SIM_FUNCTIONS import *
from SIM_BOXSCORE import *
from SIM_TIME import *
from SIM_PLAY_EXEC import *

def simulate_game():
    # Initialize teams and game state
    home_team = Team("CHI")
    away_team = Team("MIA")
    game_state = GameState(home_team, away_team)
    game_time = Time(game_state=game_state)
    game_state.time = game_time
    print()
    game_state.coin_toss()
    exec = Execute(game_state)
    scoreboard = Scoreboard(game_state)
    scoreboard.scoreboard()
    exec.execute_kickoff()

        # Main simulation loop
    while game_state.time.quarter <= 4:
        scoreboard.scoreboard()
        game_state.time.handle_user_input()
        
        if game_state.time.isTimeoutCalled:
            scoreboard.scoreboard()
            game_state.time.isTimeoutCalled = False

        exec.execute_play()   

        if game_state.isTouchdown:
            scoreboard.scoreboard()
            exec.execute_extrapt()
            game_state.isTouchdown = False
            scoreboard.scoreboard()
            exec.execute_kickoff()
        
        if game_state.isFieldGoal:
            game_state.isFieldGoal = False
            scoreboard.scoreboard()
            exec.execute_kickoff()

        if game_state.isSafety:
            game_state.isSafety = False
            scoreboard.scoreboard()
            exec.execute_kickoff()

        # Handle the two-minute warning
        if game_state.time.quarter in [2, 4]:
            if game_state.time.qtr_len <= 120 and not game_state.time.isTwoMinWarning:
                scoreboard.scoreboard()
                game_state.time.two_minute_warning()
            elif game_state.time.isClockRunning and 120 < game_state.time.qtr_len <= 160:
                scoreboard.scoreboard()
                game_state.time.two_minute_decision()
                if game_state.time.isTwoMinWarning:
                    scoreboard.scoreboard()
                    game_state.time.two_minute_warning()
                else:
                    game_state.time.handle_user_input()
                    if game_state.time.isTimeoutCalled:
                        scoreboard.scoreboard()  # Consider if this is necessary again so soon
                        game_state.time.isTimeoutCalled = False
                    else:
                        exec.execute_play()

        # Check if the quarter should end due to time running out or a decision made
        if game_state.time.qtr_len <= 0 or game_state.time.isEndQuarter:
            game_state.time.qtr_len = max(0, game_state.time.qtr_len)  # Ensure time does not go negative
            scoreboard.scoreboard()
            game_state.display_stats()
            scoreboard.quarter_score()
            game_state.time.reset_quarter()  # Resets quarter, possibly setting isEndQuarter to False internally
        else:
            # Loop for handling the last 40 seconds of the quarter
            while game_state.time.qtr_len > 0 and game_state.time.isClockRunning:
                # Display the current game state
                scoreboard.scoreboard()
                
                # Make a decision for the quarter, potentially updating game state and time
                game_state.time.quarter_decision()
                
                # Check if the decision leads to the end of the quarter
                if game_state.time.isEndQuarter:
                    scoreboard.scoreboard()
                    game_state.display_stats()
                    scoreboard.quarter_score()
                    game_state.time.reset_quarter()
                    break  # Exit the loop as the quarter ends
                else:
                    # Handle actions based on user input or game logic
                    game_state.time.handle_user_input()
                    
                    if game_state.time.isTimeoutCalled:
                        # Display the scoreboard if a timeout is called
                        scoreboard.scoreboard()
                        game_state.time.isTimeoutCalled = False  # Reset the timeout flag
                    else:
                        # Execute a play, assuming it adjusts the game clock accordingly
                        exec.execute_play()
                        
                        # Immediately check and adjust for quarter end if time runs out after a play
                        if game_state.time.qtr_len <= 0:
                            game_state.time.qtr_len = 0  # Ensure time does not go negative
                            scoreboard.scoreboard()
                            game_state.display_stats()
                            scoreboard.quarter_score()
                            game_state.time.reset_quarter()
                            break  # Exit the loop as the quarter ends

                    # Ensure the quarter length is never negative after any operation
                    game_state.time.qtr_len = max(0, game_state.time.qtr_len)

        # Additional checks or logic can be placed here if needed for transitioning between quarters or other game states
           
        if game_state.time.quarter == 2: # Check if it's halftime
            game_state.time.halftime()  # Perform halftime activities, including quarter change
            game_state.time.second_half()
            scoreboard.scoreboard()
            exec.execute_kickoff()

        if game_state.time.quarter > 4:
            SimFunctions.scroll_print("THATS THE END OF THE GAME.")
            if game_state.home_team.score > game_state.away_team.score:
                SimFunctions.scroll_print(f'{game_state.home_team.abbreviation} DEFEATS {game_state.away_team.abbreviation}')
            else:
                SimFunctions.scroll_print(f'{game_state.away_team.abbreviation} DEFEATS {game_state.home_team.abbreviation}')

            game_state.display_stats()
            game_state.boxscore.display_box_score()
            break

if __name__ == "__main__":
    simulate_game()
