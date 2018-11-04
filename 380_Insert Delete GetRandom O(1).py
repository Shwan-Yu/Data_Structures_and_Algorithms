import random
class RandomizedSet(object):
    def __init__(self):
        self.l = []
        self.d = {}

    def insert(self, val):
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val):
        if val not in self.d:
            return False
        index = self.d[val]
        newVal = self.l[-1]
        self.l[index] = newVal
        self.d[newVal] = index
        del self.d[val]
        self.l.pop()
        return True

    def getRandom(self):
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
