kiri = 'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'
kanan = 'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'
###### penjelasan: karakter yang berdempetan yakni "l" dan "o" berada di satu tangan (kanan) #######
a = input('masukkan kata nyaman ')
b = 0
c = 0 
d = True
e = True
penampungan_kiri = []
penampungan_kanan = []

for kata_nyaman in a :
    if kata_nyaman in kiri :
        b += 1
        if c == 1 :
            c -= 1
        elif b == 2 :
            d = False
            penampungan_kiri.append(kata_nyaman)
            b -= 2
    elif kata_nyaman in kanan :
        c += 1
        if b == 1: 
            b -=1 
        elif c == 2:
            e = False
            penampungan_kanan.append(kata_nyaman)
            c -= 2

print (penampungan_kiri, penampungan_kanan)

if d == True : 
    print (d)
    print ('penjelasan : setiap karakter selalu bergantian tangan')
elif d == False and e == False :
    print (e)
    print ('penjelasan : karakter yang berdempetan adalah ',penampungan_kanan,'berada di satu tangan (kanan) dan ', penampungan_kiri, 'berada di satu tangan (kiri)')
elif  d == False :
    print (d)
    print ('penjelasan : karakter yang berdempetan adalah ',penampungan_kiri,'berada di satu tangan (kiri)')
elif e == True :
    print (e)
    print ('penjelasan : setiap karakter selalu bergantian tangan')
elif e == False:
    print(e)
    print ('penjelasan : karakter yang berdempetan adalah ',penampungan_kanan,'berada di satu tangan (kanan)')
