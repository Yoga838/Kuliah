import pos
import json
import hashlib
import os

def loadAccount():
    '''
    Load data dari file akun.json kemudian dikonversi menjadi dictionary
    '''
    with open('akun.json','r') as account_db:
        account = json.load(account_db)
    return account


# load data kemudian disimpan pada variabel account
account = loadAccount()

while True:
    os.system('clear')
    menu = ['1. Login', '2. Buat Akun']
    
    print(' '.join(menu)) # menampilkan menu
    choice = int(input('Pilih: ')) # meminta pengguna untuk memilih menu

    if choice==1: # jika 1 maka login
        while True:
            username =  input("Username: ")
            password =  input("Password: ")

            for i in account: # mengiterasikan seluruh akun yang ada pada database akun
                hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest() # enkripsi password 
                if username==i['username'] and hashed_password==i['password']: # membandingkan password dengan format yang sama,  jika di db password yang disimpan adalah hasil hash maka inputan juga harus di hash
                    print('Selamat Datang ',i['username'])
                    pos.main()
                else:
                    print('Maaf username atau password anda salah')
    elif choice==2:
        # registrasi
        akun = {}
        akun['username'] = input("Username: ")
        akun['password'] = input("Password: ")
        akun['password'] = hashlib.md5(akun['password'].encode('utf-8')).hexdigest()
        account.append(akun)
        with open('akun.json','w') as output:
            output.write(json.dumps(account))
    