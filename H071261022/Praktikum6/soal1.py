# sistem inventaris toko buku ---------------------------------
def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):

    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)
    return hasil


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            # jika negatif
            if stok_baru < 0:
                print(f"Gagal! Stok '{buku['judul']}' tidak cukup. "
                      f"Stok saat ini: {buku['stok']}")
            else:
                buku["stok"] = stok_baru
                if jumlah >= 0:
                    print(f"Stok '{buku['judul']}' bertambah {jumlah}. "
                          f"Stok sekarang: {buku['stok']}")
                else:
                    print(f"Stok '{buku['judul']}' berkurang {-jumlah}. "
                          f"Stok sekarang: {buku['stok']}")
            return  # buku sudah ketemu, keluar dari function

    print(f"Error: Buku '{judul}' tidak ditemukan!")


def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0
    buku_termahal = None

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]

        if buku_termahal is None or buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku

    print("========================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")
    if buku_termahal is not None:
        print(f"Buku termahal : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    else:
        print("Buku termahal : -")
    print("========================================")


# PROGRAM UTAMA -----------------------------------------------
inventaris = []  # list kosong untuk menyimpan semua buku

print("========================================")
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("========================================")
print()

while True:
    print()
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        try:
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Error: Harga dan stok tidak boleh negatif!")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)
        except:
            print("Error: Harga dan stok harus berupa angka!")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        hasil = cari_buku(inventaris, kata_kunci)
        if len(hasil) == 0:
            print("Buku tidak ditemukan.")
        else:
            print(f"Ditemukan {len(hasil)} buku:")
            nomor = 1
            for buku in hasil:
                print(f" {nomor}. {buku['judul']} - {buku['penulis']} | "
                      f"Rp{buku['harga']} | Stok: {buku['stok']}")
                nomor += 1

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan (+ = tambah, - = kurang): "))
            update_stok(inventaris, judul, jumlah)
        except:
            print("Error: Jumlah perubahan harus berupa angka!")
    elif pilihan == "4":
        ringkasan_inventaris(inventaris)
    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break  # keluar dari loop
    else:
        print("Pilihan tidak valid! Masukkan angka 1-5.")



        