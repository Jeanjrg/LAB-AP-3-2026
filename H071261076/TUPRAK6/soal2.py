GARIS = "=" * 40

def format_set(kandidat_set):
    return "{" + ", ".join(repr(k) for k in sorted(kandidat_set)) + "}"

def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()
    if nama in kandidat_set: 
        return False, f"'{nama}' sudah terdaftar sebagai kandidat!"
    kandidat_set.add(nama) 
    return True, f"'{nama}' berhasil didaftarkan sebagai kandidat!"

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    tampil = nama_pemilih.strip()
    pemilih = tampil.lower()
    pilihan = pilihan.strip().capitalize()

    if pilihan not in kandidat_set:
        return False, f"Kandidat '{pilihan}' tidak ada! Suara tidak dicatat."
    if pemilih in rekap_suara:
        return False, f"'{tampil}' sudah memberikan suara sebelumnya!"

    rekap_suara[pemilih] = pilihan
    return True, f"Suara '{tampil}' untuk '{pilihan}' berhasil dicatat!"


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in sorted(kandidat_set)}
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    total = sum(perolehan.values())

    print(GARIS)
    print("  HASIL PEMILIHAN KETUA KELAS")
    print(GARIS)
    for kandidat, jumlah in perolehan.items():
        print(f"  {kandidat}: {jumlah} suara")

    print(f"\nTotal suara masuk: {total}")

    if total == 0:
        print("Belum ada suara yang masuk.")
    else:
        tertinggi = max(perolehan.values())
        pemenang = [k for k, v in perolehan.items() if v == tertinggi]#mendeteksi jika ada suara yang seri
        if len(pemenang) > 1:
            print(f"Hasil SERI antara: {', '.join(pemenang)}")
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")
    print(GARIS)


kandidat_set = set()
rekap_suara = {}

print(GARIS)
print("  SISTEM PEMILIHAN KETUA KELAS")
print(GARIS)

print("\n--- FASE PENDAFTARAN KANDIDAT ---")
while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat sebelum bisa lanjut!")
            continue
        break
    berhasil, pesan = daftar_kandidat(kandidat_set, nama)
    print(pesan)

print(f"\nKandidat terdaftar: {format_set(kandidat_set)}")

print("\n--- FASE PEMUNGUTAN SUARA ---")
while True:
    nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ").strip()
    if nama_pemilih == "":
        break
    print(f"Kandidat yang tersedia: {format_set(kandidat_set)}")
    pilihan = input("Pilih kandidat: ")
    berhasil, pesan = berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)
    print(pesan)

print()
perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)