def tahun_kabisat(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

tahun = int(input("Masukkan tahun : "))

if tahun_kabisat(tahun):
    print("Tahun", tahun, "merupakan tahun kabisat.")
else:
    print("Tahun", tahun, "bukan tahun kabisat.")
