print ("---Sistem Pencatatan email valid---")

DOMAIN_RESMI = (".com", ".id", ".ac.id")


def deteksi_anomali_email(email):
    error = []

    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error 

    local, domain = email.split("@")

    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        error.append("Tidak boleh mengandung spasi di posisi manapun.")

    if local != "" and (local.startswith(".") or local.endswith(".") or ".." in local):
        error.append("Bagian local tidak boleh diawali atau diakhiri titik, "
                     "serta tidak boleh mengandung titik berurutan.")

    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    elif ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not email.lower().endswith(DOMAIN_RESMI):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    lebar = max(len(e) for e in daftar_email_valid) + 2  
    garis = "+" + karakter_border * lebar + "+"
    baris = [garis]
    for e in daftar_email_valid:
        baris.append("| " + e.ljust(lebar - 2) + " |")
    baris.append(garis)
    return "\n".join(baris)


def main():
    border = input("Masukkan border dengan karakter bebas: ")
    if border == "":
        border = "="
    border = border[0]

    print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

    daftar_valid = []
    while True:
        email = input("Masukkan email: ")
        if email.strip().lower() == "tutup":
            break

        error = deteksi_anomali_email(email)

        if not error and email.lower() in (e.lower() for e in daftar_valid):
            error.append("Email sudah terdaftar (Duplikat).")

        if error:
            print(">> Email DITOLAK karena:")
            for e in error:
                print(f"   - {e}")
        else:
            print(">> Email VALID!")
            daftar_valid.append(email)

    print("\n--- HASIL EMAIL VALID ---")
    if daftar_valid:
        print(cetak_daftar(daftar_valid, border))
    else:
        print("(Tidak ada email valid yang tercatat)")


if __name__ == "__main__": 
    main()