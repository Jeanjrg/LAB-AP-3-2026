import re

def validasi_username(username):
    pola = r"[A-Za-z][A-Za-z0-9_]{4,11}"
    return re.fullmatch(pola, username) is not None

daftar_valid = []

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.\n")

while True:
    username = input("Masukkan username: ")

    if username == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.")
        daftar_valid.append(username)
    else:
        print("Username tidak valid!")
    print()

print("\n=== Rekapitulasi ===")
print("Username valid:")
for i, nama in enumerate(daftar_valid, 1): #membuatperulanganuntuk mendapatkan nomor urutnya
    print(f"{i}. {nama}")

print(f"\nJumlah username valid: {len(daftar_valid)}")