from rich.console import Console
from rich.table import Table

class BoxScore:
    def __init__(self, home_team, away_team):
        self.teams = [home_team, away_team]  # Store team names or identifiers
        self.scores = [[0, 0, 0, 0],  # Home team scores by quarter
                       [0, 0, 0, 0]]  # Away team scores by quarter

    def update_score(self, team_abbr, points, quarter):
        try:
            # Find the index of the team based on the abbreviation
            team_index = self.teams.index(team_abbr)
        except ValueError:
            print(f"Team {team_abbr} not found in boxscore.")
            return

        # Update the quarter score for the found team
        self.scores[team_index][quarter - 1] += points

    def display_box_score(self):
        console = Console()
        table = Table(show_header=True, header_style="bold white")

        table.add_column("TEAM", justify="left", style=" bold yellow", no_wrap=True)
        table.add_column("1ST", justify="center")
        table.add_column("2ND", justify="center")
        table.add_column("3RD", justify="center")
        table.add_column("4TH", justify="center")
        table.add_column("FNL", justify="center")

        for i, team in enumerate(self.teams):
            scores = self.scores[i]
            final_score = sum(scores[:])  # If you're not keeping a separate "Final" score
            table.add_row(str(team), str(scores[0]), str(scores[1]), str(scores[2]), str(scores[3]), str(final_score))
        
        console.print(table)

    def scoring_event(self, event, team, quarter):
        if event == 'touchdown':
            self.update_score(team, 6, quarter)  # Assuming 6 points for a touchdown
        elif event == 'extra point':
            self.update_score(team, 1, quarter)  # Assuming 1 points for a field goal
        elif event == 'field_goal':
            self.update_score(team, 3, quarter)  # Assuming 3 points for a field goal
        elif event == 'safety':
            self.update_score(team, 2, quarter)  # Assuming 3 points for a field goal

