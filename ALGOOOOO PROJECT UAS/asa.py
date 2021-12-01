import utama
import json
def menu(arg1):
    while True :
        menu = """
        1.Tampilkan Data
        2.Pembayaran Ukt
        3.Menambah Siswa 
        4.Menghapus Siswa 
        5.exit
        """
        print (menu)
        inputan = int(input('masukkan Pilihan : '))
        if inputan == 1 :
            utama.loaddata(arg1)
        elif inputan == 2 :
            utama.pembayaran(arg1)
        elif inputan == 3 :
            utama.tambah()
        elif inputan == 4 :
            utama.hapus()
        elif inputan == 5 :
            exit()
menu('st1')

