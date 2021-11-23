a = input("Masukkan Nama Anda ")
print ("""
pilih Jenis Kelamin Anda !
1. laki - laki 
2. Perempuan
""")
b = int(input())
c = int(input("masukkan umur anda "))

if b == 2 :
    if c >= 1 and c <= 26 :
        print ("halo saudari", a )
    elif c > 26 :
        print ("halo Bu", a)
elif b == 1 :
    if c >= 1 and c <= 26 :
        print ("halo saudara", a )
    elif c > 26 :
        print ("halo Pak", a)