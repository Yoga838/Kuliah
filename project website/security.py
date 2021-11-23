def shifting(text, shift_number):
    result = ''
    for i in text:
        shifted = (ord(i)+shift_number)%127
        if shifted<=32:
            shifted+=32
        result += chr(shifted)
    return result

def deshifting(text, shift_number):
    result = ''
    for i in text:
        deshifted = ord(i)
        if (deshifted-32)<=32:
            deshifted = deshifted-32+127-shift_number
        else:
            deshifted = deshifted-shift_number
        result += chr(deshifted)
    return result