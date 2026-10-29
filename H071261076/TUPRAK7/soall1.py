import os
import random
from datetime import datetime

os.makedirs("invoices", exist_ok=True)


def rupiah(angka):
    return format(angka, ",").replace(",", ".")


def file_ada(nama_file):
    try:
        open(nama_file, "r").close()
        return True
    except:
        return False


def catat_riwayat(waktu, id_transaksi, total):
    if not file_ada("trx_history.txt"):
        with open("trx_history.txt", "w") as file:
            file.write("=" * 66 + "\n")
            file.write("| " + "Waktu".ljust(19)
                       + " | " + "ID Transaksi".ljust(20)
                       + " | " + "Nominal Transaksi".ljust(17) + " |\n")
            file.write("=" * 66 + "\n")

    with open("trx_history.txt", "a") as file:
        file.write("| " + waktu.strftime("%Y-%m-%d %H:%M:%S")
                   + " | " + id_transaksi.ljust(20)
                   + " | " + ("Rp. " + str(total)).ljust(17) + " |\n")
        file.write("=" * 66 + "\n")


def buat_transaksi():
    print("=" * 60)
    print("                 SELAMAT DATANG")
    print("=" * 60)

    nama_kasir = input("Masukkan nama kasir   : ").strip()

    if not nama_kasir:
        print("=" * 60)
        print("Nama kasir tidak boleh kosong!")
        print("=" * 60)
        return

    daftar_produk = []

    while True:
        print("=" * 60)
        nama_produk = input("Masukkan nama produk  : ").strip()

        if not nama_produk:
            print("=" * 60)
            print("Nama produk tidak boleh kosong!")
            print("=" * 60)
            continue

        try:
            harga_produk = int(input("Masukkan harga produk : "))
            jumlah_produk = int(input("Masukkan jumlah produk: "))

            if harga_produk <= 0 or jumlah_produk <= 0:
                print("=" * 60)
                print("Harga dan jumlah harus lebih dari 0!")
                print("=" * 60)
                continue

        except:
            print("=" * 60)
            print("Harga dan jumlah harus berupa angka!")
            print("=" * 60)
            continue

        subtotal_produk = harga_produk * jumlah_produk

        daftar_produk.append([
            nama_produk,
            harga_produk,
            jumlah_produk,
            subtotal_produk
        ])

        print("=" * 60)
        print("Subtotal produk: Rp", rupiah(subtotal_produk))
        print("=" * 60)

        while True:
            tambah = input("Tambah produk? (Y/T)   : ").strip().lower()

            if tambah == "y" or tambah == "t":
                break

            print("=" * 60)
            print("Masukkan Y atau T!")
            print("=" * 60)

        print("=" * 60)

        if tambah == "t":
            break

    total = sum(produk[3] for produk in daftar_produk)

    print("                 RINGKASAN BELANJA")
    print("=" * 60)

    for produk in daftar_produk:
        print("Nama produk           :", produk[0])
        print("Harga produk          : Rp", rupiah(produk[1]))
        print("Jumlah produk         :", produk[2])
        print("Subtotal              : Rp", rupiah(produk[3]))
        print("=" * 60)

    print("TOTAL                 : Rp", rupiah(total))
    print("=" * 60)

    waktu = datetime.now()

    inisial = ""
    for kata in nama_kasir.split():
        inisial += kata[0]

    inisial = inisial.upper()

    while True:
        id_transaksi = (
            inisial
            + waktu.strftime("%y%m%d%H%M")
            + str(random.randint(100, 999))
        )

        nama_file = "invoices/" + id_transaksi + ".txt"

        if not file_ada(nama_file):
            break

    isi_invoice = "=" * 60 + "\n"
    isi_invoice += "                 INVOICE\n"
    isi_invoice += "=" * 60 + "\n"
    isi_invoice += "ID transaksi         : " + id_transaksi + "\n"
    isi_invoice += "Nama kasir           : " + nama_kasir + "\n"
    isi_invoice += "Waktu                : " + waktu.strftime(
        "%Y-%m-%d %H:%M:%S") + "\n"
    isi_invoice += "=" * 60 + "\n"

    for produk in daftar_produk:
        isi_invoice += "Nama produk           : " + produk[0] + "\n"
        isi_invoice += "Harga produk          : Rp " + rupiah(produk[1]) + "\n"
        isi_invoice += "Jumlah produk         : " + str(produk[2]) + "\n"
        isi_invoice += "Subtotal              : Rp " + rupiah(produk[3]) + "\n"
        isi_invoice += "=" * 60 + "\n"

    isi_invoice += "TOTAL                 : Rp " + rupiah(total) + "\n"
    isi_invoice += "=" * 60 + "\n"
    isi_invoice += "              TERIMA KASIH\n"
    isi_invoice += "=" * 60 + "\n"

    with open(nama_file, "w") as file:
        file.write(isi_invoice)

    catat_riwayat(waktu, id_transaksi, total)

    print("                 TRANSAKSI BERHASIL")
    print("=" * 60)


while True:
    print("\n" + "=" * 60)
    print("                   MENU KASIR")
    print("=" * 60)
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print("=" * 60)

    pilihan = input("Masukkan opsi pilihan  : ").strip()

    print("=" * 60)

    if pilihan == "1":
        buat_transaksi()

    elif pilihan == "2":
        id_cari = input("Masukkan ID transaksi: ").strip()

        print("=" * 60)

        try:
            with open("invoices/" + id_cari + ".txt", "r") as file:
                print(file.read())
        except:
            print("Transaksi tidak ditemukan!")

        print("=" * 60)

    elif pilihan == "3":
        print("Terima Kasih!")
        print("=" * 60)
        break

    else:
        print("Pilihan tidak valid!")
        print("=" * 60)