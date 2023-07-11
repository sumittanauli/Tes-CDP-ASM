def hitung_kalimat(sentence):
    sentence = sentence.replace(" ", "").lower()

    hitung_huruf = {}

    for huruf in kalimat:
        if huruf.isalpha():
            if huruf in hitung_huruf:
                hitung_huruf[huruf] += 1
            else:
                hitung_huruf[huruf] = 1

    sorted_letters = sorted(hitung_huruf.keys())

    jlh_huruf = 0
    for huruf in sorted_letters:
        count = hitung_huruf[huruf]
        print(f"{huruf}: {count}")
        jlh_huruf += count

    print("Jumlah huruf yang terpakai :", jlh_huruf)

kalimat = input("Masukkan kalimat : ")

hitung_kalimat(kalimat)
