
def hitung_mundur(n):
    print(n)
    if n == 0:
        print("Luncurkan!")
        return 
    hitung_mundur(n - 1)

while True:
    angka_awal = input("Masukkan angka awal hitung mundur: ")
    try:
        angka = int(angka_awal)
    except:
        print("Input tidak valid, masukkan angka bulat.")
        continue
    if angka < 0:
        print("Input tidak valid, angka tidak boleh negatif.")
        continue
    break
hitung_mundur(angka)