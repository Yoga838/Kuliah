a = input("Masukkan Nama Anda ")
b = input("Masukkan Jenis Kelamin Anda (laki - laki / perempuan )")
c = int(input("masukkan umur anda "))

if b == "perempuan" :
    if c >= 1 and c <= 26 :
        print ("halo saudari", a )
    elif c > 26 :
        print ("halo Bu", a)
elif b == "laki - laki" :
    if c >= 1 and c <= 26 :
        print ("halo saudara", a )
    elif c > 26 :
        print ("halo Pak", a)