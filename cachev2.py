from collections import defaultdict
import json


class location:
    def __init__(self, index, tag):
        self.index = index
        self.tag = tag


byteoffsetbits = 2  # int(input("Enter the no of byteoffsetbits :"))
indexbits = 14  # int(input("Enter the no of indexbits :"))
tagbits = 16  # int(input("Enter the no of tagbits :"))


def bintodec(n):
    return int(n, 2)


def hextobin(n):
    dec = int(n, 16)
    return "{:032b}".format(dec)


def addresssplitter(address, byteoffsetbits, indexbits, tagbits):
    rev = address[::-1]
    byteoffsetz = rev[0:byteoffsetbits][::-1]
    indexz = rev[byteoffsetbits:indexbits + 2][::-1]
    tagz = rev[indexbits + 2:len(rev)][::-1]
    return {
        'byteoffset': byteoffsetz,
        'index': indexz,
        'tag': tagz
    }


map = {lst: [0, 0] for lst in range(75000)}
hits = 0
misses = 0
counter = 0


def maptocache(objects):
    map[objects.index] = objects.tag


with open('swim.trace', 'r') as f:
    for line in f:
        line = line[4:12]
        address = hextobin(line)
        thisdict = addresssplitter(address, byteoffsetbits, indexbits, tagbits)
        resbyteoffset = thisdict['byteoffset']
        resindex = thisdict['index']
        restag = thisdict['tag']
        l = location(bintodec(resindex), restag)
        maptocache(l)
        if map[l.index] == restag:
            hits += 1
        else:
            misses += 1
        counter += 1
print('misses :', misses)
print('hits :', hits)
print('total: ', counter)
