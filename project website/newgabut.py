hargatotal = 0
katasalah = [ ]
i = 0
while True:
    JumlahBarang = int(input('Entrikan Jumlah Barang Yang Dibeli = '))
    HargaBarang = int(input('Entrikan Harga Satuan Barangnya = '))
    hargatotal += JumlahBarang*HargaBarang
    ask = input('Apakah Ada Lagi Item Barang Yang Di Entrikan atau tidak? [y]/[t]')
    while ask != 'y' and ask !='t' :
        katasalah.append(ask)
        ask = input('Apakah Ada Lagi Item Barang Yang Di Entrikan atau tidak? [y]/[t] ')
    if ask == 't' :
        break
print ('total harga anda = ', hargatotal)
for elemenkatasalah in katasalah :
    print('karakter salah indeks ke ',i,'adalah',elemenkatasalah)
    i += 1