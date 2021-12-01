import json
openjs = open("datatgs.json")
data = json.loads(openjs.read())
tmp = []
tmp1 = []
genap = []
ganjil = []
for i in data :
    for j in i.items():
        v = j[1]
        v = str(v)
        x = j[0]
        tmp1.append(x)
        tmp.append(v)
for j in tmp:
    tmp2 = j[-1]
    tmp2 = int(tmp2)
    rumus = tmp2 % 2
    if rumus == 0 :
        genap.append(j)
    else:
        ganjil.append(j)

for i in genap
print ('genap : ', genap)
print ('ganjil : ', ganjil)
# if rumus == 0 :
#        genap.append(j)
#     else:
#         ganjil.append(j)