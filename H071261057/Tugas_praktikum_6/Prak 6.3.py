# ===== FUNGSI-FUNGSI =====

def format_durasi(detik):
    """Ubah detik menjadi format menit:detik, contoh 354 -> 5:54"""
    menit = detik // 60
    sisa = detik % 60
    return f"{menit}:{sisa:02d}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)   # tuple
    playlist.append(lagu)                  # masuk ke list
    genre_set.add(genre)                   # masuk ke set (otomatis unik)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    print("=" * 60)
    print(f"{'No':<4}{'Judul':<22}{'Artis':<16}{'Genre':<10}{'Durasi'}")
    print("=" * 60)

    total = 0
    for i, lagu in enumerate(playlist, start=0):
        judul, artis, genre, durasi = lagu   # unpacking tuple
        print(f"{i:<4}{judul:<22}{artis:<16}{genre:<10}{format_durasi(durasi)}")
        total += durasi

    print("=" * 60)
    print(f"Total durasi playlist: {total // 60} menit {total % 60} detik")


def filter_genre(playlist, genre_target):
    # list comprehension: ambil lagu yang genre-nya sama
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu = playlist.pop(nomor - 1)     # nomor tampil mulai 1, indeks mulai 0
        print(f"Lagu '{lagu[0]}' berhasil dihapus!")
    else:
        print("Nomor lagu tidak valid!")


def statistik_playlist(playlist, genre_set):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    print("=" * 40)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    print(f"Total lagu      : {len(playlist)}")
    print(f"Jumlah genre    : {len(genre_set)}")
    print(f"Daftar genre    : {genre_set}")

    # dictionary untuk menghitung lagu per genre
    hitungan = {}
    for lagu in playlist:
        genre = lagu[2]
        if genre in hitungan:
            hitungan[genre] += 1
        else:
            hitungan[genre] = 1

    print("Distribusi genre:")
    for genre, jumlah in hitungan.items():
        print(f"  {genre:<10}: {'#' * jumlah} ({jumlah})")

    # lagu terpanjang & terpendek (berdasarkan durasi di indeks 3)
    terpanjang = playlist[0]
    terpendek = playlist[0]
    for lagu in playlist:
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu
        if lagu[3] < terpendek[3]:
            terpendek = lagu

    print(f"Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f"Lagu terpendek  : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)


# ===== PROGRAM UTAMA =====

playlist = []        # list of tuple
genre_set = set()    # set genre unik

while True:
    print("=" * 40)
    print("PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)
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
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                print("Durasi harus angka positif!")
            else:
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        except ValueError:
            print("Durasi harus berupa angka!")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        print("Genre tersedia:", genre_set)
        target = input("Masukkan genre yang ingin difilter: ")
        hasil = filter_genre(playlist, target)
        if len(hasil) == 0:
            print(f"Tidak ada lagu bergenre '{target}'.")
        else:
            print(f"Lagu bergenre '{target}':")
            for i, lagu in enumerate(hasil, start=1):
                print(f"{i}. {lagu[0]} - {lagu[1]} ({format_durasi(lagu[3])})")

    elif pilihan == "4":
        tampilkan_playlist(playlist)
        if len(playlist) > 0:
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)
            except ValueError:
                print("Input harus berupa angka!")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid, pilih 1-6.")
