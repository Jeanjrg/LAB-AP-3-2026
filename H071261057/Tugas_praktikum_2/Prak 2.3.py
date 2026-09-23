Nilai = int(input("masukkan nilai tes:"))
Pengalaman = int(input("masukkan :"))

if Nilai >= 80:
    print("Lolos ke tahap wawancara")
elif Nilai >= 65 and Pengalaman >= 2:
    print("Lolos bersyarat")
else: 
    print("Tidak lolos")