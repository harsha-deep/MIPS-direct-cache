from collections import defaultdict
from json import dumps
from math import log


# function to convert to binary string to a decimal integer
def bintodec(n):
    return int(n, 2)

# function to convert a hexadecimal string to a 32-bit binary string
def hextobin(n):
    dec = int(n, 16)
    return "{:032b}".format(dec)

# the input part.
cache_size = int(input("Enter the size of the cache in kilo bytes : "))
block_size = int(input("Enter the size of block in bytes : "))
byteoffsetbits = int(log(block_size) / log(2))
temp = int((cache_size * 1024) / block_size)
indexbits = int(log(temp)/log(2))
tagbits = 32 - (indexbits + byteoffsetbits)


# function to split the 32 bit address string into byteoffset, tag and index.
def addresssplitting(address, byteoffsetbits, indexbits, tagbits):
    rev = address[::-1]
    byteoffsetz = rev[0:byteoffsetbits][::-1]
    indexz = rev[byteoffsetbits:indexbits + 2][::-1]
    tagz = rev[indexbits + 2:len(rev)][::-1]
    return {
        'byteoffset': byteoffsetz,
        'index': indexz,
        'tag': tagz
    }


# Just a temporary class for mapping
class location:
    def __init__(self, valid, index, tag):
        self.valid = valid
        self.index = index
        self.tag = tag


# map = defaultdict()
# a dictionary of lists intitialized to all 0: [0,0]
map = {lst: [0, 0] for lst in range(75000)}


# mapping the index --> [valid bit, tag]
def maptocache(objects):
    map[objects.index] = [objects.valid, objects.tag]


# the main part
hit = 0
miss = 0
with open('swim.trace', 'r') as f:  # open the .trace file
    for line in f:
        line = line[4:12]  # 3004caa0
        address = hextobin(line)  # 32 bit address in binary
        thisdict = addresssplitting(address, byteoffsetbits, indexbits, tagbits)
        # extract the required elements from the dictionary
        resbyteoffset = thisdict['byteoffset'] 
        resindex = thisdict['index']
        restag = thisdict['tag']
        # creating a temporary object from the class location and the
        #using it for mapping.
        l = location(1, bintodec(resindex), restag)
        maptocache(l)
        #If valid bit == 1 and tag match then it is a hit.
        if map[l.index][0] == 1 and restag == map[l.index][1]:
            hit += 1
        else:
            miss += 1


print("miss ratio :", miss/(miss + hit))
print("hit ratio : ", hit/(miss + hit))

# printing the map dictionary to visualize the cache
# print(dumps(map, indent=4))
