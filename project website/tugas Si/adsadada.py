acuan = input()
p = int(input())
for i in range(p): 
    kata = input()
    indeks = 0
    hasil = True
    while indeks < len(kata) :
        kondisi = kata[indeks] in acuan and kata.count(kata[indeks]) == 1
        if kondisi == True:
            indeks += 1 
            hasil &= kondisi
        else :
            indeks += 1
            hasil &= kondisi
    if hasil == True :
        print("Ya")
    else :
        print("Tidak")
