data1 = input('masukkan kata pertama !  ')
d = ""
for a in data1 :
    asci_code = ord(a)
    b = int(asci_code)
    if b < 110 :
        b += 13
        c = chr(b)
        d = d + c
    elif b >= 110 :
        b -= 13
        c = chr(b)
        d = d + c
print (d)