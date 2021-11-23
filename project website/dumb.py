from os import X_OK


tmp1 = [1,2,3,4,5]
tmp = ['a','b','c','d','e']
v = {}
x = {}

for j in tmp1:
    for i in range (len(tmp)):
        print (i)
        rumus = j %2
        if rumus == 0 :
            v [tmp[i]] = j
        else:
            x [tmp[i]] = j
print (v)
print (x)