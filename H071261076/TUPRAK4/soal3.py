import time
def hitung_mundur(n: int):
    print(n)
    time.sleep(1)
    if n > 0:
        hitung_mundur(n - 1)
    else:
        print("Luncurkan!")


while True:
    try:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))

        if angka_awal < 0:
            print("Input tidak valid, angka tidak boleh negatif.")
            continue  

        hitung_mundur(angka_awal)
        break

    except:
            print("Input tidak valid. Harap masukkan angka bulat (integer).")
