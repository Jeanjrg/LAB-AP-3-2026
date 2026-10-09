print("---Setup Denah Bioskop NontonYuk---")

while True:
    try:
        b = int(input("Masukkan jumlah baris: "))
        if b <=0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        break
    except :
        print ("Input harus berupa angka!")


while True:
    try:
        k = int(input("Masukkan jumlah kursi per baris: "))
        if k <=0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        break
    except :
        print ("Input harus berupa angka!")


print("Daftar Kursi Tersedia")

for baris in range(1, b + 1):
    for kursi in range(1, k + 1):

        if kursi == 13:
            continue

        if baris == 1:
            if kursi % 2 != 0:
                print(f"baris {baris} - kursi {kursi}")

        else:
            print(f"baris {baris} - kursi {kursi}")