def bubble_sort(angk):
    for i in range(len(angka)):
        for j in range(len(angka) - 1):
            if angka[j] > angka[j+1]:
                angka[j], angka[j+1] = angka[j+1], angka[j]

angka = [7,3,5,6,4,2,1]
bubble_sort(angka)
print(angka)