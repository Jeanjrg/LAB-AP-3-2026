#data awal
menu = ["Kopi Susu", "Matcha Latte","Americano" ]
harga = [18000, 22000, 15000]
jumlah = [4.5, 3, 5]
#subtotal 
sub_kopi = harga[0]*jumlah[0]
sub_matcha = harga [1]*jumlah[1]
sub_americano = harga [2]*jumlah[2]
#subtotal pendapatan
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]
#hitung sub total 
BIAYA_OPRASIONAL = 15000
total_seluruh = sum(subtotal_pendapatan)
pendapatan_bersih = total_seluruh - BIAYA_OPRASIONAL
total_barang_terjual = sum(jumlah) 
#target tercapai
target_tercapai = (total_seluruh > 200000) and (total_barang_terjual > 10)

#print
print("Sub Total Pendapatan per Minuman:")
print("-kopi susu    : Rp", subtotal_pendapatan[0])
print("-Matcha Latte : Rp", subtotal_pendapatan[1])
print("-Americano    : Rp", subtotal_pendapatan[2])

print("\n--- Ringkasan Laporan---")
print("Total Seluruh Pendapatan : Rp", total_seluruh)
print("Pendapatan Bersih        : Rp", pendapatan_bersih)
print("Target Tercapai          :", target_tercapai)