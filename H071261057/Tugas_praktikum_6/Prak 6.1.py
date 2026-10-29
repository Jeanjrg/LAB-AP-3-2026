
inventaris = []

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok}

    inventaris.append(buku)
    print("Buku", judul, "berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    ditemukan = 0

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            ditemukan += 1
            print(
                str(ditemukan) + ". " + buku["judul"]
                + " - " + buku["penulis"]
                + " | Rp" + str(buku["harga"])
                + " | Stok: " + str(buku["stok"])
            )

    if ditemukan == 0:
        print("Buku tidak ditemukan.")
    else:
        print("Ditemukan", ditemukan, "buku.")


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():

            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal! Stok tidak boleh negatif.")
            else:
                buku["stok"] = stok_baru
                print("Stok berhasil diubah.")
                print("Stok sekarang:", buku["stok"])

            return

    print("Error! Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    total_stok = 0
    total_aset = 0

    for buku in inventaris:
        total_stok = total_stok + buku["stok"]
        total_aset = total_aset + buku["harga"] * buku["stok"]

    print("========================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    print("Jumlah jenis buku :", len(inventaris))
    print("Total seluruh stok:", total_stok)
    print("Total nilai aset  : Rp" + str(total_aset))

    if len(inventaris) > 0:
        termahal = inventaris[0]

        for buku in inventaris:
            if buku["harga"] > termahal["harga"]:
                termahal = buku

        print(
            "Buku termahal     : " + termahal["judul"]
            + " (Rp" + str(termahal["harga"]) + ")"
        )
    else:
        print("Buku termahal     : Belum ada buku")

    print("========================================")


# Menu utama
print("========================================")
print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("========================================")

while True:
    print("\nMenu:")
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
                print("Harga dan stok tidak boleh negatif.")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)

        except ValueError:
            print("Error! Harga dan stok harus berupa angka.")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")

        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)

        except ValueError:
            print("Error! Jumlah perubahan harus berupa angka.")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid!")
