
# Fungsi untuk mendaftarkan kandidat
def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()

    if nama in kandidat_set:
        print("Kandidat sudah terdaftar!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


# Fungsi untuk mencatat suara
def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if nama_pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")

    elif pilihan not in kandidat_set:
        print("Kandidat tidak tersedia! Suara tidak dicatat.")

    else:
        rekap_suara[nama_pemilih] = pilihan
        print(f"Suara berhasil dicatat untuk '{pilihan}'!")


# Fungsi untuk menghitung suara
def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


# Fungsi untuk menampilkan hasil
def tampilkan_hasil(perolehan):
    print("==================================")
    print("HASIL PEMILIHAN KETUA KELAS")
    print("==================================")

    for kandidat, jumlah in perolehan.items():
        print(f"{kandidat}: {jumlah} suara")

    total = sum(perolehan.values())
    print(f"Total suara masuk: {total}")

    if total == 0:
        print("Belum ada suara yang masuk!")
        return

    suara_tertinggi = max(perolehan.values())
    pemenang = []

    for kandidat, jumlah in perolehan.items():
        if jumlah == suara_tertinggi:
            pemenang.append(kandidat)

    if len(pemenang) > 1:
        print("Hasil SERI antara:", ", ".join(pemenang))
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")

    print("==================================")


# PROGRAM UTAMA
kandidat_set = set()
rekap_suara = {}

print("==================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("==================================")

# Fase pendaftaran kandidat
print("--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama == "":
        break

    daftar_kandidat(kandidat_set, nama)

# Memastikan minimal ada 2 kandidat
while len(kandidat_set) < 2:
    print("Minimal harus ada 2 kandidat!")

    nama = input("Masukkan nama kandidat: ")

    if nama != "":
        daftar_kandidat(kandidat_set, nama)

print("Kandidat terdaftar:", kandidat_set)

# Fase pemungutan suara
print("--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")

    if nama_pemilih == "":
        break

    print("Kandidat yang tersedia:", kandidat_set)
    pilihan = input("Pilih kandidat: ")

    berikan_suara(
        rekap_suara, kandidat_set, nama_pemilih, pilihan
    )

# Menampilkan hasil pemilihan
perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)
