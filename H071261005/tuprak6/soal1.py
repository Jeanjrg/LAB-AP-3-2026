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
    hasil = [buku for buku in inventaris if kata_kunci.lower() in buku["judul"].lower()]
    print(f"Ditemukan {len(hasil)} buku:")
    for i, buku in enumerate(hasil, 1):
        print(f"{i}. {buku['judul']}")
        print(f"{buku['penulis']} | Rp{int(buku['harga']) if buku['harga'].is_integer() else buku['harga']} | Stok: {buku['stok']}")

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print(f"Stok '{buku['judul']}' tidak boleh negatif!")
            else:
                buku["stok"] = stok_baru
                if jumlah < 0:
                    print(f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {buku['stok']}")
                else:
                    print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {buku['stok']}")
            return
    print(f"Error: Buku '{judul}' tidak ditemukan.")

def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)
    
    if inventaris:
        buku_termahal = max(inventaris, key=lambda x: x["harga"])
        harga_termahal = int(buku_termahal['harga']) if buku_termahal['harga'].is_integer() else buku_termahal['harga']
        termahal_str = f"{buku_termahal['judul']} (Rp{harga_termahal})"
    else:
        termahal_str = "-"

    total_aset_str = int(total_aset) if total_aset.is_integer() else total_aset

    print("=== RINGKASAN INVENTARIS BOOKNEST ===")
    print(f"Jumlah jenis buku: {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset_str}")
    print(f"Buku termahal : {termahal_str}")
    print("=====================================")

def main_booknest():
    inventaris = []
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
                harga = float(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif!")
                    continue
                tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Input harga dan stok harus berupa angka!")
        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci)
        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif tambah, negatif=kurang): "))
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Jumlah perubahan harus berupa angka!")
        elif pilihan == "4":
            ringkasan_inventaris(inventaris)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan tidak valid.")

main_booknest()