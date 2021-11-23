tmp = []
nilai = []
while True :
    print ('No, Nama, Nilai, Grade')
    for i in range (len(tmp)):
        for j in tmp :
            print (i+1 ,*j)
    print ('Mahasiswa yang lulus : ')
    print ('Mahasiswa yang tidak lulus : ')
    print ('Nilai tertinggi : ')
    print ('Nilai terendah : ' )

    print('''
1. MENAMBAH DATA
2. MENGHAPUS DATA
3. EXIT
    ''')
    inp = int(input())
    if inp == 1 :
        inp1 = input('masukkan nama :')
        inp2 = int(input('masukkan nilai :'))
        nilai.append(inp2)
        if 80<inp2<100 :
            grade = 'A'
            tmp_2 = [inp1,inp2,grade]
            tmp.append(tmp_2)
        if 75<inp2<80 :
            grade = 'B'
            tmp_2 = [inp1,inp2,grade]
            tmp.append(tmp_2)
        if 70<inp2<75 :
            grade = 'C'
            tmp_2 = [inp1,inp2,grade]
            tmp.append(tmp_2)
        if 65<inp2<70 :
            grade = 'D'
            tmp_2 = [inp1,inp2,grade]
            tmp.append(tmp_2)
        if 0<inp2<65 :
            grade = 'E'
            tmp_2 = [inp1,inp2,grade]
            tmp.append(tmp_2)
    elif 2:
        pass
    elif inp == 3 :
        break