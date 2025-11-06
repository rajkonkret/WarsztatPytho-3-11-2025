class Dates:
    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    @staticmethod
    def to_dash_date(date):
        return date.replace("/", "-")
