
import os
import random
from datetime import datetime

# Membuat folder invoices
if not os.path.exists("invoices"):
    os.makedirs("invoices")


def buat_invoice():
    kasir = input("Nama kasir: ")
    produk = []
    total = 0

    # Input barang
    while True:
        nama = input("Nama produk: ")
        harga = int(input("Harga produk: "))
        jumlah = int(input("Jumlah produk: "))

        subtotal = harga * jumlah
        total += subtotal

        produk.append((nama, harga, jumlah, subtotal))

        lagi = input("Tambah produk? (y/n): ")
        if lagi.lower() != "y":
            break

    # Membuat ID transaksi
    waktu = datetime.now()
    inisial = "".join(
        kata[0] for kata in kasir.split()
    ).upper()

    id_trx = (
        inisial
        + waktu.strftime("%y%m%d%H%M")
        + str(random.randint(100, 999))
    )

    nama_file = "invoices/" + id_trx + ".txt"

    # Membuat isi invoice
    isi = ""
    isi += "=" * 40 + "\n"
    isi += "           INVOICE BELANJA\n"
    isi += "=" * 40 + "\n"
    isi += "ID Transaksi : " + id_trx + "\n"
    isi += "Waktu        : " + waktu.strftime("%Y-%m-%d %H:%M:%S") + "\n"
    isi += "Kasir        : " + kasir + "\n"
    isi += "-" * 40 + "\n"

    for nama, harga, jumlah, subtotal in produk:
        isi += nama + "\n"
        isi += "  " + str(jumlah) + " x Rp" + format(harga, ",").replace(",", ".") + "\n"
        isi += "  Subtotal: Rp" + format(subtotal, ",").replace(",", ".") + "\n"

    isi += "-" * 40 + "\n"
    isi += "TOTAL: Rp" + format(total, ",").replace(",", ".") + "\n"
    isi += "=" * 40 + "\n"
    isi += "       Terima kasih!\n"
    isi += "=" * 40 + "\n"

    # Menyimpan invoice
    with open(nama_file, "w") as file:
        file.write(isi)

    print("\n" + isi)
    print("Invoice berhasil disimpan:", nama_file)

    # Mencatat riwayat transaksi
    file_baru = not os.path.exists("trx_history.txt")

    with open("trx_history.txt", "a") as file:
        if file_baru:
            file.write(
                f"{'Waktu':20} | {'ID Transaksi':18} | Nominal\n"
            )
            file.write("-" * 65 + "\n")

        file.write(
            f"{waktu.strftime('%Y-%m-%d %H:%M:%S'):20} | "
            f"{id_trx:18} | Rp{total}\n"
        )

    print("Riwayat transaksi berhasil dicatat.")


def cari_invoice():
    id_trx = input("Masukkan ID transaksi: ")
    nama_file = "invoices/" + id_trx + ".txt"

    if os.path.exists(nama_file):
        with open(nama_file, "r") as file:
            print("\n" + file.read())
    else:
        print("Invoice tidak ditemukan.")


def lihat_riwayat():
    if os.path.exists("trx_history.txt"):
        with open("trx_history.txt", "r") as file:
            print("\n" + file.read())
    else:
        print("Belum ada riwayat transaksi.")


# Menu utama
while True:
    print("\n===== APLIKASI KASIR =====")
    print("1. Buat invoice")
    print("2. Cari invoice")
    print("3. Lihat riwayat transaksi")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        buat_invoice()
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        lihat_riwayat()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")