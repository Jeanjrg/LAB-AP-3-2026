print("Selamat Datang di Kasir Minimarket")

def hitung_total(Sub_total, diskon):
    potongan = Sub_total * diskon
    Total_akhir = Sub_total - potongan
    return Total_akhir
while True:
    Status_member = input("Apakah Anda Member? (y/n) : ").strip().lower()
    if Status_member == "y" :
        diskon = 0.10
        break
    elif Status_member == "n" :
        diskon = 0
        break
    else:
        print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")
        continue

    
    
total_subtotal = 0

while True:

    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if not nama_barang:
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    Sub_total = harga * jumlah

    print("Sub total", nama_barang, ": Rp", hitung_total(Sub_total, diskon))
    total_subtotal += hitung_total(Sub_total, diskon)

print("Total semua barang: Rp", total_subtotal)

