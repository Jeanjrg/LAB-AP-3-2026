
import re

print("=== Pembersihan Data Nomor Telepon ===")

sebelum = []
sesudah = []
status = []

jumlah = int(input("\nMasukkan jumlah data: "))

for i in range(jumlah):
    nomor = input("Nomor ke-" + str(i + 1) + ": ")

    sebelum.append(nomor)

    bersih = re.sub(r"[ -]", "", nomor)
    sesudah.append(bersih)

    if re.fullmatch(r"\d{10,13}", bersih):
        status.append("Valid")
    else:
        status.append("Tidak valid")


print("\n--- Hasil Pembersihan ---")

total_valid = 0

for i in range(jumlah):
    print("\nData", i + 1)
    print("Sebelum :", sebelum[i])
    print("Sesudah :", sesudah[i])
    print("Status  :", status[i])

    if status[i] == "Valid":
        total_valid += 1

print("\nJumlah nomor valid:", total_valid)
