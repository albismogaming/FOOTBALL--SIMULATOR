# TEAM CLASS

class Team:
    def __init__(self, abbreviation, score=0, timeouts=3):
        self.abbreviation = abbreviation
        self.score = score
        self.timeouts = timeouts
        self.possession = False
        self.total_yards = 0
        self.quarters = [0, 0, 0, 0]  # Scores for Q1, Q2, Q3, Q4
        self.final = 0

    def __str__(self):
        return self.abbreviation

    def update_quarter_score(self, quarter, points):
            if 1 <= quarter <= 4:
                self.quarters[quarter-1] += points
                self.update_final_score()

    def update_final_score(self):
        self.final = sum(self.quarters)

    def add_points(self, points):
        self.score += points

    def use_timeout(self):
        if self.timeouts > 0:
            self.timeouts -= 1
            return True
        return False

    def update_yards_gained(self, yards):
        self.total_yards += yards
