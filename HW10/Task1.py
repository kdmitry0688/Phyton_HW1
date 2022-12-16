

class MinStat:
    def __init__(self):
        self.v = []

    def add_number(self, n):
        self.v.append(n)

    def result(self):
        if self.v == []:
            return None
        else:
            return min(self.v)


class MaxStat:
    def __init__(self):
        self.v = []

    def add_number(self, n):
        self.v.append(n)

    def result(self):
        if self.v == []:
            return None
        else:
            return max(self.v)


class AverageStat:
    def __init__(self):
        self.v = []

    def add_number(self, n):
        self.v.append(n)

    def result(self):
        if self.v == []:
            return None
        else:
            n = len(self.v)
            s = sum(self.v)
            return s / n


values = [1, 2, 4, 5, 6]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

print('------ Пример 2 ------')
mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())

print('------ Пример 3 ------')
values = [1, 0, 0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
