from datetime import datetime as dt
print ('-------------- Kasir 1.0 --------------')
print ("""
1. mobo: 
    1. Asus Rp.1.000.000,-
    1. GigaByte Rp.1.500.000,-
    1. Asrock Rp 900.000,-
2.Ram :
    1. Hyper X Rp. 1.100.000,-
    1. Kingston Rp. 700.000,-
    1. Corsair Rp.1.300.000,-
3.Cpu :
    1. Ryzen 3 2200G Rp.1.500.000,-
    1. ryzen 5 2400G Rp.2.200.000,-
    1. athlon 3000G Rp.850.000,-'
4.Vga :
    1. Gtx 1650 Super Rp.2.700.000,-
    1. Rtx 2060 Super Rp.5.400.000,-
    1. rx 6600  Rp.5.000.000,-
""")
produk = {'asus':1000000, 'gigabyte': 1500000, 'asrock':900000, 'hyper x':1100000, 'kingston':700000, 'corsair':1300000, 'ryzen 3 2200g':1500000, 'ryzen 5 2400g':2200000, 'athlon 3000g':850000, 'gtx 1650 super':2700000, 'rtx 2060':5400000,'rx 6600':5500000}
inp0 = int(input('Masukkan Jumlah jenis Barang = '))
tamp = []
for i in range (inp0) :
    tanggal = dt.today().strftime('%d %m %y')
    inp1 = input('masukkan nama barang ').lower()
    inp2 = int(input('masukkan banyak barang barang '))
    harga_barang = produk[inp1]*inp2
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
    
