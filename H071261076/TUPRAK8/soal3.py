import re

print("--- Pembersihan Data Nomor Telepon ---")
print()

jumlah = int(input("Masukkan jumlah data: "))

data_sebelum = []

for i in range(jumlah):
    nomor = input(f"Nomor ke-{i+1}: ")
    data_sebelum.append(nomor)

data_sesudah = []
for nomor in data_sebelum:
    bersih = re.sub(r"[\s-]", "", nomor)
    data_sesudah.append(bersih)

print()
print("--- Hasil Pembersihan ---")

jumlah_valid = 0
for i in range(jumlah):
    if re.match(r"^\d{10,13}$", data_sesudah[i]):
        status = "Valid"
        jumlah_valid += 1
    else:
        status = "Tidak valid"

    print()
    print(f"Data {i+1}:")
    print(f"Sebelum : {data_sebelum[i]}")
    print(f"Sesudah : {data_sesudah[i]}")
    print(f"Status  : {status}")

print()
print(f"Jumlah nomor valid: {jumlah_valid}")