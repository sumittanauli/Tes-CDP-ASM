def konvert(jam, menit, detik):
    total_detik = (jam * 3600) + (menit * 60) + detik
    return total_detik

jam = int(input("Masukkan jumlah jam : "))
menit = int(input("Masukkan jumlah menit : "))
detik = int(input("Masukkan jumlah detik : "))

total_detik = konvert(jam, menit, detik)

print("Jumlah detik dari masukan diatas adalah :", total_detik)
