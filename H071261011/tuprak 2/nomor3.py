#nomor 3
nilai_tes = float(input("Masukkan nilai tes: "))
pengalaman = float(input("Masukkan pengalaman kerja (tahun): "))

if nilai_tes >= 80:
    print("Lolos ke Tahap Wawancara")
elif nilai_tes >= 65 and pengalaman >= 2:
    print("Lolos Bersyarat")
else:
    print("Tidak Lolos")
