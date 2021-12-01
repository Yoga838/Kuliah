import json
import main

main.loaddata('st2')
def pembayaran (arg1):
    with open ('db.json','r')as opdb:
        tmp = json.load(opdb)
        inputan = int(input('masukkan no mahasiswa : '))
        tmp [inputan][arg1]="lunas"

    with open('db.json', 'w') as f:
        f.write(json.dumps(tmp))
pembayaran('st2')