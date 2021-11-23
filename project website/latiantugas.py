#SOAL:

    #Buatlah sebuah program yang dapat mengubah suhu dari celcius menjadi (Farenheit/ Reamur/ Kelvin) Sesuai dengan pilihan user
    #Buatlah sebuah program yang dapat menghitung BMI dari user dan menentukan apakah dengan BMI tersebut user termasuk kedalam golongan overweight/normal/underweight etc.
    #Dengan menggunakan Import Random (yang dokumentasinya bisa di cek di w3schools.com) buatlah sebuah program yang dapat bermain batu, gunting, kertas dengan user dan menampilkan hasilnya menang / kalah tergantung dengan pilihan user dan pilihan program.

# PROGRAM PERTAMA

print ('program converter suhu celcius')
print ("="*10)

a = float(input('masukkan suhu celcius! = '))
print ("="*10)

if a :
    print ('silahkan pilih suhu yang anda mau convertkan')
    print ('1. fahrenheit')
    print ('2. Reamur')
    print ('3. Kelvin')

    b = float(input())
    
    if b == 1 :
        rumus = (a * 9/5) + 32
        print ('celcius ke farenheit adalah = ', rumus,"`F")
    elif b == 2 :
        rumus = a * 4/5
        print ('celcius ke Reamur adalah = ', rumus,"`R")
    elif b == 3 :
        rumus = a +273
        print ('celcius ke Kelvin adalah = ', rumus,"`K")

#PROGRAM KEDUA

print ('Program Penghitung BMI')
print ('='*10)

a = input('selamat datang di program pengukur Bmi. silahkan masukkan nama anda! :')
print ('='*10)
berat = float(input(f'oke {a} sekarang masukkan berat badan anda dalam satuan Kg= '))
tinggi = float(input(f'selanjutnya anda masukkan tinggi badan anda dalam satuan meter = '))
Bmi = berat / tinggi**2
if Bmi <= 18.5 :
    print ('Berat badan anda kurang / UnderWeight')
elif 18.6 <= Bmi <= 29.9 :
    print ('berat bandan anda normal ')
elif Bmi >= 30 :
    print ('berat badan anda Berlebih / Overweight')
else :
    print ('inputan salah!')

    # PROGRAM KE 3

import random
print('Game Gunting Batu Kertas')

print ('Role')
print ('sistem game ini menggunakan sistem acak \n jadi kemenangan player bergantung pada kehokian player')
print ('1. Gunting')
print ('2. Batu')
print ('3. Kertas')

a = int(input('silahkan pilih gunting / batu / kertas : '))


b = random.randint(1,3)

if b == 1 :
    if a == 1:
        print ('Bot Memilih Gunting')
        print ('Hasil Draw')
    elif a == 2:
        print ('Bot Memilih Gunting')
        print ('Anda Menang')
    elif a == 3:
        print ('Bot Memilih Gunting')
        print ('Bot Menang')
elif b == 2 :
    if a == 1:
        print ('Bot Memilih Batu')
        print ('Bot Menang')
    elif a == 2:
        print ('Bot Memilih Batu')
        print ('Hasil Draw')
    elif a == 3:
        print ('Bot Memilih Batu')
        print ('Anda Menang')    
elif b == 3 :
    if a == 1:
        print ('Bot Memilih Kertas')
        print ('Anda Menang')
    elif a == 2:
        print ('Bot Memilih kertas')
        print ('Bot menang')
    elif a == 3:
        print ('Bot Memilih Kertas')
        print ('Hasil Draw')      
else :
    print('inputan error')

