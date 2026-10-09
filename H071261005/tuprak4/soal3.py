def hitung_mundur(angka):
    print(angka)
    if angka == 0:
        print("Luncurkan!")
        return
    hitung_mundur(angka - 1)

def main():
    while True:
        input_angka = int(input("Masukkan angka awal hitung mundur: "))
        if input_angka < 0:
            print("Input tidak valid, angka tidak boleh negatif.")
        else:
            hitung_mundur(input_angka)
            break

if __name__ == "__main__":
    main()
    