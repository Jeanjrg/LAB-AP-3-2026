
import re

def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim)

def validasi_email(email):
    return re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email)

def validasi_telepon(telepon):
    return re.fullmatch(r"\d{10,13}", telepon)


nim = input("Masukkan NIM: ")
email = input("Masukkan Email: ")
telepon = input("Masukkan Nomor Telepon: ")

if validasi_nim(nim):
    print("NIM valid.")
else:
    print("Format NIM tidak valid!")

if validasi_email(email):
    print("Email valid.")
else:
    print("Format email tidak valid!")

if validasi_telepon(telepon):
    print("Nomor telepon valid.")
else:
    print("Nomor telepon tidak valid!")

if validasi_nim(nim) and validasi_email(email) and validasi_telepon(telepon):
    print("Data mahasiswa berhasil diverifikasi!")
