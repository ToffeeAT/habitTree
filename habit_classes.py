from datetime import date

class Habit:
    def __init__(self,name, date_started, streak, goal_streak, score, last_completed):
        self.name = name
        self.date_started = date_started
        self.streak = streak
        self.goal_streak = goal_streak
        self.score = score
        self.last_completed = last_completed

    def complete(self):
        today = date.today()
        if self.last_completed != None:
            difference = (today - self.last_completed).days
            if difference == 0:
                return False
            elif difference == 1:
                self.streak += 1
                self.score += 1
                self.last_completed = today
                return True
            else:
                self.reset_streak()
                self.streak += 1
                self.score += 1
                self.last_completed = today
                return True
        else:
            self.last_completed = today
            self.streak += 1
            self.score += 1
            return True

    def update_goal_streak(self, streak_update):
        try:
            num = int(streak_update)
            if num <= self.streak:
                raise ValueError
            else:
                self.goal_streak = num
                return True
        except ValueError:
            return False

    def reset_streak(self):
        self.streak = 0

    def get_growth_stage(self):
        if self.score >= 30:
            return "Tree"
        elif 30 > self.score >= 25:
            return "Flower"
        elif 25 > self.score >= 15:
            return "Plant"
        elif 15 > self.score >= 5:
            return "Sprout"
        else:
            return "Seed"

    def goal_reached(self):
        return self.streak >= self.goal_streak


        
    
class HabitTracker:
    def __init__(self, habits):
        self.habits = habits

    def add_habit(self, name_input, goal):
        for h in self.habits:
            if h.name == name_input:
                return False
        habit = Habit(name_input, date.today(), 0, goal, 0, None)
        self.habits.append(habit)
        return True
    
    def find_habit(self, name_input):
        for h in self.habits:
            if h.name == name_input:
                return h
        return None

    def delete_habit(self, name_input):
        res = self.find_habit(name_input)
        if res is not None:
            self.habits.remove(res)
            return True
        else:
            return False

    def complete_habit(self, name_input):
        res = self.find_habit(name_input)
        if res is not None:
            complete_res = res.complete()
            return complete_res
        else:
            return False

    def check_all_streaks(self):
        today = date.today()
        for h in self.habits:
            if h.last_completed is not None:
                difference = (today - h.last_completed).days
                if difference > 1:
                    h.reset_streak()





