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


def hextobin(n):
    dec = int(n, 16)
    return "{:032b}".format(dec)


address1 = '1fffff50'
address2 = '1fffff58'
address3 = '1fffff88'

print(hextobin(address1))
print(addresssplitting(hextobin(address1), 2, 14, 16))
print(addresssplitting(hextobin(address2), 2, 14, 16))
print(addresssplitting(hextobin(address3), 2, 14, 16))
'''
    {'byteoffset': '00', 'index': '11111111010100', 'tag': '0001111111111111'} index=16340
    {'byteoffset': '00', 'index': '11111111010110', 'tag': '0001111111111111'} index=16342
    {'byteoffset': '00', 'index': '11111111100010', 'tag': '0001111111111111'} index=16354


    00011111111111111111111101010000               
    00011111111111111111111101010000
'''
