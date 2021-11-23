acuan = input()
n = int(input())

for i in range(n):
    memenuhi = True
    acuan_copy = acuan
    kata = input()
    for j in kata:
        if j in acuan_copy:
            acuan_copy = acuan_copy.replace(j,"",1)
        else:
            memenuhi = False
            break
    
    if memenuhi:
        print("Ya")
    else:
        print("Tidak")