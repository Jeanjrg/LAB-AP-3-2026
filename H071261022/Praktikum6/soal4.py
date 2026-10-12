def deteksi_anomali_email(email):
    daftar_error = []   
    if " " in email:
        daftar_error.append("Tidak boleh mengandung spasi.")

    if email.count("@") != 1:
        daftar_error.append("Harus memiliki tepat satu karakter @.")
        return daftar_error   
    
    dua_bagian = email.split("@")
    bagian_local = dua_bagian[0]    
    bagian_domain = dua_bagian[1]   


    if bagian_local == "" or bagian_domain == "":
        daftar_error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if bagian_local.startswith(".") or bagian_local.endswith(".") or ".." in bagian_local:
        daftar_error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    if "." not in bagian_domain:
        daftar_error.append("Bagian domain wajib memiliki minimal satu titik.")
    
    if ".." in bagian_domain or bagian_domain.endswith("."):
        daftar_error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    nama_domain = bagian_domain.split(".")[0]
    if nama_domain != "" and nama_domain != "gmail" and "gmail".find(nama_domain) == 0:
        daftar_error.append("Domain gmail tidak lengkap, seharusnya gmail.com.")

    if not (email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")):
        daftar_error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return daftar_error


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:          
        return "(tidak ada email valid)"

    panjang_terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > panjang_terpanjang:
            panjang_terpanjang = len(email)

    garis = "+" + karakter_border * (panjang_terpanjang + 2) + "+"

    hasil = garis + "\n"                      
    for email in daftar_email_valid:
        
        hasil = hasil + "| " + email.ljust(panjang_terpanjang) + " |\n"
    hasil = hasil + garis
    return hasil


print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
if border == "":
    border = "="          
border = border[0]        
print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []         

while True:               
    email = input("Masukkan email: ")
    if email.lower() == "tutup" or email == "":
        break             

    daftar_error = deteksi_anomali_email(email)   

    if email in daftar_valid:
        daftar_error.append("Email sudah terdaftar (Duplikat).")

    if len(daftar_error) == 0:             
        print(">> Email VALID!")
        daftar_valid.append(email)
    else:                                  
        print(">> Email DITOLAK karena:")
        for pesan in daftar_error:
            print("   -", pesan)

print()
print("--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_valid, border))