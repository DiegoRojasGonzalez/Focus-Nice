import time

class Pomodoro:
    def __init__(self, Name, Time_focus, Time_break, Time_longbreak, Cycles):
        self.Name = Name
        self.Time_focus = Time_focus
        self.Time_break = Time_break
        self.Time_longbreak = Time_longbreak
        self.Cycles = Cycles
        self.Cycle_Actually = 0
        self.State = "Focus"
        self.Time = 0

    def Start(self):
        print("Start method (pomodoro.py)")
        while self.Cycle_Actually < self.Cycles:
            if self.State == "Focus":
                print("Focus for", self.Time_focus, "minutes")
                time.sleep(self.Time_focus * 60)
                self.State = "Break"
            elif self.State == "Break":
                print("Break for", self.Time_break, "minutes")
                time.sleep(self.Time_break * 60)
                self.Cycle_Actually += 1
                if self.Cycle_Actually % 4 == 0:
                    self.State = "Long Break"
                else:
                    self.State = "Focus"
            elif self.State == "Long Break":
                print("Long Break for", self.Time_longbreak, "minutes")
                time.sleep(self.Time_longbreak * 60)
                self.State = "Focus"

        print("Pomodoro completed!")



    