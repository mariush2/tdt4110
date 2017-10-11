import binascii

def toHex(word):
    return int(str((binascii.hexlify(word), 'ascii'), 16))

def toString(word):
    return str((binascii.unhexlify(hex(word)[2:]), 'ascii'))



def encrypt(message, key):
    hex_m = toHex(message)
    hex_k = toHex(key)

    return hex_m

toHex("hei")
