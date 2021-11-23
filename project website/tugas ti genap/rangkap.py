print ('''
pilih menu anda :
1. Piramida 
2. Kata Reverse
3. User Generate and Login (simple login)
4. 
''')
inp = int(input())
if inp == 1 :
    rows = int(input())
        for i in range(1, rows + 1):
            for j in range(1, i + 1) :
                print(j, end="")
        for j in range(i - 1, 0, -1 ):
        print(j, end="")
    print("")
elif inp == 2 :
    kata = input()
    kata = kata[::-1]
    print (kata)
elif inp == 3 :
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
elif inp == 4 :
