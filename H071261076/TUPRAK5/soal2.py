def cek_batas_kata(teks, i, panjang):
    if i > 0:
        kiri = teks[i-1]
        if ('a' <= kiri <= 'z') or ('A' <= kiri <= 'Z'):
            return False

    indeks_kanan = i + panjang
    if indeks_kanan < len(teks):
        kanan = teks[indeks_kanan]
        if ('a' <= kanan <= 'z') or ('A' <= kanan <= 'Z'):
            return False

    return True

def cek_kata(teks, kata,):
    teks_lower = teks.lower()
    kata_lower = kata.lower()

    indeks_list = []
    start = 0
    panjang = len(kata)

    while True:
        pos = teks_lower.find(kata_lower, start) 
        if pos == -1:
            break

        if cek_batas_kata(teks, pos, panjang):
            indeks_list.append(pos)

        start = pos + 1 

    return indeks_list

def sensor_kata(teks, kata, simbol):
    indeks_awal = cek_kata(teks, kata)
    jumlah = len(indeks_awal)

    if jumlah == 0:
        return teks, 0, []

    teks_tersensor = ""
    last_idx = 0 
    panjang = len(kata)
    simbol_pengganti = simbol * panjang

    for idx in indeks_awal:
        teks_tersensor += teks[last_idx:idx] + simbol_pengganti
        last_idx = idx + panjang

    teks_tersensor += teks[last_idx:]

    return teks_tersensor, jumlah, indeks_awal

if __name__ == "__main__":
    teks_input = "Elang melihat belalang. Si elang super-elang terbang."
    kata_target = "elang"
    simbol_input = "*"

    hasil_teks, jumlah, indeks = sensor_kata(teks_input, kata_target, simbol_input)

    print(f"Masukkan Teks: {teks_input}")
    print(f"Masukkan kata target: {kata_target}")
    print(f"Masukkan simbol: {simbol_input}")
    print(f"Hasil Teks: {hasil_teks}")
    print(f"Jumlah: {jumlah} | Indeks: {indeks}")
