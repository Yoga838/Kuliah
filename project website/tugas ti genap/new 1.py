inp = int(input('Masukkan angka : '))
locker = {}
for i in range (inp):
    inp1 = input('Masukkan Username : ')
    inp2 = input ('Masukkan Password : ')
    locker[inp1] = inp2
print ("="*4, 'Register Selesai', "="*4)

print ('='*7, 'Login', '='*7)
user = input('Masukkan Username anda = ')
pw = input ('Masukkan Password anda = ')
if locker[user]==pw : 
    print ('login Berhasil')
else :
    print ('Gagal Login')