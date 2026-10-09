huruf = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    if ch.lower() in huruf:
        kapital = ch.isupper()
        idx = huruf.find(ch.lower())

        idx_baru = (idx + k)%26
        hasil_char = huruf[idx_baru]

        return hasil_char.upper() if kapital else hasil_char
    else:
        return ch

def mesin_enskripsi(teks, k):
    return "".join(cek_sandi(ch, k) for ch in teks) 

def mesin_deskripsi(teks, k):
    return mesin_enskripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil_retas =[]
    for k in range(26):
        pesan_asli = mesin_deskripsi(sandi, k)
        if pesan_asli.find(kata_kunci) != -1:
            hasil_retas.append((k, pesan_asli))
    return hasil_retas

if __name__ == "__main__":
    while True:
        pesan_tersita = input("Masukkan pesan tersita (enkripsi Caesar): ")
        kata_kunci_target = input("Masukkan kata kunci target: ")
    
        output_deskripsi = retas_sandi(pesan_tersita, kata_kunci_target)
        print(f"Output Deskripsi: {output_deskripsi}")