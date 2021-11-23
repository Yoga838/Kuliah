print ("""
Aplikasi Penentu Bilangan Prima
Author : Ahmad Bagus Prayoga (212410102031)
""")


a = int(input('inputkan nilai prima '))
if a >= 2 and a <= 30 :
    b = a % 2 % 3
    if a == 2 or a == 3 :
        print ('PRIME')
    elif a == 9 or a == 15 or a == 21 or a == 25 or a == 27 :
        print ('NOT PRIME')
    else :
        if b == 0 :
            print ('NOT PRIME')
        elif b == 1 :
            print ('PRIME')
else :
    print ('ERROR')
