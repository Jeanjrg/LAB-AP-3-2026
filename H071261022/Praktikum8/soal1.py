import re

def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim) 

def validasi_email(email):
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email) 

def validasi_telepon(telepon):
    return re.fullmatch(r"\d{10,13}", telepon) 

print("=== Validasi Data Mahasiswa ===")
print()
nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
telepon = input("Masukkan No. Telp  : ")

print()
print("--- Hasil Validasi ---")

semua_valid = True

if validasi_nim(nim):
    print("NIM         : Valid")
else:
    print("NIM         : Format NIM tidak valid!")
    semua_valid = False

if validasi_email(email):
   print("Email       : Valid")
else:
    print("Email       : Format email tidak valid!")
    semua_valid = False

if validasi_telepon(telepon):
    print("No. Telepon : Valid")
else:
    print("No. Telepon : Nomor telepon tidak valid!")
    semua_valid = False

if semua_valid:
    print("Data mahasiswa berhasil diverifikasi!")
