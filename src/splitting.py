def addresssplitting(address,byteoffsetbits,indexbits,tagbits):
    rev = address[::-1]
    byteoffsetbits = 2
    indexbits = 14
    tagbits = 16

    byteoffset = rev[0:byteoffsetbits]
    index = rev[byteoffsetbits:indexbits+2]
    tag = rev[indexbits+2:len(rev)]
    return {
        'byteoffset' :byteoffset,
        'index'      :index,
        'tag'        :tag
    }
    # print(byteoffset)
    # print(index)
    # print(tag)


print(addresssplitting('00110000000001001100101010100000',byteoffsetbits=2,indexbits=14,tagbits=16))

# print(rev)


# References

# address
'''                                                    
     0011000000000100     11001010101000     00
     Tag                  Index          Byte offset
'''


# rev
'''              00010101010011          0010000000001100
     00          00010101010011          0010000000001100
    Byte offset     Index                 Tag
'''
