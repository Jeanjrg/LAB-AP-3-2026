def cek_kata(teks, kata):
    indeks = []
    start = 0
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    while True:
        idx = teks_lower.find(kata_lower, start)
        if idx == -1:
            break
        indeks.append(idx)
        start = idx + 1
    return indeks

def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sebelum_ok = (i == 0) or (teks[i - 1] not in alfabet)
    sesudah_ok = (i + panjang == len(teks)) or (teks[i + panjang] not in alfabet)
    return sebelum_ok and sesudah_ok

def sensor_kata(teks, kata, simbol):
    indeks_ditemukan = cek_kata(teks, kata)
    p = len(kata)
    indeks_valid = [i for i in indeks_ditemukan if cek_batas_kata(teks, i, p)]
    
    teks_baru = ""
    idx_sekarang = 0
    for i in indeks_valid:
        teks_baru += teks[idx_sekarang:i] + (simbol * p)
        idx_sekarang = i + p
    teks_baru += teks[idx_sekarang:]
    
    return teks_baru, len(indeks_valid), indeks_valid

# Program Utama
t = input("Masukkan Teks: ")
k = input("Masukkan kata target: ")
s = input("Masukkan simbol: ")
hasil_teks, jumlah, list_idx = sensor_kata(t, k, s)
print(f"Hasil Teks: {hasil_teks}")
print(f"Jumlah: {jumlah}  Indeks: {list_idx}")