import json
import utama

def hapus():
    utama.loaddata('st1')
    inputan = int(input('masukkan no mahasiswa : '))
    with open ('db.json','r') as ldb :
        tmp = json.load(ldb)
    tmp.pop(inputan)
    with open ('db.json','w') as delete :
        json.dump(tmp,delete)
    utama.loaddata('st1')        
hapus()