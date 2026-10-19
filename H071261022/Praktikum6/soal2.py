def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize() 
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebelumnya!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    kunci_pemilih = nama_pemilih.lower() 
    pilihan = pilihan.capitalize()        

    
    if kunci_pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    
    elif pilihan not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak ada! Suara tidak dicatat.")
    else:
        rekap_suara[kunci_pemilih] = pilihan
        print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in sorted(kandidat_set):
        perolehan[kandidat] = 0
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    print("========================================")
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    total_suara = 0
    for kandidat, jumlah in perolehan.items():
        print(f" {kandidat}: {jumlah} suara")
        total_suara += jumlah
    print(f"Total suara masuk: {total_suara}")

    if total_suara == 0:
        print("Belum ada suara yang masuk, tidak ada pemenang.")
    else:
        suara_tertinggi = max(perolehan.values())

        pemenang = []
        for kandidat, jumlah in perolehan.items():
            if jumlah == suara_tertinggi:
                pemenang.append(kandidat)

        if len(pemenang) == 1:
            print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
        else:
            print(f"Hasil SERI antara: {', '.join(pemenang)}")
            print("Perlu dilakukan pemilihan ulang!")
    print("========================================")


# utama ----------------------------------------------------------
kandidat_set = set()   
rekap_suara = {}       

print("========================================")
print(" SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

# ----- FASE PENDAFTARAN -----
print("--- FASE PENDAFTARAN KANDIDAT ---")
while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()

    if nama == "":
       
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat! Silakan tambah kandidat lagi.")
        else:
            break
    else:
        daftar_kandidat(kandidat_set, nama)

print(f"Kandidat terdaftar: {kandidat_set}")

# FASE PEMUNGUTAN SUARA ------------------------------------------
print("--- FASE PEMUNGUTAN SUARA ---")
while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()

    if nama_pemilih == "":
        break

    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ").strip()
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

# ----- HASIL -----
perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)