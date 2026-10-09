while True:
    input_kursi = input("Masukkan maksimal kursi bus: ")
    try:
        sisa_kursi = int(input_kursi)
    except:
        print("Input jumlah kursi harus berupa angka!")
        continue
    if sisa_kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!")
        continue
    break

print()
print("--- Sistem Reservasi PO BUS Dimulai ---")
print()

total_pendapatan = 0
while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    input_umur = input("Masukkan umur penumpang: ")
    try:
        umur = int(input_umur)
    except:
        print("Input umur harus berupa angka!")
        print()
        continue
    if umur < 0:
        print("Umur tidak valid!")
        print()
        continue
    elif umur <= 5:
        harga = 0
        print(f"Kategori: Balita - Tiket Gratis (Rp {harga})")
    elif umur <= 12:
        harga = 50000
        print(f"Kategori: Anak - Harga: Rp {harga:,}")
    else:
        harga = 100000
        print(f"Kategori: Dewasa - Harga: Rp {harga:,}")
    total_pendapatan += harga
    sisa_kursi -= 1
    print()

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan:,}")