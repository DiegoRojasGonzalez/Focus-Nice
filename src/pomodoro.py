import time
class Pomodoro:
    def __init__(self, Name, Time_focus, Time_break, Time_longbreak, Cycles, Cycle_Actually, State, Time):
        self.Name = Name
        self.Time_focus = Time_focus
        self.Time_break = Time_break
        self.Time_longbreak = Time_longbreak
        self.Cycles = Cycles
        self.Cycle_Actually = 0
        self.State = "Focus"
        self.Time = 0


