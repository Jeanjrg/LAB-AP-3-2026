# menu untuk data penjualan
menu = ["kopi susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

#sub total masing-masing
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1] 
sub_americano = harga[2] * jumlah[2]

#sub total keseluruhan
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano] 

#total pendapatan
total_pendapatan = sum(subtotal_pendapatan)

BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_pendapatan - BIAYA_OPERASIONAL

# Jumlah semua barang yang terjual
total_barang = sum(jumlah)

#menentukan apakah target tercapai
target_tercapai = total_pendapatan > 200000 and total_barang > 10

#hasil
print("Subtotal Kopi Susu   : ", sub_kopi)
print("Subtotal Matcha Latte: ", sub_matcha)
print("Subtotal Americano   : ", sub_americano)
print("Subtotal pendapatan  : ", total_pendapatan)
print("Pendapatan Bersih    : ", pendapatan_bersih)
print("Target Tercapai      : ", target_tercapai)




