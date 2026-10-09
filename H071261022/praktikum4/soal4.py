
def konversi_suhu(suhu, asal, tujuan):
    skala_valid = ("C", "F", "K") 
    if asal not in skala_valid or tujuan not in skala_valid: 
        raise("Skala suhu tidak dikenali.") 
    
    if asal == "C": #Celsius
        celsius = suhu
    elif asal == "F": #Fahrenheit
        celsius = (suhu - 32) * 5 / 9 #rumus
    else: #Kelvin
        celsius = suhu - 273.15 #rumus
#----------------------------------------------------
    if tujuan == "C":
        hasil = celsius
    elif tujuan == "F":
        hasil = celsius * 9 / 5 + 32
    else:
        hasil = celsius + 273.15
    return round(hasil, 2)


print("=== Konversi Suhu ===")
while True:
    masukan = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if masukan == "selesai":
        break
    try:
        suhu = float(masukan) #harus angaka
    except:
        print("Input tidak valid, suhu harus berupa angka.")
        continue

    skala_asal = input("Skala asal (C/F/K): ").upper() #emngubah menjadi huruf besar
    skala_tujuan = input("Skala tujuan (C/F/K): ").upper()
    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
    except:
        print("Error: Skala suhu tidak dikenali.")