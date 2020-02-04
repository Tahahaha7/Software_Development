class ClockIterator():
    def __init__(self):
        self.h, self.m = 0, 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.m%60 == 59:
            self.h+=1
        self.m+=1
        return str(self.h%24).zfill(2)+":"+str(self.m%60).zfill(2)

clock = ClockIterator()
for time in clock:
    print(time)