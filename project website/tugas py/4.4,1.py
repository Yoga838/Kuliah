from datetime import datetime as dt
print ('-------------- Kasir 1.0 --------------')
barang = {}
tamp = []
while True :
    inp = input ('admin / kasir ').lower()
    if inp == "admin":
        while inp == 'admin': 
            inpt = input ('tambah/hapus? ').lower()
            if inpt == 'tambah' :
                inp0 = input('masukkan nama barang ').lower()
                inp1 = int(input('masukkan harga barang '))
                barang[inp0] = inp1
            elif inpt == 'hapus' :
                inpz = input('masukkan nama barang ').lower()
                del barang[inp0]
            inpj = input ('keluar y/t? ').lower()
            if inpj == "y":
                break
            elif inpj == 't':
                continue
            print (barang)
    elif inp == 'kasir' :
        print ("{:<10} {:<10}".format('Nama_Barang', 'harga_Barang'))
        for key, value in barang.items():
            Nama_Barang, harga_Barang = value
            print ("{:<10} {:<10}".format(Nama_Barang, harga_barang))
        inp0 = int(input('Masukkan Jumlah jenis Barang = '))
        for i in range (inp0) :
            tanggal = dt.today().strftime('%d %m %y')
            inp1 = input('masukkan nama barang ').lower()
            inp2 = int(input('masukkan banyak barang barang '))
            harga_barang = barang[inp1]*inp2
            tmp = [f'Nama barang = {inp1} ', f'Banyaknya Barang = {inp2} ',f'Total Harga = {harga_barang}', f'Tanggal Transaksi = {tanggal}']
            tamp.append(tmp)
        print ('--------------------------------------')
        for i in tamp :
            for j in i :
                print (j)
        print ('--------------------------------------')
        while True :
            inp = input('Apakah ada Item yang mau di hapus? y/t ').lower()
            if inp == 'y':
                inp = int(input ('Item ke berapa yang mau di hapus? '))
                inp -= 1
                tamp.pop(inp)
            else:
                break
        print ('--------------------------------------')
        for i in tamp :
            for j in i :
                print (j)
        print ('---------- Happy Shoping ------------')