from datetime import datetime # untuk mengambil tanggal & waktu saat ini
import random # untuk membuat angka acak (bagian akhir ID transaksi)
import os #untuk mengatur folder dan file

folder_saat_ini = os.path.dirname(os.path.abspath(__file__)) #Mengambil alamat lengkap file program
folder_invoices = os.path.join(folder_saat_ini, "invoices") #folder penyimpanan invoice
file_history = os.path.join(folder_saat_ini, "trx_history.txt") #file riwayat transaksi
os.makedirs(folder_invoices, exist_ok=True) #Buat folder "invoices". exist_ok=True artinya: kalau foldernya sudah ada, jangan error.

def membuat_invoices(kasir, data_produk):
    # buat id transsaksi
    waktu_sekarang = datetime.now().strftime("%Y%m%d%H%M%S")
    id_nama = kasir[:3].upper()
    id_tahun = waktu_sekarang[2:4]
    id_bulan = waktu_sekarang[4:6]
    id_tanngal = waktu_sekarang[6:8]
    id_jam_menit = waktu_sekarang[8:12]
    angka_random = random.randint(100, 999)

    border = "=" * 79
    tabel1 = f"|{'NAMA':^38}|{'HARGA':^14}|{'JUMLAH':^8}|{'TOTAL':^14}|"
    total_keseluruhan = 0

    nama_file = f"{id_nama}{id_tahun}{id_bulan}{id_tanngal}{id_jam_menit}{angka_random}.txt"
    file_dalam_folder = os.path.join(folder_invoices, nama_file)

    with open(file_dalam_folder, "w") as a: 
        # Tabel  ID transakdi =============================================================================================================
        # tabel toko
        a.write(f"TOKO {kasir.upper()}".center(100))
        a.write("\n")
        a.write("=" * 100)
        a.write("\nNama kasir".ljust(20) + f": {kasir}")
        a.write("\nWaktu transaksi".ljust(20) + f": {id_tanngal}/{id_bulan}/{id_tahun} {waktu_sekarang[8:10]}:{waktu_sekarang[10:12]}")
        a.write("\n")
        a.write("=" * 100)
        a.write("\n")

        # daftar produk
        a.write("\n" + "Daftar Produk".center(100) + "\n")

        # border awal
        a.write("\n" + border.center(100))
        a.write("\n" + tabel1.center(100))
        a.write("\n" + border.center(100))

        # tabel kedua
        for i in data_produk:
            total_item = i["Harga"] * i["Jumlah"]
            hasil = f"| {i['Nama']:<37}|{'Rp' + str(i['Harga']):>13} |{i['Jumlah']:^8}|{'Rp' + str(total_item):>13} |"
            a.write("\n" + hasil.center(100))
            total_keseluruhan += total_item

        # tabel total
        border_total = "|" + "TOTAL".center(38) + "|".rjust(25) + f"Rp{total_keseluruhan}".rjust(13) + " |"
        a.write("\n" + border.center(100))
        a.write("\n" + border_total.center(100))
        a.write("\n" + border.center(100))

        # tabel terimkasih
        a.write("\n\n")
        a.write("=" * 100)
        a.write("\n" + "TERIMAKASIH TELAH BELANJA".center(100))
        a.write("\n" + "=" * 100 + "\n")

    # utuk file trx_history
    with open(file_history, "a") as isi:
        isi.write("\n" + ("=" * 90))
        waktu = f"{id_tanngal}/{id_bulan}/{id_tahun} {waktu_sekarang[8:10]}:{waktu_sekarang[10:12]}"
        id_trx = f"{id_nama}{id_tahun}{id_bulan}{id_tanngal}{id_jam_menit}{angka_random}"
        isi.write(f"\n| {waktu:<28}| {id_trx:<29}|{'Rp' + str(total_keseluruhan):>26} |")
        isi.write("\n" + ("=" * 90))

    print("=" * 54)
    print("TRANSAKSI BERHASIL".center(54))

print("=" * 54)
print("SELAMAT DATANG".center(54))
print("=" * 54)
nama_kasir = input("Masukkan nama kasir".ljust(35) + ": ")

while True:
    print("=" * 54)
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. keluar")
    print("=" * 54)
    pilih_opsi = input("Masukkan opsi pilihan".ljust(35) + ": ")
    print("=" * 54)

    if pilih_opsi == "1":
        data_list = []

        while True:
            try:
                nama_produk = input("Masukkan nama produk".ljust(35) + ": ")
                harga_produk = int(input("Masukkan harga produk".ljust(35) + ": "))
                jumlah_produk = int(input("Masukkan jumlah produk".ljust(35) + ": "))

                data = {
                    "Nama": nama_produk,
                    "Harga": harga_produk,
                    "Jumlah": jumlah_produk,
                    }
                data_list.append(data)
                
                Tambah = True
                Keluar = True

                while Tambah == True:
                    print("=" * 54)
                    tambah_produk = input("Mau nambah? (y/t)".ljust(35) + ": ")
                    print("=" * 54)
                    if tambah_produk == "y":
                        Tambah = False
                    elif tambah_produk == "t":
                        Keluar = False
                        break
                    else:
                        print("Input yang anda masukkan tidak valid")
                        continue

                if Keluar == False:
                    membuat_invoices(nama_kasir, data_list)
                    break

            except:
                print("Harga yang anda masukkan tidak valid")
                continue

    elif pilih_opsi == "2":
        id_transaksi = input("Masukkan ID transaksi".ljust(35) + ": ")
        lokasi_file_folder = os.path.join(folder_invoices, id_transaksi+".txt")

        if os.path.isfile(lokasi_file_folder):
            with open(lokasi_file_folder, "r") as ada:
                isi = ada.read()
                print("======================= ISI FILE =====================".center(54))
                print(isi)
        else:
            print(f"File '{id_transaksi}' tidak ditemukan.")
            
    elif pilih_opsi == "3":
        print("Terimas kasih!")
        break
    else:
        print("Opsi yang anda pilih tidak valid!")