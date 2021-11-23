#   Nama : Ahmad Bagus Prayoga
#   Nim : 212410102031
#   Tugas algo Percabangan
print ("""
Aplikasi Penentu Bilangan Prima
Author : Ahmad Bagus Prayoga (212410102031)
""")

a = float(input('masukkan angka 1 - 100 :')) # variabel dimana saya jadikan tempat penginputan data yang berupa float
if a >= 0 and a <= 40 : # memberikan perintah kondisi jika inputan berada di antara 0 - 40 akan mengeluarkan output E
    print ('E')
elif a >= 41 and a <= 45 : # memberikan perintah kondisi jika inputan berada di antara 40 - 45 akan mengeluarkan output ED
    print ('ED')
elif a >= 46 and a <= 50 : # memberikan perintah kondisi jika inputan berada di antara 46 - 50 akan mengeluarkan output D
    print ('D')
elif a >= 51 and a <= 55 : # memberikan perintah kondisi jika inputan berada di antara 51 - 55 akan mengeluarkan output CD
    print ('CD')
elif a >= 56 and a <= 65 : # memberikan perintah kondisi jika inputan berada di antara 56 - 60 akan mengeluarkan output C
    print ('C')
elif a >= 66 and a <= 70 : # memberikan perintah kondisi jika inputan berada di antara 61 - 70 akan mengeluarkan output BC
    print ('BC')
elif a >= 71 and a <= 75 : # memberikan perintah kondisi jika inputan berada di antara 71 - 75 akan mengeluarkan output B
    print ('B')
elif a >= 76 and a <= 80 : # memberikan perintah kondisi jika inputan berada di antara 76 - 80 akan mengeluarkan output AB
    print ('AB')
elif a >= 80 and a <= 100 : # memberikan perintah kondisi jika inputan berada di antara 80 - 100 akan mengeluarkan output A
    print ('A')
else :
    print ('angka yang anda masukkan tidak dapat diterjemahkan') # memberikan jalur alternatif pada if apabila hasil nya tidak true/salah/ tidak sesuai
