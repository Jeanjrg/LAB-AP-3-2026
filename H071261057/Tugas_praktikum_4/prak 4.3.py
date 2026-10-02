Angka_awal = int(input("Masukkan angka awal hitung mundur: "))
if Angka_awal < 0:
    print("Input tidak valid. Angka tidak boleh negatif.")
    exit()

def Hitung_angka(angka):
    if angka == 0:
        return
    print(angka)
    Hitung_angka(angka - 1)

Hitung_angka(Angka_awal)
print("Luncurkan!")
