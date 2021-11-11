#rumus : (luas segitiga + luas persegi) / 5 = 1 sak semen
#sumber : https://contoh123.info/mencari-luas-gabungan-bangun-datar-soal-dan-jawaban/
#sumber 2 : https://kelasprogrammer.com/menghitung-luas-segitiga-python/

#nilai variabel 
A = float(input("Masukkan alas atap: "))
T = float(input("Masukkan tinggi atap: "))
B = float(input("Masukkan tinggi tembok: "))

#luas segitiga
S = (1/2 * A * T)
#luas persegi
P = (B * B)

J = (S + P) / 5

print("rumah tersebut membutuhkan", J ,"sak semen")
