def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_valid = {'C', 'F', 'K'}
    
    skala_asal = skala_asal.upper()
    skala_tujuan = skala_tujuan.upper()

    if skala_asal not in skala_valid or skala_tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    # Konversi skala asal ke Celsius
    if skala_asal == 'C':
        celsius = suhu
    elif skala_asal == 'F':
        celsius = (suhu - 32) * 5 / 9
    elif skala_asal == 'K':
        celsius = suhu - 273.15

    # Konversi dari Celsius ke skala tujuan
    if skala_tujuan == 'C':
        hasil = celsius
    elif skala_tujuan == 'F':
        hasil = (celsius * 9 / 5) + 32
    elif skala_tujuan == 'K':
        hasil = celsius + 273.15

    return hasil, skala_asal, skala_tujuan

def main():
    print("=== Konversi Suhu ===")
    while True:
        input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ").strip()
        if input_suhu.lower() == 'selesai':
            break
        
        suhu = float(input_suhu)
        skala_asal = input("Skala asal (C/F/K): ").strip()
        skala_tujuan = input("Skala tujuan (C/F/K): ").strip()

        try:
            hasil, asal, tujuan = konversi_suhu(suhu, skala_asal, skala_tujuan)
            print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")
        except ValueError as e:
            print(f"Error: {e}")


main()