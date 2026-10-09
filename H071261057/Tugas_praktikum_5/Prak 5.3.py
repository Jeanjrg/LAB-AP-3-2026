
ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    if ch.lower() not in ALFABET:
        return ch 

    huruf = ch.lower()
    posisi = ALFABET.find(huruf)
    posisi_baru = (posisi + k) % 26 #menghitung posisi baru dengan pergeseran k
    hasil = ALFABET[posisi_baru]

    if ch.isupper(): # jika huruf awalnya kapital, hasil kapital
        return hasil.upper()

    return hasil


def mesin_enkripsi(teks, k): # menggeser seluruh char dlm satu kalimat
    hasil = ""

    for ch in teks: #char dikirim ke fungsi cek_sandi untuk digeser lalu hasinya di tambahakn ke cariabel hasil
        hasil += cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k): # mengembalikan pesan terenskripsi menjadi pesan asli
    return mesin_enkripsi(teks, -k) # knp -? karna untuk mengembalikan pesan asli


def retas_sandi(teks, kata_kunci):
    hasil = []

    for k in range(26):
        pesan_asli = mesin_dekripsi(teks, k)

        if kata_kunci.lower() in pesan_asli.lower():
            hasil.append((k, pesan_asli))

    return hasil


pesan = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")

hasil = retas_sandi(pesan, kata_kunci)

print()
print("Output Deskripsi:", hasil)
