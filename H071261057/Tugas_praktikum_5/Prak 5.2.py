
def cek_kata(teks, kata):
    indeks = []
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    start = 0

    while True:
        i = teks_kecil.find(kata_kecil, start)

        if i == -1:
            break

        indeks.append(i)
        start = i + 1

    return indeks


def cek_batas_kata(teks, i, panjang):
    sebelum = i - 1
    sesudah = i + panjang

# memeriksa karakter sebelum kata
    batas_kiri = (
        sebelum < 0
        or not (
            'a' <= teks[sebelum].lower() <= 'z'
        )
    )
# memeriksa karakter setelah kata
    batas_kanan = (
        sesudah >= len(teks)
        or not (
            'a' <= teks[sesudah].lower() <= 'z'
        )
    )

    return batas_kiri and batas_kanan


def sensor_kata(teks, kata, simbol):
    indeks = cek_kata(teks, kata)
    teks_sensor = teks
    jumlah_sensor = 0
    list_indeks_awal = []

    for i in reversed(indeks):
        if cek_batas_kata(teks, i, len(kata)):
            teks_sensor = (
                teks_sensor[:i] #teks sebelum kata
                + simbol * len(kata) #simbol pengganti kata
                + teks_sensor[i + len(kata):] #teks setelah kata
            )

            jumlah_sensor += 1
            list_indeks_awal.append(i)

    list_indeks_awal.reverse()

    return teks_sensor, jumlah_sensor, list_indeks_awal


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(
    teks, kata, simbol
)

print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)