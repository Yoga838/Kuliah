inputan = float(input("masukkan angka di antara 0 - 5 atau 8 - 11 ="))

#rumus 0 lebih dari
rumus1 = inputan > 0

#rumus 5 kurang dari 
rumus2 = inputan < 5

#rumus 8 lebih dari 
rumus3 = inputan > 8

#rumus 11 kurang dari
rumus4 = inputan < 11

Correct = rumus1 and rumus2 or rumus3 and rumus4
print ("hasil yang anda inputkan adalah =", Correct)

print ("\n", 10*"=","\n")

inputan = float(input("masukkan angka di bawah 0 atau 5-8 atau diatas 11="))

#rumus 0 kurang dari
rumus1 = inputan < 0

#rumus 5 lebih dari 
rumus2 = inputan > 5

#rumus 8 kurang dari 
rumus3 = inputan > 8

#rumus 11 lebih dari
rumus4 = inputan < 11

Correct = rumus1 or rumus2 and rumus3 or rumus4
print ("hasil yang anda inputkan adalah =", Correct)

