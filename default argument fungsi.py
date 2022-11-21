#contoh 1.
def apaantuh(nama = "ganteng"):
    print(f"hi {nama}")

apaantuh("armin")
apaantuh()

#contoh 2.
def sapatuh (nama,pesan = "apa kabar"):
    print(f"hai {nama} {pesan}")

sapatuh("kacok","hai ganteeeeng")
sapatuh("marchell")

#contoh 3.
def hitung_pangkat(angka,pangkat):
    
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

#contoh 4.
def fungsi(angka1=1,angka2=2,angka3=3,angka4=4):
    hasil = angka1 + angka2 + angka3 + angka4
    return hasil
print(fungsi())
print(fungsi(angka3=10))#untuk mengganti argumen
