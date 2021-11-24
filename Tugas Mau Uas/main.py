import pos # mengimport fungsi yang ada di file pos.py
import json # mengimport library json
import hashlib #mengimport library hashlib
import os # mengimport library os

def loadAccount(): # pembuatan fungsi dengan nama loadAccount
    '''
    Load data dari file akun.json kemudian dikonversi menjadi dictionary
    '''
    with open('akun.json','r') as account_db: #pembuatan sesi di file json dengan perintah read kemudian disimpah ke adalam variabel account_db
        account = json.load(account_db) # mengambil data yang ada pada json kemudian di simpan  ke dalam variabel account
    return account # mengembalikan nilai yang di peroleh ke dalam variabel account


# load data kemudian disimpan pada variabel account
account = loadAccount() # inisiasi variabel account supaya memiliki fungsi yang sama dengan fungsi loadAccount

while True: # infinity loop 
    os.system('clear') # Fungsi system dengan argumen "clear" pada library os yang bertujuan untuk membersihkan terminal
    menu = ['1. Login', '2. Buat Akun'] # inisiasi list
    
    print(' '.join(menu)) # menampilkan menu dengan menambahkan spasi antar index pada list yang akan di tampilkan
    choice = int(input('Pilih: ')) # meminta pengguna untuk memilih menu

    if choice==1: # jika 1 maka login
        while True: # infinity loop
            username =  input("Username: ") # input user dengan perintah username yang kemudian di simpan ke dalam variabel username
            password =  input("Password: ") # input user dengan perintah Password yang kemudian di simpan ke dalam variabel Paswword

            for i in account: # mengiterasikan seluruh akun yang ada pada database akun
                hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest() # enkripsi password 
                if username==i['username'] and hashed_password==i['password']: # membandingkan password dengan format yang sama,  jika di db password yang disimpan adalah hasil hash maka inputan juga harus di hash
                    print('Selamat Datang ',i['username']) # menampilkan username berdasarkan index 1 dan selamat datang 
                    pos.main() # memanggil fungsi main pada file pos
                else: # kondisi apabila semua kondisi tidak terpenuhi
                    print('Maaf username atau password anda salah') # menampilkan kata "maaf username atau password anda salah"
    elif choice==2: # jika 2 maka registrasi
        # registrasi
        akun = {} #inisiasi dictionary
        akun['username'] = input("Username: ") # input user dengan perintah username yang kemudian di simpan kedalam bentuk dictionary dengan key username yang kemudian di simpan ke variabel akun
        akun['password'] = input("Password: ") # input user dengan perintah Paswword yang kemudian di simpan kedalam bentuk dictionary dengan key Paswword yang kemudian di simpan ke variabel 
        akun['password'] = hashlib.md5(akun['password'].encode('utf-8')).hexdigest() # mengenkripsi password hasil inputan user mengunakan hashlib md 5 kemudian disimpan kedalam variabel akun 
        account.append(akun) # variabel akum di tambahkan ke dalam variabel account
        with open('akun.json','w') as output: # membuat sesi pada file json dengan perintah write yang kemudian di simpan ke dalam variabel output
            output.write(json.dumps(account)) # memasukkan isi variabel account ke dalam file json
    