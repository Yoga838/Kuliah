nama = input('masukkan nama anda :')
Kelas = input('masukkan Kelas anda :')
nim = input ('masukkan 4 digit terakhir nim anda :')
print ("hai !", nim, nama, "dari kelas", Kelas)
print ("="*10)

a = int(input('masukkan nilai 1='))
b = int(input('masukkan nilai 2='))

operasi_aritmatika = a*b/a
print (operasi_aritmatika)

if operasi_aritmatika <= 10 :
    if operasi_aritmatika == 1 :
        print ('anda sangat true')
    else :
        print ('anda cuma true')
else :
    print ('anda false')


