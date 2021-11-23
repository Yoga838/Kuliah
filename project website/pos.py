import json
import os
import security

def loadData(PATH):
    with open(PATH) as database:
        tmp = json.load(database)
        for i in range(len(tmp)):
            for j in tmp[i].keys():
                tmp[i][j] = security.deshifting(tmp[i][j],5)
        showData(tmp)
    return tmp

########## SHOW DATA ###############
def showData(arg1):
    if isinstance(arg1, list): # isinstance itu tujuannya untuk cek apakah variabel arg1 tipe datanya adalah list
        os.system('clear')
        print('Daftar Produk')
        print('-'*45)
        print('%-2s | %-20s | %-10s | %-2s'%('#','Nama','Harga','Stok'))
        print('-'*45)
        # ['A', 'B', 'C'] enumerate => [(0,'A'), (1,'B'), (2,'C')]
        for idx, item in enumerate(arg1):
            print('%-2s | %-20s | %-10s | %-2s'%(idx,item['nama'],item['harga_satuan'],item['stok']))
        print('-'*45)
    else:
        print('Tipe data tidak sesuai')
        exit()

########## DELETE DATA ################
def deleteData(arg1):
    showData(arg1)
    idx = int(input('Pilih index data: '))
    arg1.pop(idx)
    showData(arg1)
    return arg1

########### ADD DATA ###################
def addData(arg1):
    # Menambahkan data
    nama = input('Nama Produk: ')
    harga_satuan = int(input('Harga Satuan: '))
    stok = int(input('Stok: '))
    tmp = {'nama': nama, 'harga_satuan': harga_satuan, 'stok': stok}

    arg1.append(tmp)
    showData(arg1)
    return arg1

############# SAVE DATA ################
def saveData(arg1, arg2):
    '''
    arg1: tujuannya untuk mendapatkan nilai yang akan ditulis pada file
    arg2: tujuannya untuk menginformasikan path dari file 
    '''
    for i in range(len(arg1)):
        for j in arg1[i].keys():
            arg1[i][j] = security.shifting(arg1[i][j],5)
    
    data_dump = json.dumps(arg1) # json.dumps digunakan untuk mengkonversi dictionary atau list menjadi json dengan tipe data string
    
    with open(arg2,'w') as output: # Membuat sesi untuk menulis file dengan nama yang ada pada arg2 dengan tipe sesi adalah write
        output.write(data_dump) # perintah untuk menuliskan nilai pada file


######### MAIN PROGRAM #################
def main():
    os.system('clear')
    print("Point of Sales")
    DATA_PATH = 'data.json'
    data = []
    menu = ['1. Menampilkan Data', '2. Input Data', '3. Hapus Data', '4. Save Data', '5. Exit']
    data = loadData(DATA_PATH)
    while True:
        flatten_menu = ' '.join(menu) # ' ' => glue (karakter yang akan menyambungkan antar value yang ada pada list)
        print(flatten_menu)

        choice = input('Menu: ')

        if choice=='1':
            # Show Data
            data = loadData(DATA_PATH)
        elif choice=='2':
            # input Data
            data = addData(data)
        elif choice=='3':
            # Hapus Data
            deleteData(data)
        elif choice=='4':
            # Saving Data
            saveData(data, DATA_PATH)
        else:
            break