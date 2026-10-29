daftar_buku = {}
daftar_penulis = {}
daftar_harga = {}
daftar_stok = {}

def tambah_buku( judul, penulis, harga, stok):
    daftar_buku[judul] = judul
    daftar_penulis[judul] = penulis
    daftar_harga[judul] = harga
    daftar_stok[judul] = stok
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(kata_kunci):
    urutan = 0
    for judul in daftar_buku.keys():
        if kata_kunci.lower() in judul.lower():
            urutan += 1
            if urutan == 1:
                print("Ditemukan buku:")
            penulis = daftar_penulis[judul]
            harga = daftar_harga[judul]
            stok = daftar_stok[judul]
            print(f" {urutan}. {judul} - {penulis} | Rp{harga} | Stok: {stok}")

    if urutan == 0:
        print("Tidak ada buku yang ditemukan")


def update_stok(judul, jumlah):
    ketemu = None
    for i in daftar_buku.keys():
        if i.lower() == judul.lower():
            ketemu = i

    if ketemu is None:
        print(f"Error: Buku '{judul}' tidak ditemukan!")
        return

    stok_baru = daftar_stok[ketemu] + jumlah
    if stok_baru < 0:
        print("Gagal! Stok tidak boleh menjadi negatif.")
    else:
        daftar_stok[ketemu] = stok_baru
        if jumlah >= 0:
            print(f"Stok '{ketemu}' bertambah {jumlah}. Stok sekarang: {stok_baru}")
        else:
            print(f"Stok '{ketemu}' berkurang {-jumlah}. Stok sekarang: {stok_baru}")


def ringkasan_inventaris():
    total_stok = 0
    total_aset = 0
    buku_termahal = None
    harga_termahal = -1

    for judul in daftar_buku.keys():
        total_stok += daftar_stok[judul]
        total_aset += daftar_harga[judul] * daftar_stok[judul]
        if daftar_harga[judul] > harga_termahal:
            harga_termahal = daftar_harga[judul]
            buku_termahal = judul

    print("========================================")
    print(" RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    print(f"Jumlah jenis buku : {len(daftar_buku)}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")
    if buku_termahal is None:
        print("Buku termahal     : -")
    else:
        print(f"Buku termahal     : {buku_termahal} (Rp{harga_termahal})")
    print("========================================")


print("========================================")
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("========================================")

while True:
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
    menu = input("Pilih menu (1-5): ")

    if menu == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        try:
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Error: Harga dan stok tidak boleh negatif!")
            else:
                tambah_buku(judul, penulis, harga, stok)
        except:
            print("Error: Harga dan stok harus berupa angka!")

    elif menu == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(kata_kunci)

    elif menu == "3":
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(judul, jumlah)
        except:
            print("Error: Jumlah perubahan harus berupa angka!")

    elif menu == "4":
        ringkasan_inventaris()

    elif menu == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1-5!")