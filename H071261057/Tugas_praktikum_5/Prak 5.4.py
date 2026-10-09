
def deteksi_anomali_email(email):
    error = []

    # Email harus memiliki tepat satu karakter @
    jumlah_at = email.count("@")

    if jumlah_at != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    # Memisahkan email menjadi bagian local dan domain
    bagian = email.split("@")
    local = bagian[0]
    domain = bagian[1]

    # Local dan domain tidak boleh kosong
    if local == "" or domain == "":
        error.append(
            "Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong."
        )

    # email tidak boleh mengandung spasi
    if " " in email:
        error.append("Email tidak boleh mengandung spasi.")

    # memeriksa bagian local
    if local.startswith("."):
        error.append(
            "Bagian local tidak boleh diawali atau diakhiri titik (.) serta tidak boleh mengandung titik berurutan."
        )
    elif local.endswith("."):
        error.append(
            "Bagian local tidak boleh diawali atau diakhiri titik (.) serta tidak boleh mengandung titik berurutan."
        )
    elif ".." in local:
        error.append(
            "Bagian local tidak boleh diawali atau diakhiri titik (.) serta tidak boleh mengandung titik berurutan."
        )

    # Memeriksa bagian domain
    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    elif ".." in domain:
        error.append(
            "Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik."
        )
    elif domain.endswith("."):
        error.append(
            "Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik."
        )

    # Memeriksa akhiran domain
    if domain.endswith(".ac.id"):
        pass
    elif domain.endswith(".com"):
        pass
    elif domain.endswith(".id"):
        pass
    else:
        error.append(
            "Wajib berakhiran dengan .com, .id, atau .ac.id."
        )

    return error


def cetak_daftar(daftar_email, karakter_border):
    # Jika tidak ada email valid, tidak perlu mencetak tabel
    if len(daftar_email) == 0:
        return

    # Mencari email yang paling panjang
    lebar = len("HASIL EMAIL VALID")

    for email in daftar_email:
        if len(email) > lebar:
            lebar = len(email)

    # Membuat garis tabel
    garis = karakter_border * (lebar + 4)

    print("\n--- HASIL EMAIL VALID ---")
    print(garis)

    # Menampilkan setiap email yang valid
    for email in daftar_email:
        spasi = lebar - len(email)
        print("| " + email + (" " * spasi) + " |")

    print(garis)


# PROGRAM UTAMA

print("=== Sistem Pencatatan Email Valid ===")

border = input("Masukkan border dengan karakter bebas: ")

print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_email = []

# Mengulang input sampai pengguna mengetik tutup
while True:
    email = input("Masukkan email: ")

    # Menghentikan program jika input adalah tutup
    if email.lower() == "tutup":
        break

    # Memeriksa aturan email
    error = deteksi_anomali_email(email)

    # Jika terdapat kesalahan
    if len(error) > 0:
        print(">> Email DITOLAK karena:")

        for alasan in error:
            print("   - " + alasan)

    # Jika email sudah pernah dimasukkan
    elif email in daftar_email:
        print(">> Email DITOLAK karena:")
        print("   - Email sudah terdaftar (Duplikat).")

    # Jika email valid dan belum pernah dimasukkan
    else:
        daftar_email.append(email)
        print(">> Email VALID!")


cetak_daftar(daftar_email, border)
