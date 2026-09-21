jarak = float(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ").strip().lower()

# Menentukan tarif dasar
if jarak < 5:
    tarif_dasar = 10000
elif jarak <= 20:
    tarif_dasar = 20000
else:
    tarif_dasar = 35000

# Menentukan biaya tambahan menggunakan ternary operator
biaya_express = 15000 if express == "ya" else 0

total_tarif = tarif_dasar + biaya_express
print(f"Total tarif pengiriman: Rp{total_tarif}")