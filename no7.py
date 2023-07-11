import string

def remove_kalimat(sentence):
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    sentence = sentence.replace(" ", "")
    return sentence

kalimat = input("Masukkan kalimat : ")

kalimat_tanpa_tanda_baca_dan_spasi = remove_kalimat(kalimat)

print("Hasil : ", kalimat_tanpa_tanda_baca_dan_spasi)
