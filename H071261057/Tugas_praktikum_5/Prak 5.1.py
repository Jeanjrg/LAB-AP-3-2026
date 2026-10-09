
def bersihkan_teks(teks):
    hasil = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    for huruf in teks.lower():
        if huruf in alfabet:
            hasil += huruf

    return hasil


def cek_palindrome(teks):
    teks_balik = teks[::-1]

    if teks == teks_balik:
        return True, -1

    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return False, i


def inti_palindrome(teks):
    teks_bersih = bersihkan_teks(teks)

    palindrom_terpanjang = ""
    indeks_awal = 0

    for i in range(len(teks_bersih)):
        for j in range(i + 1, len(teks_bersih) + 1):
            substring = teks_bersih[i:j] #mengambil potongan teks berdasarkan indeks i sampai sebelum indeks j

            hasil_cek, indeks = cek_palindrome(substring)

            if hasil_cek:
                if len(substring) > len(palindrom_terpanjang):
                    palindrom_terpanjang = substring
                    indeks_awal = i

    return {
        "teks": palindrom_terpanjang,
        "panjang": len(palindrom_terpanjang),
        "indeks_awal": indeks_awal
    }


teks = input("Masukkan teks prasasti: ")

teks_bersih = bersihkan_teks(teks)
print("\nTeks Bersih:", teks_bersih)

hasil = inti_palindrome(teks)

print("Output Terharap:", hasil)