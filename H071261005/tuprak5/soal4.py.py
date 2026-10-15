def deteksi_anomali_email(email):
    error = []
    if email.count('@') != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error
    
    local, domain = email.split('@')
    
    if not local or not domain:
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
    if ' ' in email:
        error.append("Tidak boleh mengandung spasi di posisi manapun.")
    if local.startswith('.') or local.endswith('.') or '..' in local:
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")
    if '.' not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if '..' in domain or domain.endswith('.'):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
    if not (domain.endswith('.com') or domain.endswith('.id') or domain.endswith('.ac.id')):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")
        
    return error

def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return
    max_len = max(len(e) for e in daftar_email_valid)
    border_line = karakter_border * (max_len + 4)
    print("+" + border_line[1:-1] + "+")
    print("HASIL EMAIL VALID")
    print("+" + border_line[1:-1] + "+")
    for email in daftar_email_valid:
        print(f"| {email.ljust(max_len)} |")
    print("+" + border_line[1:-1] + "+")

# Program Utama
print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []
while True:
    inp = input("Masukkan email: ").strip()
    if inp.lower() == "tutup":
        break
    
    if inp in daftar_valid:
        print(">> Email DITOLAK karena:\nEmail sudah terdaftar (Duplikat).")
        continue
        
    anomali = deteksi_anomali_email(inp)
    if not anomali:
        print(">> Email VALID!")
        daftar_valid.append(inp)
    else:
        print(">> Email DITOLAK karena:")
        for err in anomali:
            print(err)

cetak_daftar(daftar_valid, border)