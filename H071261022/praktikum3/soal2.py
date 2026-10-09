print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    input_baris = input("Masukkan jumlah baris: ")
    try:
        jumlah_baris = int(input_baris)
    except:
        print("Input baris harus berupa angka!")
        print()
        continue
    if jumlah_baris <= 0:
        print("Jumlah baris harus lebih dari 0!")
        print()
        continue
    break

while True:
    input_kursi = input("Masukkan jumlah kursi per baris: ")
    try:
        jumlah_kursi = int(input_kursi)
    except:
        print("Input kursi harus berupa angka!")
        print()
        continue
    if jumlah_kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!")
        print()
        continue
    break
print()
print("--- Daftar Kursi Tersedia ---")

for baris in range(1, jumlah_baris + 1):
    for kursi in range(1, jumlah_kursi + 1):
        if kursi == 13:
            continue
        if baris == 1 and kursi % 2 == 0:
            continue
        print(f"Baris {baris} - Kursi {kursi}") 