def konversi_suhu(suhu, asal, tujuan):
    if asal not in ["C", "F", "K"] or tujuan not in ["C", "F", "K"]:
        raise ValueError("Skala suhu tidak dikenali")
    
    if asal == 'C':
        celsius = suhu
    elif asal == 'F':
        celsius = (suhu - 32) * 5/9
    elif asal == 'K':
        celsius = suhu - 273.15

    if tujuan == 'C':
        hasil = celsius
    elif tujuan == 'F':
        hasil = (celsius * 9/5) + 32
    elif tujuan == 'K':
        hasil = celsius + 273.15
    
    return hasil

print("== Konversi Suhu ==")
while True:
    suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if suhu == 'selesai':
        break

    try:
        suhu = float(suhu)
        Skala_asal = input("masukkan skala asal (C/F/K) : ")
        Skala_tujuan = input("masukkan skala tujuan (C/F/K) : ")
        hasil = konversi_suhu(suhu, Skala_asal, Skala_tujuan)
        print("Hasil:", suhu, Skala_asal, "=", hasil, Skala_tujuan)
    except ValueError as error:
        print("Error:", error)