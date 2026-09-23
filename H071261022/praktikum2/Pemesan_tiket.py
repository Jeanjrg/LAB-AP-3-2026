tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu (pagi/Malam): ")
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ")

match tujuan:
    case "pantai":
        if waktu == "pagi":
            print("Paket Rekomendasi: Paket A")
        elif waktu == "malam" and tipe == "dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "pegunungan":
        if waktu == "pagi" and tipe == "dewasa":
            print("Paket Rekomendasi: Paket B")
        elif waktu == "malam" and tipe == "dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "kota":
        if waktu == "malam":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case _:
        print("Tujuan tidak valid")