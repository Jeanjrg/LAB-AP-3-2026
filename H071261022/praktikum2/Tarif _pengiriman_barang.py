jarak = int(input("masukkan jarak penggiriman (km): "))
express = input("layanan express (ya/tidak): ")

if jarak < 5:
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
else:
    jarak = 35000

layanan = 15000 if express == "ya" else 0
tarif = tarif + layanan
print(f"total tarif pengiriman: Rp{tarif}")