GARIS_DOUBLE = "=" * 52
GARIS_STATS = "=" * 40


def format_durasi(detik):
    menit, sisa = divmod(detik, 60)
    return f"{menit}:{sisa:02d}"


def format_lagu(lagu):
    judul, artis, _, durasi = lagu
    return f"{judul} - {artis} ({format_durasi(durasi)})"

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    playlist.append((judul, artis, genre, durasi))
    genre_set.add(genre)
    return f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!"


def tampilkan_playlist(playlist):
    if not playlist: 
        return "Playlist masih kosong."

    w_judul = max(5, max(len(l[0]) for l in playlist))
    w_artis = max(5, max(len(l[1]) for l in playlist))
    w_genre = max(5, max(len(l[2]) for l in playlist))
    w_durasi = 6
    lebar = 4 + w_judul + w_artis + w_genre + w_durasi + 4 * 2
    garis = "=" * lebar

    baris = [
        garis,
        f"{'No':>3} {'Judul':<{w_judul}}  {'Artis':<{w_artis}}  "
        f"{'Genre':<{w_genre}}  {'Durasi':<{w_durasi}}",
        garis,
    ] 
    for i, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        baris.append(
            f"{i:>3} {judul:<{w_judul}}  {artis:<{w_artis}}  "
            f"{genre:<{w_genre}}  {format_durasi(durasi):<{w_durasi}}"
        )
    baris.append(garis)

    total = sum(l[3] for l in playlist)
    menit, detik = divmod(total, 60) 
    baris.append(f" Total durasi playlist: {menit} menit {detik} detik")
    return "\n".join(baris)


def filter_genre(playlist, genre_target):
    return [l for l in playlist if l[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        return playlist.pop(nomor - 1)
    return None


def statistik_playlist(playlist, genre_set):
    if not playlist:
        return "Playlist masih kosong, belum ada statistik."

    distribusi = {}
    for _, _, genre, _ in playlist:
        distribusi[genre] = distribusi.get(genre, 0) + 1

    terpanjang = max(playlist, key=lambda l: l[3])
    terpendek = min(playlist, key=lambda l: l[3])

    baris = [
        GARIS_STATS,
        "  STATISTIK PLAYLIST PLAYTUNE",
        GARIS_STATS,
        f"  Total lagu       : {len(playlist)}",
        f"  Jumlah genre     : {len(genre_set)}",
        f"  Daftar genre     : {genre_set}",
        "",
        "  Distribusi genre:",
    ]
    lebar_genre = max(len(g) for g in distribusi)
    for genre, jumlah in distribusi.items():
        baris.append(f"    {genre:<{lebar_genre}} : {'#' * jumlah} ({jumlah})")
    baris += [
        "",
        f"  Lagu terpanjang  : {format_lagu(terpanjang)}",
        f"  Lagu terpendek   : {format_lagu(terpendek)}",
        GARIS_STATS,
    ]
    return "\n".join(baris)

def input_durasi():
    while True:
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                raise ValueError
            return durasi
        except ValueError:
            print("Durasi harus berupa angka positif!")


def menu_tambah(playlist, genre_set):
    judul = input("Judul lagu: ").strip()
    artis = input("Artis: ").strip()
    genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
    durasi = input_durasi()
    print(tambah_lagu(playlist, genre_set, judul, artis, genre, durasi))


def menu_filter(playlist, genre_set):
    print(f"Genre tersedia: {genre_set}")
    genre = input("Masukkan genre yang ingin difilter: ").strip()
    hasil = filter_genre(playlist, genre)

    print(f"\nLagu bergenre '{genre}':")
    if hasil:
        for i, lagu in enumerate(hasil, start=1):
            print(f"  {i}. {format_lagu(lagu)}")
    else:
        print("  Tidak ada lagu dengan genre tersebut.")


def menu_hapus(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        return
    print(tampilkan_playlist(playlist))
    try:
        nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
    except ValueError:
        print("Nomor harus berupa angka!")
        return

    lagu = hapus_lagu(playlist, nomor)
    if lagu:
        print(f"Lagu '{lagu[0]}' berhasil dihapus!")
    else:
        print("Nomor lagu tidak valid!")


def main():
    playlist = []
    genre_set = set()

    while True:
        print(f"\n{GARIS_DOUBLE}")
        print("   PLAYLIST MUSIK - PLAYTUNE")
        print(GARIS_DOUBLE)
        print("\nMenu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            menu_tambah(playlist, genre_set)
        elif pilihan == "2":
            print()
            print(tampilkan_playlist(playlist))
        elif pilihan == "3":
            menu_filter(playlist, genre_set)
        elif pilihan == "4":
            menu_hapus(playlist)
        elif pilihan == "5":
            print()
            print(statistik_playlist(playlist, genre_set))
        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break
        else:
            print("Pilihan tidak valid, pilih angka 1-6!")


if __name__ == "__main__":
    main()


