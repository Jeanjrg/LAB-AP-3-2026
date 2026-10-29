import os
import random
from datetime import datetime

def get_inisial(nama_kasir):
    """Mengambil inisial nama kasir dalam huruf kapital."""
    words = nama_kasir.strip().split()
    if len(words) >= 3:
        inisial = "".join([w[0].upper() for w in words[:3]])
    elif len(words) == 2:
        inisial = words[0][0].upper() + words[1][:2].upper()
    else:
        inisial = nama_kasir[:3].upper() if len(nama_kasir) >= 3 else nama_kasir.upper()
    return inisial

def buat_invoice():
    print("\n" + "="*40)
    print("      BUAT INVOICE TRANSAKSI BARU")
    print("="*40)
    nama_kasir = input("Masukkan Nama Kasir: ").strip()
    if not nama_kasir:
        print("Nama kasir tidak boleh kosong!")
        return

    items = []
    total_nominal = 0

    # Input produk (bisa lebih dari satu)
    while True:
        nama_produk = input("Masukkan Nama Produk (ketik 'selesai' untuk mengakhiri): ").strip()
        if nama_produk.lower() == 'selesai':
            break
        if not nama_produk:
            print("Nama produk tidak boleh kosong.")
            continue
        
        try:
            harga = float(input(f"Masukkan Harga {nama_produk}: "))
            jumlah = int(input(f"Masukkan Jumlah {nama_produk}: "))
            if harga < 0 or jumlah <= 0:
                print("Harga tidak boleh negatif dan jumlah harus lebih dari 0.")
                continue
        except ValueError:
            print("Input harga atau jumlah harus berupa angka!")
            continue

        subtotal = harga * jumlah
        items.append({
            'nama': nama_produk,
            'harga': harga,
            'jumlah': jumlah,
            'subtotal': subtotal
        })
        total_nominal += subtotal
        print(f"-> Ditambahkan: {nama_produk} ({jumlah}x) = Rp. {subtotal:,.0f}\n")

    if not items:
        print("Transaksi dibatalkan karena tidak ada produk yang diinput.")
        return

    # Buat folder 'invoices' jika belum ada
    if not os.path.exists("invoices"):
        os.makedirs("invoices")

    # Format waktu & ID Transaksi
    now = datetime.now()
    tahun = now.strftime("%y")
    bulan = now.strftime("%m")
    tanggal = now.strftime("%d")
    waktu_hm = now.strftime("%H%M")
    waktu_lengkap = now.strftime("%Y-%m-%d %H:%M:%S")

    inisial_kasir = get_inisial(nama_kasir)
    rand_num = random.randint(100, 999)

    # Susun ID Transaksi (Inisial + YY + MM + DD + HHMM + Random 3 digit)
    id_transaksi = f"{inisial_kasir}{tahun}{bulan}{tanggal}{waktu_hm}{rand_num}"
    nama_file = f"{id_transaksi}.txt"
    filepath = os.path.join("invoices", nama_file)

    # Isi teks invoice
    invoice_content = f"""========================================
             STRUK BELANJA
========================================
ID Transaksi : {id_transaksi}
Waktu        : {waktu_lengkap}
Kasir        : {nama_kasir}
----------------------------------------
Daftar Produk:
"""
    for item in items:
        invoice_content += f"- {item['nama']} ({item['jumlah']}x) @ Rp. {item['harga']:,.0f} = Rp. {item['subtotal']:,.0f}\n"

    invoice_content += f"""----------------------------------------
Total Belanja: Rp. {total_nominal:,.0f}
========================================
     TERIMA KASIH TELAH BERBELANJA
========================================
"""

    # Simpan invoice ke file txt
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(invoice_content)

    # Simpan ke riwayat transaksi (Soal 3)
    simpan_riwayat(waktu_lengkap, id_transaksi, total_nominal)

    print(f"\n[SUKSES] Invoice berhasil dibuat dan disimpan sebagai: {nama_file}")
    print("\nPreview Invoice:")
    print(invoice_content)

def simpan_riwayat(waktu, id_trx, nominal):
    """Menyimpan ringkasan transaksi ke file trx_history.txt dalam format tabel."""
    history_file = "trx_history.txt"
    file_exists = os.path.exists(history_file)

    with open(history_file, "a", encoding="utf-8") as f:
        if not file_exists:
            # Header Tabel
            f.write("="*75 + "\n")
            f.write(f"| {'Waktu':<20} | {'ID Transaksi':<20} | {'Nominal Transaksi':<22} |\n")
            f.write("="*75 + "\n")
        
        f.write(f"| {waktu:<20} | {id_trx:<20} | Rp. {nominal:<19,.0f} |\n")
        f.write("="*75 + "\n")

def cari_invoice():
    print("\n" + "="*40)
    print("         CARI INVOICE TRANSAKSI")
    print("="*40)
    id_trx = input("Masukkan ID Transaksi (contoh: KLS2308291250123): ").strip()
    if not id_trx:
        print("ID Transaksi tidak boleh kosong.")
        return

    filepath = os.path.join("invoices", f"{id_trx}.txt")
    if os.path.exists(filepath):
        print(f"\n[DITEMUKAN] Menampilkan isi invoice untuk ID: {id_trx}\n")
        with open(filepath, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print(f"\n[GAGAL] Invoice dengan ID '{id_trx}' tidak ditemukan di folder 'invoices'.")

def lihat_riwayat():
    print("\n" + "="*40)
    print("           RIWAYAT TRANSAKSI")
    print("="*40)
    history_file = "trx_history.txt"
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Belum ada riwayat transaksi yang tercatat.")

def main():
    while True:
        print("\n========================================")
        print("      APLIKASI KASIR SEDERHANA          ")
        print("========================================")
        print("1. Buat Invoice Tr\ansaksi Baru (Soal 1)")
        print("2. Cari Invoice Berdasarkan ID (Soal 2)")
        print("3. Lihat Riwayat Transaksi (Soal 3)")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == '1':
            buat_invoice()
        elif pilihan == '2':
            cari_invoice()
        elif pilihan == '3':
            lihat_riwayat()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi kasir!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 4.")

main()