def rekap_nilai(*args):
    if not args:
        return None, None, None
    
    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)
    
    return rata_rata, nilai_tertinggi, nilai_terendah

def main():
    daftar_nilai = []
    
    while True:
        input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ").strip()
        if input_nilai == "":
            break
        
        # Mengubah ke int jika bilangan bulat, atau float jika desimal
        nilai = float(input_nilai)
        if nilai.is_integer():
            nilai = int(nilai)
        daftar_nilai.append(nilai)

    if not daftar_nilai:
        print("Data nilai tidak tersedia.")
    else:
        rata, tinggi, rendah = rekap_nilai(*daftar_nilai)
        print(f"Rata-rata kelas: {rata}")
        print(f"Nilai tertinggi: {tinggi}")
        print(f"Nilai terendah: {rendah}")

if __name__ == "__main__":
    main()