
import re

def validasi_username(username):
    pola = r"[a-zA-Z][a-zA-Z0-9_]{4,11}"
    return re.fullmatch(pola, username)

daftar_username = []

while True:
    username = input("Masukkan username (SELESAI untuk berhenti): ")

    if username == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.")
        daftar_username.append(username)
    else:
        print("Username tidak valid!")

print("\nUsername Valid:")
for nama in daftar_username:
    print(nama)

print("Jumlah username valid:", len(daftar_username))
