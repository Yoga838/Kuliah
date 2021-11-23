kata_paten = input() # untuk kata patokan
banyak_kata = int(input()) # untuk banyak referensi yang dibutuhkan

for i in range (banyak_kata): # looping sebanyak variabel banyak kata
    kata_acuan = input() # kata tebakan 
    kata_paten_copy = kata_paten # variabel bayangan dari inputan kata patokan 
    hasil = True # pengkondisan hasil
    for z in kata_acuan: #untuk supaya kata acuan di sebutin satu satu 
        if z in kata_paten_copy :
            kata_paten_copy = kata_paten_copy.replace(z,"",1)
        else : 
            hasil = False
            break
    if hasil == True:
        print ("Ya")
    else :
        print ("Tidak")
