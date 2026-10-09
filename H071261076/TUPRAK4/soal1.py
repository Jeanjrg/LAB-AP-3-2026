def hitung_subtotal(harga, jumlah, adalah_member):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal *= 0.9
    return int(subtotal)

print("Selamat datang di Kasir Minimarket!")

status_input = input("Apakah Anda member? (y/n):  ").strip().lower()
adalah_member = True if status_input == "y" else False

total_belanja = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ").strip()
    if not nama_barang:
        break

    try:
        harga_barang = int(input("Harga barang: "))
        jumlah_barang = int(input("Jumlah barang: "))
    except:
        print("Harap masukkan angka yang valid untuk harga dan jumlah")
        continue

    subtotal = hitung_subtotal(harga_barang, jumlah_barang, adalah_member)
    total_belanja += subtotal

    print(f"subtotal {nama_barang}: Rp{subtotal}")

print(f"Total Belanja Rp{total_belanja}")
