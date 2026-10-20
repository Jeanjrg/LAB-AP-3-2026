def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    print("\n==== PLAYLIST MUSIK PLAYTUNE ====")
    print(f"{'No':<3} | {'Judul':<20} | {'Artis':<15} | {'Genre':<10} | {'Durasi':<8}")
    print("-" * 65)
    total_detik = 0
    for i, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu
        total_detik += durasi
        menit = durasi // 60
        detik = durasi % 60
        durasi_str = f"{menit}:{detik:02d}"
        print(f"{i:<3} | {judul:<20} | {artis:<15} | {genre:<10} | {durasi_str:<8}")
    
    total_menit = total_detik // 60
    sisa_detik = total_detik % 60
    print("-" * 65)
    print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik\n")

def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]

def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu_dihapus = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus dari playlist.")
    else:
        print("Nomor lagu tidak valid!")

def statistik_playlist(playlist, genre_set):
    total_lagu = len(playlist)
    jumlah_genre = len(genre_set)
    
    distribusi = {genre: 0 for genre in genre_set}
    for lagu in playlist:
        genre = lagu[2]
        if genre in distribusi:
            distribusi[genre] += 1
            
    print("\n=== STATISTIK PLAYLIST PLAYTUNE ===")
    print(f"Total lagu          : {total_lagu}")
    print(f"Jumlah genre        : {jumlah_genre}")
    print(f"Daftar genre        : {genre_set}")
    print("Distribusi genre:")
    for genre, count in distribusi.items():
        print(f"  {genre:<15} : {'#' * count} ({count})")
        
    if playlist:
        lagu_terpanjang = max(playlist, key=lambda x: x[3])
        lagu_terpendek = min(playlist, key=lambda x: x[3])
        
        m_panjang = lagu_terpanjang[3] // 60
        d_panjang = lagu_terpanjang[3] % 60
        m_pendek = lagu_terpendek[3] // 60
        d_pendek = lagu_terpendek[3] % 60
        
        print(f"Lagu terpanjang     : {lagu_terpanjang[0]} ({m_panjang}:{d_panjang:02d})")
        print(f"Lagu terpendek      : {lagu_terpendek[0]} ({m_pendek}:{d_pendek:02d})")
    print("===================================")

def main_playtune():
    playlist = []
    genre_set = set()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            judul = input("Judul lagu: ")
            artis = input("Artis: ")
            genre = input("Genre: ")
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Durasi harus angka positif!")
                    continue
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Durasi harus berupa angka bulat (detik)!")
        elif pilihan == "2":
            tampilkan_playlist(playlist)
        elif pilihan == "3":
            print(f"Genre tersedia: {genre_set}")
            target = input("Masukkan genre yang ingin difilter: ")
            hasil_filter = filter_genre(playlist, target)
            print(f"Lagu bergenre '{target}':")
            for idx, lagu in enumerate(hasil_filter, 1):
                m = lagu[3] // 60
                d = lagu[3] % 60
                print(f"{idx}. {lagu[0]} - {lagu[1]} ({m}:{d:02d})")
        elif pilihan == "4":
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)
            except ValueError:
                print("Nomor lagu harus berupa angka!")
        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)
        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break
        else:
            print("Pilihan tidak valid.")

main_playtune()