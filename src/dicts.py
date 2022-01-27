from collections import defaultdict


class location:
    def __init__(self, valid, index, tag):
        self.valid = valid
        self.index = index
        self.tag = tag


map = defaultdict(list)
testmap = {new_list: [] for new_list in range(7)}


def maptocache(objects):
    map[objects.index] = [objects.valid, objects.tag]


for i in range(5):
    l = location(i, i+1, i+2)
    maptocache(l)

print(dict(map))
print(map[2][0])
print(testmap)