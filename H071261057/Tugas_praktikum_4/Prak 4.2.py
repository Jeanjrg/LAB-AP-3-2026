nilai_siswa = []

while True:
    Nilai = input("Masukan nilai ujian siswa (kosongkan untuk selesai  ): ")

    if not Nilai:
        break

    Nilai = int(Nilai)
    nilai_siswa.append(Nilai)



def add(*args):
    if not args:
        return None, None, None
    rata_rata = sum(args) / len(args)
    tinggi = max(args)
    rendah = min(args)
    return rata_rata, tinggi, rendah

rata_rata, tinggi, rendah = add(*nilai_siswa)

print ("rata-rata kelas : ", rata_rata)
print ("nilai tertinggi : ", tinggi)
print ("nilai terendah : ", rendah)



