def konversi_suhu(suhu, asal, tujuan):
    skala_valid = ("C", "F", "K")
    if asal not in skala_valid or tujuan not in ['C', 'F', 'K']:
        raise("Error: Skala suhu tidak dikenal.")

    if skala_asal == 'C':
        celsius = suhu
    elif skala_asal == 'F':
        celsius = (suhu - 32) * 5/9
    elif skala_asal == 'K':
        celsius = suhu - 273.15
        
    if skala_tujuan == 'C':
        return celsius
    elif skala_tujuan == 'F':
        return (celsius * 9/5) + 32
    elif skala_tujuan == 'K':
        return celsius + 273.15

print("=== Konversi Suhu ===")
while True:
    masukkan = input("Masukkan suhu (atau 'selesai' untuk keluar): ")   
    if masukkan == 'selesai':
        break
        
    try:
        suhu = float(masukkan)
    except:
        print("Input tidak valid, suhu harus berupa angka.")
        continue

    skala_asal = input("Skala asal (C/F/K): ").upper()
    skala_tujuan = input("Skala tujuan (C/F/K): ").upper()
    try:
        hasil= konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
    except:
        print("Eror: Skala suhu tidak dikenali.")