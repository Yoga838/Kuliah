import csv #dituliskan untuk memanggil file csv yg telah dibuat 
import datetime #dituliskan untuk membaca waktu saat data diinputkan


while True: #perulangan jika benar akan menjalankan perintah
    menu = print("\nMenu") #menampilkan tulisan menu
    pilihan = print("1. Tampilkan data\n2. Tambahkan data\n3. Hapus Data\n4. keluar") #menampilkan pilihan dari menu  
    jawaban = input("masukkan pilihan [1] [2] [3] [4] : ") #perintah untuk menginputkan jawaban 1,2,3 atau 4
    if jawaban == '1': #percabangan if yang jika jawaban 1 makan akan menjalankan perintah yang dituliskan

        with open('data.csv') as csv_f: #membuka file csv yang telah dibuat menggunakan nama alias yaitu "csv_f"
            csv_reader = csv.reader(csv_f, delimiter=",") #variabel csv_reader yang berisi perintah untuk membaca isi dari data csv
            data = list(csv_reader) #variabel untuk menampung list data

            for i in range(len(data)): #perulangan yang digunakan untuk memasukkan data dari range(len(data)) ke variabel i
                tanggal = datetime.datetime.now() #variabel untuk menampung data tanggal dan waktu
                day = tanggal.day #variabel untuk menampung tanggal saat data diinputkan
                month = tanggal.month #variabel untuk menampung bulan ke berapa data diinputkan
                year = tanggal.year #variabel untuk menampung tahun berapa data diinputkan
                Tanggal = (day , month , year) #variabel untuk menampung tanggal, bulan, dan tahun data saat data diinputkan
                print(f'{i+1}. {Tanggal} {data[i][0]} {data[i][1]} {data[i][2]}') #perintah untuk menampilkan data dari csv beseta tanggal dengan urut 

    elif jawaban == '2': #percabangan yang jika jawaban adalah 2, maka akan menjalankan perintah yang dituliskan
        hasil_entri = [] #Array atau list kosong yang disiapkan untuk menampung hasil dari input an nantinya

        with open('data.csv', newline='') as csv_f: #membuka file csv yang telah dibuat menggunakan nama alias yaitu "csv_f"
            csv_reader = csv.reader(csv_f, delimiter=",") #variabel csv_reader yang berisi perintah untuk membaca isi dari data csv

        nama_barang = str(input("masukkan nama barang : ")) #variabel perintah untuk menginputkan nama barang yang akan ditambahkan
        jumlah_barang = int(input("masukkan jumlah barang : ")) #variabel perintah untuk menginputkan jumlah barang yang akan ditambahkan
        total_harga = int(input("masukkan total harga barang : ")) #variabel perintah untuk menginputkan total harga barang yang akan ditambahkan
        
        hasil_entri.append(nama_barang) #nama barang yang telah diinputkan akan masuk ke dalam csv dengan adanya append ini
        hasil_entri.append(jumlah_barang) #jumlah barang yang telah diinputkan akan masuk ke dalam csv dengan adanya append ini
        hasil_entri.append(total_harga) #Total harga barang yang telah diinputkan akan masuk ke dalam csv dengan adanya append ini

        sukses = print("SELAMAT DATA BARU TELAH DITAMBAHKAN") #menampilkan tulisan "SELAMAT DATA BARU TELAH DITAMBAHKAN" setelah data ditambahkan
        with open("data.csv", "a", newline="") as csv_f: #membuka data baru dari csv 
            data_baru = csv.writer(csv_f, delimiter=",") #variabel data_baru yang berisi perintah untuk menulis isi dalam data csv
            data_baru.writerow(hasil_entri) #berisi perintah untuk menulis isi dalam baris baru

    elif jawaban == '3': #jika jawaban adalah 3, maka akan menjalankan perintah yang dituliskan
        with open('data.csv') as csv_f: #membuka file csv yang telah dibuat menggunakan nama alias yaitu "csv_f"
            csv_reader = csv.reader(csv_f) #variabel csv_reader yang berisi perintah untuk membaca isi dari data csv
            data = list(csv_reader) #variabel untuk mengubah bentuk data menjadi list
           
            for i in range(len(data)): #perulangan yang digunakan untuk memasukkan data dari range(len(data)) ke variabel i
                tanggal = datetime.datetime.now() #variabel untuk menampung data tanggal dan waktu
                day = tanggal.day #variabel untuk menampung tanggal saat data diinputkan
                month = tanggal.month #variabel untuk menampung bulan ke berapa data diinputkan
                year = tanggal.year #variabel untuk menampung tahun berapa data diinputkan
                Tanggal = (day , month , year) #variabel untuk menampung tanggal, bulan, dan tahun data saat data diinputkan
                print(f'{i+1}. {Tanggal} {data[i][0]} {data[i][1]} {data[i][2]}') #perintah untuk menampilkan data dari csv beseta tanggal dengan urut 
        nomor = int(input("masukkan nomor barang yang akan dihapus : ")) #perintah untuk menginputkan nomor urut data yang ingin dihapus
        nomor -= 1 #menentukan nomor data yang akan dihapus dari angka 1
        del data[nomor] #menghapus nomor yang dipilih 
        with open('data.csv' , 'w', newline='') as csv_f: #membuka file csv yang telah dibuat menggunakan nama alias yaitu "csv_f"
            data_baru_dihapus = csv.writer(csv_f) #menuliskan kembali data yang baru diperbarui
            for data_baru in data: #perulangan yang digunakan untuk memasukkan data dari data ke data_baru
                data_baru_dihapus.writerow(data_baru) #berisi perintah untuk menulis isi dalam baris baru
        print("ITEM BERHASIL DIHAPUS") #menampilkan tulisan "ITEM BERHASIL DIHAPUS" setelah menghapus data
     
    elif jawaban == '4': #jika jawaban adalah 4, maka akan menjalankan perintah yang dituliskan
        print ("TERIMAKASIH") #menampilkan tulisan "TERIMAKASIH"
        exit() #menutup dan menghentikan program
