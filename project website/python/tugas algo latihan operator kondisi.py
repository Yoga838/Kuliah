#   Nama : Ahmad Bagus Prayoga
#   Nim : 212410102031
#   Tugas Algo Operator Kondisi

i = 0
while i<5: # bermakna pengulangan pada variabel i apabila i memenuhi persyaratan
    nilai =  int(input("masukkan bilangan = ")) #untuk memberikan input pada pengulangan i
    i += 1 # bermaksud untuk menghentikan perulangan 
    if nilai % 2 == 1: #memoduluskan input supaya hasil nya bisa menjadi 0 dan 1 karena dalam data boolean true and false = 1 dan 0, dan memformat 1/true/ganjil atau 0/false/genap 
        print ("bilangan yang anda masukkan ganjil")
    else : # bermaksud apabila variabel yang di input salah atau tidak benar dapat di alihkan ke jalur ini
        print ("bilangan yang anda masukkan genap") 