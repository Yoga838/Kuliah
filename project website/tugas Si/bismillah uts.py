inputan=int(input())
if inputan < 3:
    rumus = inputan*2
    print(rumus) 
elif inputan >= 3 :
    nilai1 = 2
    nilai2 = 4
    for i in range(2, inputan):
        Rumus = nilai1 + nilai2 
        nilai1 = nilai2
        nilai2 = Rumus
    print(Rumus)

