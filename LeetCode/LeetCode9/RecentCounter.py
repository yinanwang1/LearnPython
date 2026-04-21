class RecentCounter:

    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)

        for i in range(len(self.times)):
            if t - 3000 <= self.times[i]:
                self.times = self.times[i:]
                break

        return len(self.times)
