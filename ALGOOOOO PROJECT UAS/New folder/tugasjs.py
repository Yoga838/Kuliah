import json
pengampungan = {}
with open("./First.json","r") as acc :
    akun = json.load(acc)
    Ganjil = []
    Genap = []
    for Nim in akun :
        nim = Nim['Nim']
        rumus = nim % 2
        if rumus == 1 :
            Ganjil.append(Nim)
        else :
            Genap.append(Nim)
    pengampungan ['Ganjil'] = Ganjil
    pengampungan ['Genap'] = Genap
with open ("./last.json",'w')as finall:
    json.dump(pengampungan,finall)