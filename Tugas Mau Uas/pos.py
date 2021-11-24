import json # mengimport library json
import os # mengimport library os
import security # mengimport fungsi dari file security

def loadData(PATH): # Pembuatan fungsi dengan nama LoadData dengan syarat fungsi satu parameter 
    with open(PATH) as database: # membuat sesi pada file json kemudian di simpan ke dalam variabel database
        tmp = json.load(database) # mengambil data yang ada pada json kemudian di simpan ke dalam variable tmp
        for i in range(len(tmp)): # melakukan perulangan sebanyak panjagn variabel tmp
            for j in tmp[i].keys(): # melakukan perulangan yang bertujuan mendapatkan nilai tmp dengan index i yang kemudian di simpan ke dalam variabel j
                tmp[i][j] = security.deshifting(tmp[i][j],5) # melakukan perubahan pada nilai tmp index j yang ada dalam index i menggunakan fungsi deshifting yang ada pada file security
        showData(tmp) # memanggil fungsi showdata dengan parameter tmp
    return tmp # mengembalikan nilai yang diperoleh ke dalam variabel tmp

########## SHOW DATA ###############
def showData(arg1): # pembuatan fungsi dengan nama showdata dengan syarat satu parameter
    if isinstance(arg1, list): # isinstance itu tujuannya untuk cek apakah variabel arg1 tipe datanya adalah list
        os.system('clear') # Fungsi system dengan argumen "clear" pada library os yang bertujuan untuk membersihkan terminal
        print('Daftar Produk') # menampilkan kata daftar produk
        print('-'*45) # menampilkan karakter "-" sebanyak 45 kali
        print('%-2s | %-20s | %-10s | %-2s'%('#','Nama','Harga','Stok')) # membuat tabel dan jarak antar kata untuk menampilkan 4 kata kata string
        print('-'*45) # menampilkan karakter "-" sebanyak 45 kali
        # ['A', 'B', 'C'] enumerate => [(0,'A'), (1,'B'), (2,'C')]
        for idx, item in enumerate(arg1): # melakukan perulangan sebanyak file yang ada pada enumerate
            print('%-2s | %-20s | %-10s | %-2s'%(idx,item['nama'],item['harga_satuan'],item['stok'])) # print table dengan isian dari json dan inisiasi jarak dan tanda tabel
        print('-'*45) # menampilkan karakter "-" sebanyak 45 kali
    else: #kondisi terakhir apabila kondisi yang lainnya tidak terpenuhi
        print('Tipe data tidak sesuai') 
        exit() # perintah untuk keluar dari program 

########## DELETE DATA ################
def deleteData(arg1): # pembuatan fungsi dengan nama deleteData dengan syarat satu parameter
    showData(arg1) # memanggil fungsi showdata dengan parameter arg1
    idx = int(input('Pilih index data: ')) # input user dengan perintah "pilih index data" kemudian di casting ke dalam format integer yang kemudian hasilnya di simpan ke dalam variabel idx
    arg1.pop(idx) # menghapus nilai yang ada pada arg1 berdasarkan index yang sesuai dengan nilai idx
    showData(arg1) # memanggil fungsi showdata dengan parameter arg1
    return arg1 # mengembalikan nilai yang diperoleh ke arg1

########### ADD DATA ###################
def addData(arg1): # Pembuatan fungsi dengan nama addData dengan syarat fungsi satu parameter 
    # Menambahkan data
    nama = input('Nama Produk: ') # input user dengan perintah "nama produk" yang kemudian di simpan ke dalam variabel nama
    harga_satuan = int(input('Harga Satuan: ')) # input user dengan perintah "harga satuan" lalu nilai tersebut di casting ke format integer kemudian di simpan ke dalam variabel harga_satuan
    stok = int(input('Stok: ')) # input user dengan perintah "stok " lalu nilai tersebut di casting ke format integer kemudian di simpan ke dalam variabel stok
    tmp = {'nama': nama, 'harga_satuan': harga_satuan, 'stok': stok} #inisiasi dictionary 

    arg1.append(tmp) # menambahkan nilai variabel tmp ke dala variabel arg1
    showData(arg1) # memamnggil fungsi showdata dengan parameter arg1
    return arg1 # mengembalikan nilai yang telah diperoleh ke arg1

############# SAVE DATA ################ 
def saveData(arg1, arg2): # Pembuatan fungsi dengan nama saveData dengan syarat fungsi dua parameter
    '''
    arg1: tujuannya untuk mendapatkan nilai yang akan ditulis pada file
    arg2: tujuannya untuk menginformasikan path dari file 
    '''
    for i in range(len(arg1)): # perulangan dengan jarak sebanyak panjang variabel arg1 / parameter 1
        for j in arg1[i].keys(): # melakukan perulangan yang bertujuan mendapatkan nilai arg1 dengan index i yang kemudian di simpan ke dalam variabel j
            arg1[i][j] = security.shifting(arg1[i][j],5) # melakukan perubahan pada nilai arg1 index j yang ada dalam index i menggunakan fungsi deshifting yang ada pada file security
    
    data_dump = json.dumps(arg1) # json.dumps digunakan untuk mengkonversi dictionary atau list menjadi json dengan tipe data string
    
    with open(arg2,'w') as output: # Membuat sesi untuk menulis file dengan nama yang ada pada arg2 dengan tipe sesi adalah write
        output.write(data_dump) # perintah untuk menuliskan nilai pada file


######### MAIN PROGRAM #################
def main(): # pembuatan fungsi dengan nama main
    os.system('clear') # Fungsi system dengan argumen "clear" pada library os yang bertujuan untuk membersihkan terminal
    print("Point of Sales") # menampilkan string "Point of Sales"
    DATA_PATH = 'data.json' # inisiasi variabel data_path untuk pemanggilan file json 
    data = [] # inisisasi data
    menu = ['1. Menampilkan Data', '2. Input Data', '3. Hapus Data', '4. Save Data', '5. Exit']
    data = loadData(DATA_PATH) # pemanggilan fungsi loadData dengan parameter DATA_PATH kemudian di simpan ke dalam variabel data
    while True: #infinity loops
        flatten_menu = ' '.join(menu) # ' ' => glue (karakter yang akan menyambungkan antar value yang ada pada list)
        print(flatten_menu) # menampilkan flatten_menu

        choice = input('Menu: ') # input user dengan perintah menu kemudian di simpan ke dalam variabel choice

        if choice=='1': # pengkondisian choice apabila sama dengan '1'
            # Show Data
            data = loadData(DATA_PATH) # pemanggilan fungsi loadData dengan argumen DATA_PATH kemudian di simpan ke dalam variabel data
        elif choice=='2': #pengkondisian ke dua apabila choice sama dengan '2'
            # input Data 
            data = addData(data) # pemanggilan fungsi addData dengan argumen data kemudian di simpan ke dalam variabel data 
        elif choice=='3': # pengkondisian ke tiga apabila choice sama dengan '3' 
            # Hapus Data
            deleteData(data) # pemanggilan fungsi deleteData dengan argumen data  
        elif choice=='4': # pengkondisian ke tiga apabila choice sama dengan '4'
            # Saving Data
            saveData(data, DATA_PATH)  # pemanggilan fungsi saveData dengan argumen data dan DATA_PATH 
        else:
            break # menghentikan perulangan infinity loops