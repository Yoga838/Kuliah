def penjumlahan():
    angka1 = int(input())
    angka2 = int(input())
    x = angka1 + angka2
    print(x)
    return
def pengurangan():
    angka1 = int(input())
    angka2 = int(input())
    x = angka1 - angka2
    print(x)
    return
def pembagian():
    angka1 = int(input())
    angka2 = int(input())
    x = angka1 / angka2
    print(x)
    return
def perkalian():
    angka1 = int(input())
    angka2 = int(input())
    x = angka1 * angka2
    print(x)
    return

print('Kalkulator sederhana')
print('''1.Penjumlahan
2.Pengurangan
3.Pembagian
4.Perkalian''')
operasi= input('Pilih operasi: ')
if operasi == "1":
    penjumlahan()
elif operasi == "2":
    pengurangan()
elif operasi == "3":
    pembagian()
elif operasi == "4":
    perkalian()