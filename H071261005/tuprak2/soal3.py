nilai_tes = float(input("Masukkan nilai tes: "))
if nilai_tes >= 80:
    print("Lolos ke Tahap Wawancara")
else:
    pengalaman_kerja = int(input("masukkan pengalaman kerja: "))

    if pengalaman_kerja >= 2 and nilai_tes >= 65:
        print("anda lolos bersyarat")