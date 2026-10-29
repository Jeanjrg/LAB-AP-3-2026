def format_durasi(detik):
    menit = detik // 60
    sisa_detik = detik % 60
    return f"{menit}:{sisa_detik:02d}"  # :02d agar detik selalu 2 digit (5:04)


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)  # tuple: data tidak bisa diubah
    playlist.append(lagu)
    genre_set.add(genre)  # set otomatis menolak genre yang sama
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    print("=" * 55)
    print(f"{'No':<4}{'Judul':<22}{'Artis':<15}{'Genre':<8}{'Durasi'}")
    print("=" * 55)

    total_detik = 0
    nomor = 1
    for lagu in playlist:
        judul, artis, genre, durasi = lagu  # membongkar isi tuple
        print(f"{nomor:<4}{judul:<22}{artis:<15}{genre:<8}{format_durasi(durasi)}")
        total_detik += durasi
        nomor += 1

    print("=" * 55)
    print(f"Total durasi playlist: {total_detik // 60} menit {total_detik % 60} detik")


def filter_genre(playlist, genre_target):
    # lagu[2] adalah genre, karena urutan tuple: (judul, artis, genre, durasi)
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Error: Nomor lagu tidak valid!")
        return False

    lagu_dihapus = playlist.pop(nomor - 1)  # nomor urut mulai 1, indeks mulai 0
    print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus!")
    return True


def statistik_playlist(playlist, genre_set):
    if len(playlist) == 0:
        print("Playlist masih kosong, belum ada statistik.")
        return

    # Hitung jumlah lagu per genre memakai dictionary
    hitungan_genre = {}
    for lagu in playlist:
        genre = lagu[2]
        if genre in hitungan_genre:
            hitungan_genre[genre] += 1
        else:
            hitungan_genre[genre] = 1

    # Cari lagu terpanjang dan terpendek
    terpanjang = playlist[0]
    terpendek = playlist[0]
    for lagu in playlist:
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu
        if lagu[3] < terpendek[3]:
            terpendek = lagu

    print("========================================")
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    print(f" Total lagu : {len(playlist)}")
    print(f" Jumlah genre : {len(genre_set)}")
    print(f" Daftar genre : {genre_set}")
    print(" Distribusi genre:")
    for genre, jumlah in hitungan_genre.items():
        print(f" {genre} : {'*' * jumlah} ({jumlah})")
    print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" Lagu terpendek : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("========================================")



# utama -----------------------------------------------------
playlist = []       # list of tuple
genre_set = set()   # set genre unik

print("========================================")
print(" PLAYLIST MUSIK - PLAYTUNE")
print("========================================")

while True:
    print("Menu:")
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
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                print("Error: Durasi harus angka positif!")
            else:
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        except ValueError:
            print("Error: Durasi harus berupa angka!")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        print(f"Genre tersedia: {genre_set}")
        genre_target = input("Masukkan genre yang ingin difilter: ")
        hasil = filter_genre(playlist, genre_target)
        if len(hasil) == 0:
            print(f"Tidak ada lagu bergenre '{genre_target}'.")
        else:
            print(f"Lagu bergenre '{genre_target}':")
            nomor = 1
            for lagu in hasil:
                print(f" {nomor}. {lagu[0]} - {lagu[1]} ({format_durasi(lagu[3])})")
                nomor += 1

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                berhasil = hapus_lagu(playlist, nomor)
                if berhasil:
                    # Perbarui set genre agar genre yang sudah tidak ada ikut hilang
                    genre_set.clear()
                    for lagu in playlist:
                        genre_set.add(lagu[2])
            except ValueError:
                print("Error: Nomor harus berupa angka!")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)
    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break
    else:
        print("Pilihan tidak valid! Masukkan angka 1-6.")
