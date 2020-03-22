class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_string):
        year, month,  day = tuple(date_string.split('/'))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls, date_string):
        year, month,  day = tuple(date_string.split('/'))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return '{year}/{month}/{day}'.format(year=self.year, month=self.month, day=self.day)


if __name__ == "__main__":
    new_day = Date(2018, 12, 13)
    new_day.tomorrow()
    print(new_day)

    date_string = "2018/11/12"
    new_date = Date.from_string(date_string)
    print(new_date)