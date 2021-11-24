def shifting(text, shift_number): # Pembuatan fungsi dengan nama shifting dengan syarat fungsi dua parameter
    result = '' # inisiasi string ke dalam variabel result
    for i in text: # perulangan sebanyak isi variabel text
        shifted = (ord(i)+shift_number)%127 # pengubahan struktur ascii awal kemudian di simpan ke dalam variabel shifted
        if shifted<=32: # pengkondisian ketika nilai variabel shifted kurang dari atau sama dengan 32
            shifted+=32 # variabel shifted ditambahkan nilai 32
        result += chr(shifted) # mengubah nilai ascii shifted ke dalam bentuk karakter kemudian di tambahkan ke dalam variabel result
    return result #mengembalikan nilai yang diperoleh kedalam variabel result

def deshifting(text, shift_number): # Pembuatan fungsi dengan nama deshifting dengan syarat fungsi dua parameter
    result = '' # inisiasi string ke dalam variabel result
    for i in text: # perulangan sebanyak isi variabel text
        deshifted = ord(i) #mengubah nilai i ke dalam bentuk angka kemudian di simpan ke dalam variabl deshifted
        if (deshifted-32)<=32: # pengkondisian apabila nilai deshifted - 32 kurang dari atau sama dengan 32
            deshifted = deshifted-32+127-shift_number # nilai deshifted dikurangi 32 kemudian di tambah 127 lalu dikurangi dengan nilai variabel shift_number setelah itu disimpan ke dalam variabel deshifted 
        else: # pengkondisian ketika semua pengkondisian tidak bisa terpenuhi
            deshifted = deshifted-shift_number # nilai deshifted dikurangi nilai shift_number lalu disimpen kedalam variable deshifted
        result += chr(deshifted) # mengubah nilai ascii deshifted ke dalam bentuk karakter kemudian di tambahkan ke dalam variabel result
    return result #mengembalikan nilai yang diperoleh kedalam variabel result