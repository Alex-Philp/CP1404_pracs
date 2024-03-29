class Guitar:

    def __init__(self, name="", year=0, cost=float):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return int(2019) - int(self.year)

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
