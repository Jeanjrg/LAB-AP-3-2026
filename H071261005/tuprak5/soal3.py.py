ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    ch_lower = ch.lower()
    idx = ALFABET.find(ch_lower)
    if idx == -1:
        return ch
    idx_baru = (idx + k) % 26
    karakter_baru = ALFABET[idx_baru]
    return karakter_baru.upper() if ch.isupper() else karakter_baru

def mesin_enkripsi(teks, k):
    return "".join(cek_sandi(ch, k) for ch in teks)

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil

# Program Utama
sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kunci = input("Masukkan kata kunci target: ")
print("Output Deskripsi:", retas_sandi(sandi, kunci))