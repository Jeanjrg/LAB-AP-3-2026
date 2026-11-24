
import re

def validasi_username(username):
    pola = r"[A-Za-z][A-Za-z0-9_]{4,11}"
    return re.fullmatch(pola, username) is not None

daftar_username = []

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
print()

while True:
    username = input("Masukkan username: ")

    if username.upper() == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.")
        daftar_username.append(username)
    else:
        print("Username tidak valid!")

print()
print("=== Rekapitulasi ===")
print("Username valid:")
nomor = 1
for nama in daftar_username:
    print(f"{nomor}. {nama}")
    nomor += 1
 
print()
print("Jumlah username valid:", len(daftar_username))
