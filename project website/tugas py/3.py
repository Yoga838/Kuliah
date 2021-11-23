 # PROGRAM KE 3

import random #
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