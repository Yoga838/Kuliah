total_pembayaran = 0
condition = True
while condition:
    jumlah = int(input('jumlah barang yang dibeli : '))
    harga = int(input('entrikan harga barang'))

    total_pembayaran += jumlah + harga
    jawab = input('pilih y / t')
    while jawab != 'y' or jawab != 't':
        jawab_1 = input('apakah ada lagi?')
    if jawab == "t" :
        condition = False
