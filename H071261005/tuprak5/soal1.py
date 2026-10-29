def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""
    for ch in teks:
        ch_lower = ch.lower()
        if ch_lower in alfabet:
            hasil += ch_lower
    return hasil

def cek_palinrome(teks):
    teks_balik = "".join(reversed(teks))
    if teks == teks_balik:
        return True, -1
    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return False, i

def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)
    n = len(teks_bersih)
    max_len = 0
    hasil = {"teks": "", "panjang": 0, "indeks_awal": 0}
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks_bersih[i:j]
            is_pal, _ = cek_palinrome(sub)
            if is_pal and len(sub) > max_len:
                max_len = len(sub)
                hasil = {"teks": sub, "panjang": len(sub), "indeks_awal": i}
    return teks_bersih, hasil

# Program Utama
inp = input("Masukkan teks prasasti: ")
tb, res = inti_palinrome(inp)
print("Teks Bersih:", tb)
print("Output Terharap:", res)