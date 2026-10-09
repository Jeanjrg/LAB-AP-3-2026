def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = int(subtotal * 0.9)  # Diskon 10%
    return subtotal

def main():
    print("Selamat datang di Kasir Minimarket!")
    status_input = input("Apakah Anda member? (y/n): ").strip().lower()
    is_member = True if status_input == 'y' else False
    
    total_belanja = 0

    while True:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        if nama_barang == "":
            break
        
        harga = int(input("Harga barang: "))
        jumlah = int(input("Jumlah barang: "))
        
        subtotal = hitung_subtotal(harga, jumlah, adalah_member=is_member)
        print(f"Subtotal {nama_barang}: Rp{subtotal}")
        
        total_belanja += subtotal

    print(f"Total belanja: Rp{total_belanja}")

if __name__ == "__main__":
    main()

    