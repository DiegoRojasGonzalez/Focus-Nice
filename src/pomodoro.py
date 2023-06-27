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

    def start(self):
        if self.State == "Focus":
            self.Time = self.Time_focus
        elif self.State == "Break":
            self.Time = self.Time_break
        elif self.State == "Long Break":
            self.Time = self.Time_longbreak

        while self.Time > 0:
            print(f"Time remaining: {self.Time} minutes")
            time.sleep(60)  # Sleep for 1 minute
            self.Time -= 1

        self.update_state()

    def update_state(self):
        if self.State == "Focus":
            self.Cycle_Actually += 1
            if self.Cycle_Actually == self.Cycles:
                self.State = "Long Break"
                self.Cycle_Actually = 0
            else:
                self.State = "Break"
        elif self.State == "Break":
            self.State = "Focus"
        elif self.State == "Long Break":
            self.State = "Focus"

        self.start()




