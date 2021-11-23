tmp = []
tmp_copy = []
for i in range (6):
    inp = int(input())
    tmp.append(inp)
    inp1 = inp % 2
    inp1 = str(inp1)
    tmp_copy.append(inp1)
if tmp_copy.count('1') > tmp_copy.count('0'):
    index = tmp_copy.index ('0')
    print (tmp,'--->',tmp[index])
else :
    index = tmp_copy.index ('1')
    print(tmp,'--->',tmp[index])

