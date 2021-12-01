import csv
import os
import datetime 

namaFile = 'tikete.csv'

tiket = []

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('\n', '='*49)
    print('{0:^49}'.format('TIKET KAI JATIM'))
    print('\n', '='*49)
    print('''
    1. Pesan tiket
    2. Lihat tiket yang telah di pesan
    3. Batalkan pemesanan
    ''')
    print('-' * 50)
    return int(input('Pilih Menu : '))

def pesan():
    clearScreen()
    print('FORM PEMESANAN')
    print('-'*50)
    tanggal = datetime.datetime.now() 
    asal = input("masukkan stasiun asal anda :")
    tujuan = input("masukkan stasiun tujuan anda :")
    print('\n')
    print('''
    1. Argo lawu \t (20000)
    2. Jayabaya \t (50000)
    3. Gajayana \t (35000)
    5. Wijayakusuma \t (25000)
    4. Ranggajati \t (75000)
    ''')
    bil = int(input('Pilih harga tiket: Rp '))
    print('\n')
    print("harga tiket per orang", bil)
    jmlh = int(input("jumlah tiket: "))
    num_array = list()
    for i in range (int(jmlh)):
        i += 1
        print()
        n = input("Masukkan Nama Pemesan {} :".format(i))
        num_array.append(str(n))
    total = jmlh*bil
    hrg = print("total harga : Rp ", total)
    print('\n')
    print ("Data berhasil ditambahkan!")
    tambahData(tanggal, n, asal, tujuan, bil, jmlh, hrg, total)
    back()    

def tambahData(tanggal, n, asal, tujuan, bil, jmlh, hrg, total):
    with open(namaFile,'a',newline='') as csv_file: 
        tulis = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tulis.writerow([tanggal, n, asal, tujuan, bil, jmlh, hrg, total])


def cetakData_jual():  
    clearScreen()
    proses = []
    with open(namaFile) as file:
        csvReader = csv.DictReader(file, delimiter = ',') 
        for row in csvReader:
            proses.append(row) 

    print('{0:^120}'.format('TIKET YANG TELAH ANDA PESAN')) 
    print('='*120)
    print('TANGGAL \t\t NAMA \t\t ASAL \t\t TUJUAN \t JUMLAH TIKET \t\t HARGA \t\t TOTAL')
    print('-'*120) 
    for data in proses: 
        print(f"{data['TANGGAL']} \t {data['NAMA']} \t {data['ASAL']} \t\t {data['TUJUAN']} \t {data['JUMLAH TIKET']} \t {data['HARGA']} \t\t {data['TOTAL']}") 
        print('\n')
    back()

def csv_ke_list():
    with open(namaFile,'r',newline='') as csv_file:  
        baca = csv.reader(csv_file) 
        for data in baca:
            tiket.append(data)

def hapusData(inputan):
    tiket.remove(tiket[inputan])
    with open(namaFile,'w',newline='') as csv_file:
        tulisUlang = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tulisUlang.writerows(tiket)
    back()

def read_csv(namaFile):
    temp_list = []
    with open(namaFile, 'r') as csv_file:
        baca = csv.reader(csv_file)
        for data in baca:
            temp_list.append(data)
        return temp_list
    print(namaFile)

def back(): 
    print('\n') 
    input('Tekan enter untuk kembali ke menu') 
    clearScreen()
    menu() 
    clearScreen()



if __name__ == "__main__":
    while True:
        csv_ke_list()
        pilih = menu()

        if pilih ==1: 
            pesan()

        elif pilih == 2: 
            cetakData_jual()

        elif pilih == 3:
            inputan = int(input("masukan indeks yang ingin dibatalkan : "))
            print("pemesanan tiket yang akan anda di batalkan {}".format(tiket[inputan]))
            hapusData(inputan)
            print("Pemesanan tiket berhasil dibatalkan ")