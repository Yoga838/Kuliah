#PROGRAM KEDUA

print ('Program Penghitung BMI')
print ('='*10)

a = input('selamat datang di program pengukur Bmi. silahkan masukkan nama anda! :')
print ('='*10)
berat = float(input(f'oke {a} sekarang masukkan berat badan anda dalam satuan Kg= '))
tinggi = float(input(f'selanjutnya anda masukkan tinggi badan anda dalam satuan meter = '))
Bmi = berat / tinggi**2
if Bmi <= 18.5 :
    print ('Berat badan anda kurang / UnderWeight')
elif 18.6 <= Bmi <= 29.9 :
    print ('berat bandan anda normal ')
elif Bmi >= 30 :
    print ('berat badan anda Berlebih / Overweight')
else :
    print ('inputan salah!')
