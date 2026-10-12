
alfabet = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k): # k itu jumlah geser
    nomor_ch = alfabet.find(ch.lower())
    if nomor_ch == -1:                       
        return ch
    nomor_baru = (nomor_ch + k) % 26 
    ch_baru = alfabet[nomor_baru]

    if ch == ch.upper():
        return ch_baru.upper()
    return ch_baru.lower()


def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:                                    
        hasil = hasil + cek_sandi(ch, k)
    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []                                   
    
    for kunci in range(26):                       
        percobaan = mesin_dekripsi(sandi, kunci)  

        if percobaan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((kunci, percobaan))      
    return hasil

sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")
print()
print(f"Output Deskripsi:", retas_sandi(sandi, kata_kunci))