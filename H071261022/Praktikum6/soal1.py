alfabet  = "abcdefghijklmnopqrstuvwxyz"

teks = input("Masukkan teks prasasti: ")
print()

def bersihkan_teks(teks):
    teks = teks.lower()
    hasil = ""
    for huruf in teks:
        huruf_kecil = huruf.lower()
        if huruf_kecil in alfabet:
            hasil += huruf_kecil
    return hasil

def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    else:
        for posisi in range(len(teks)):
            if teks[posisi] != terbalik[posisi]:
                return (False, 1)

def inti_palinrome(teks):
    bersih = bersihkan_teks(teks)
    terpanjang = ""
    indeks_awal = 0

    for mulai in range(len(bersih)):
        for berhenti in range(mulai + 1, len(bersih) + 1):
            potongan = bersih[mulai:berhenti]
            hasil_cek = cek_palinrome(potongan)
            if hasil_cek[0] == True and len(potongan) > len(terpanjang):
                terpanjang = potongan
                indeks_awal = mulai
    return {"teks": terpanjang, "panjang": len(terpanjang), "indeks_awal": indeks_awal}


print("Teks Bersih:", bersihkan_teks(teks))
print("Output Terharap:", inti_palinrome(teks))

