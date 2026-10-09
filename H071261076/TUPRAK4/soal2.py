def rekap_nilai(*args):
    if len(args) == 0:
        return 
    
    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)
    
    return rata_rata, nilai_tertinggi, nilai_terendah

daftar_nilai = []

while True:
    user_input = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    
    if user_input == "":
        break
    
    try:
        nilai = float(user_input)
        daftar_nilai.append(nilai)
    except:
        print("Masukkan angka yang valid!")

hasil = rekap_nilai(*daftar_nilai)

if isinstance(hasil, str):
    print(hasil)
else:
    rata, tertinggi, terendah = hasil
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")