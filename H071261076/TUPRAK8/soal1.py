import re

def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim) is not None

def validasi_email(email):
    return re.fullmatch(r"[\w.]+@[\w-]+\.[a-zA-Z]+", email) is not None

def validasi_telp(telp):
    return re.fullmatch(r"\d{10,13}", telp) is not None

print("=== Validasi Data Mahasiswa ===")
print()
nim = input("Masukkan NIM      : ")
email = input("Masukkan Email    : ")
telp = input("Masukkan No. Telp : ")

print()
print("--- Hasil Validasi ---")

nim_ok = validasi_nim(nim)
email_ok = validasi_email(email)
telp_ok = validasi_telp(telp)

print("NIM         :", "Valid" if nim_ok else "Format NIM tidak valid!")
print("Email       :", "Valid" if email_ok else "Format email tidak valid!")
print("No. Telepon :", "Valid" if telp_ok else "Nomor telepon tidak valid!")

print()
if nim_ok and email_ok and telp_ok:
    print("Data mahasiswa berhasil diverifikasi!")