from random import randrange

# a = random.randrange(1,20)
a = randrange (20)
print (a)
while True :
    i = int(input('masukkan tebakan anda = '))
    if i == a :
        print  ("berhasil")
        break
    elif i < a :
        print ("Lebih kecil")
    else :
        print ('Lebih Besar')

        

