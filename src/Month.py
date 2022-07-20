from Week import Week


class Month:
    weeks = []
    tasks = []


    def __init__(self, month_name: MonthName):
        self.month_name = month_name
        for week_number in range(5):
            self.weeks.append(Week(week_number))
