print("---Rekapitulasi Transaksi Dins Store---")
print("kerik '0' untuk menutup tokoh dan mengakhiri sesi.")
print()
while True:
    input_jumlah = input("masukkan jumlah item: ")
    try:
        jumlah = int(input_jumlah)
    except:
        print("input harus berupa angka!")
        print()
        continue
    if jumlah == 0:
        print("toko ditutup. sesi rekap selesai.")
        print()
        break
    elif jumlah < 0:
        print("jumlah tidak boleh negatif")
        print()
        continue
    elif jumlah > 100:
        print("jumlah tidak boleh negatif")
        print()
        continue
    else:
        print(f"transaksi {jumlah} item berhsil!")
        print()