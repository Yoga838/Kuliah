import csv
import datetime
import os

namaFile = "data.csv"
os.system('cls')

def bacaData():
    with open(namaFile, "r") as csv_file:
        barang = csv.reader(csv_file, delimiter=",")
        for i in barang:
            print(i)

def tambahData():
    datahasil = []

    Tanggal = datetime.datetime.now()
    NamaBarang = input("Masukkan nama barang: ")
    JumlahBarang = int(input("Masukkan jumlah barang: "))
    harga = int(input("Harga: Rp."))
    TotalHarga = harga*JumlahBarang

    datahasil.append([NamaBarang, JumlahBarang, TotalHarga, Tanggal])

    with open(namaFile, "a", newline="") as csv_file:
        tambah = csv.writer(csv_file, delimiter=",")
        tambah.writerows(datahasil)
    print("\nTransaksi sukses!")

def hapusData():
    datahasil = []

    with open(namaFile, "r") as csv_file:
        barang = csv.reader(csv_file, delimiter=",")
        for i in barang:
            print(i)
            datahasil.append(i)

    nomor = int(input("Masukkan urutan list yang ingin dihapus: "))
    nomor -= 1
    del datahasil[nomor]
    with open(namaFile, "w", newline="") as csv_file:
        dataDihapus = csv.writer(csv_file)
        dataDihapus.writerows(datahasil) 
    print("\nTransaksi berhasil dihapus!")

def editData():
    datahasil = []

    with open(namaFile, "r") as csv_file:
        barang = csv.reader(csv_file, delimiter=",")
        for i in barang:
            print(i)
            datahasil.append(i)

    indeks = int(input("Masukkan list yang ingin diganti: "))
    indeks -= 1
    NamaBarang = input("Masukkan nama barang: ")
    JumlahBarang = int(input("Masukkan jumlah barang: "))
    harga = int(input("Harga: Rp."))
    TotalHarga = harga*JumlahBarang

    datahasil[indeks][0] = NamaBarang
    datahasil[indeks][1] = JumlahBarang
    datahasil[indeks][2] = TotalHarga

    with open(namaFile, "w", newline="") as csv_file:
        dataDiubah = csv.writer(csv_file)
        dataDiubah.writerows(datahasil)
    print("\nData berhasil di-edit!")

def menu(): 
    print ('''~~~~ APLIKASI KASIR ~~~~
[1] Lihat riwayat transaksi
[2] Tambah transaksi
[3] Hapus transaksi
[4] Edit transaksi
[5] Exit
--------------------------''')

if __name__ == "__main__":
    while True:
        menu()
        pilihMenu = input('Pilih Menu : ')
        if pilihMenu == '1':
            bacaData()
        elif pilihMenu == '2':
            tambahData()
        elif pilihMenu == '3':
            hapusData()
        elif pilihMenu == '4':
            editData()
        elif pilihMenu == '5':
            break
        else :
            print ('Pilihan Anda Salah, Silahkan Pilih Angka 1/2/3') 
        input('\nTekan apa saja untuk kembali\n')