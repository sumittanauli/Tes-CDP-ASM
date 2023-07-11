def konvert(detik):
    jam = detik // 3600
    menit = (detik % 3600) // 60
    remaining_seconds = (detik % 3600) % 60
    return jam, menit, remaining_seconds

total_detik = int(input("Masukkan jumlah detik : "))

jam, menit, detik = konvert(total_detik)

print("Hasil konversi:")
print("Jumlah Jam:", jam)
print("Jumlah Menit:", menit)
print("Jumlah Detik:", detik)
