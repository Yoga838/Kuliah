Hindari = '''!()-[]{};:'",<>./?@#$%^&*_~'''
a = input('masukkan kata-kata anda! ')
aman = ""
for kata_aman in a :
  if kata_aman not in Hindari :
    aman = aman + kata_aman
print (aman)
