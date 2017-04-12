from equality import EqualityMixin


class Interval(EqualityMixin):
    def __init__(self, start, end, value):
        self.start = float(start)
        self.end = float(end)
        self.value = value
        self.duration = self.end - self.start

    def __iter__(self):
        yield (self.start, self.end, self.value)

    def __repr__(self):
        return "I({a}, {b}, {c} [{d}])".format(a=self.start, b=self.end, c=self.value, d=self.duration)