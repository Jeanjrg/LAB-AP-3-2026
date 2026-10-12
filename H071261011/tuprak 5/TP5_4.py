database_email = []

domain_list = (".com", ".id", ".ac.id")


def deteksi_anomali_email(email):
    list_error = []

    
    if " " in email:
        list_error.append("Email tidak boleh memiliki spasi.")

    
    if email.count("@") != 1:
        list_error.append("Harus memiliki tepat satu karakter @.")
        return list_error

    local, domain = email.split("@")

    
    if not local or not domain:
        list_error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

   
    if local.startswith(".") or local.endswith(".") or ".." in local:
        list_error.append("Bagian local tidak boleh diawali atau diakhiri titik, serta tidak boleh mengandung titik berurutan.")

    
    if "." not in domain:
        list_error.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        list_error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    
    if not email.lower().endswith(domain_list):
        list_error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    
    if not list_error and email in database_email:
        list_error.append("Email sudah terdaftar (Duplikat).")

    return list_error


def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return ""

    email_terpanjang = max(len(email) for email in daftar_email_valid)
    lebar_garis = email_terpanjang + 2
    garis_horizontal = karakter_border * lebar_garis

    hasil_bingkai = [f"+{garis_horizontal}+"]
    for email in daftar_email_valid:
        hasil_bingkai.append(f"| {email.ljust(email_terpanjang)} |")
    hasil_bingkai.append(f"+{garis_horizontal}+")

    return "\n".join(hasil_bingkai)



print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
if border == "":
    border = "="

print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

while True:
    email = input("Masukkan email: ")

    if email.lower() == "tutup":
        break

    daftar_error = deteksi_anomali_email(email)

    if daftar_error:
        print(">> Email DITOLAK karena:")
        for pesan in daftar_error:
            print(f"   - {pesan}")
    else:
        print(">> Email VALID!")
        database_email.append(email)

print("\n--- HASIL EMAIL VALID ---")
print(cetak_daftar(database_email, border))