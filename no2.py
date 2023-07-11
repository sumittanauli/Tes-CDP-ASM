def faktorial(n):
    if n == 0:  
        return 1
    else:
        return n * faktorial(n - 1)  

variabel = int(input("Masukkan nilai faktorialnya : "))

hasil = faktorial(variabel)
print("Hasil :")
print("Nilai desimalnya adalah", hasil)
