while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))
        if N <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except:
        print("Input jumlah kursi harus berupa angka!")

print("\n--- Sistem Reservasi PO BUS Dimulai ---\n")

total_pendapatan = 0
kursi_tersisa = N

while kursi_tersisa > 0:
    print(f"Sisa kursi: {kursi_tersisa}")
    
    try:
        umur = int(input("Masukkan umur penumpang: "))
        
        if umur < 0:
            print("Umur tidak valid!")
            continue

        if umur <= 5:
            harga = 0
            print("Kategori: Balita - Tiket Gratis (Rp 0)")

        elif umur <= 12:
            harga = 50000
            print("Kategori: Anak - Harga: Rp 50.000")
        else:
            harga = 100000
            print("Kategori: Dewasa - Harga: Rp 100.000")
            
        kursi_tersisa -= 1
        total_pendapatan += harga
        
    except:
        print("Input umur harus berupa angka!")

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")