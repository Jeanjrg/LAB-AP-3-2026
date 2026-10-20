def daftar_kandidat(kandidat_set, nama):
    nama_cap = nama.strip().capitalize()
    if nama_cap:
        kandidat_set.add(nama_cap)
        print(f"'{nama_cap}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih_lower = nama_pemilih.strip().lower()
    pilihan_cap = pilihan.strip().capitalize()
    
    if pemilih_lower in rekap_suara:
        print(f"'{nama_pemilih.strip().capitalize()}' sudah memberikan suara sebelumnya!")
        return
    
    if pilihan_cap not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak terdaftar!")
        return
    
    rekap_suara[pemilih_lower] = pilihan_cap
    print(f"Suara '{nama_pemilih.strip().capitalize()}' untuk '{pilihan_cap}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set}
    for pilihan in rekap_suara.values():
        if pilihan in perolehan:
            perolehan[pilihan] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    print("\n=== HASIL PEMILIHAN KETUA KELAS ===")
    total_suara = sum(perolehan.values())
    
    for kandidat, suara in perolehan.items():
        print(f"{kandidat}: {suara} suara")
    
    print(f"Total suara masuk: {total_suara}")
    
    if not perolehan or total_suara == 0:
        print("Belum ada suara yang masuk.")
        return

    suara_tertinggi = max(perolehan.values())
    pemenang = [k for k, v in perolehan.items() if v == suara_tertinggi]
    
    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(sorted(pemenang))}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
    print("===================================")

def main_voteclass():
    kandidat_set = set()
    rekap_suara = {}
    
    print("=== FASE PENDAFTARAN KANDIDAT ===")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
        if nama == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum bisa lanjut!")
                continue
            break
        daftar_kandidat(kandidat_set, nama)
        
    print(f"Kandidat terdaftar: {kandidat_set}")
    
    print("\n=== FASE PEMUNGUTAN SUARA ===")
    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
        if nama_pemilih == "":
            break
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)
        
    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)

main_voteclass()