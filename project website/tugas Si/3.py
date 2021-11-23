data1 = input('masukkan kata pertama !  ')
data2 = input('masukkan kata kedua !  ')
i = 0
j = 0
for a in data1 :
    asci_code = ord(a)
    b = int(asci_code)
    i += b
for a in data2 :
    asci_code = ord(a)
    b = int(asci_code)
    j += b
if i > j :
    print (data1)
else:
    print(data2)
print(i)
print(j)