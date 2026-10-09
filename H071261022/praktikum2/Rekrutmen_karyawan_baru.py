nilai = int(input("masukkan nilai tes: "))
pengalaman = int(input("masukkan pengalaman kerja (tahun): "))

if nilai >= 80:
    print("lolos ketahap wawancara")
elif nilai >= 65 and pengalaman >= 2:
    print("lolos bersyarat")
else:
    print("tidak lolos")

