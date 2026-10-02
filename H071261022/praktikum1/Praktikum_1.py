menu = ["kopi susu", "matcha latte", "americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopiSusu = jumlah[0] * harga[0]
sub_matchaLatte = jumlah[1] * harga[1]
sub_americano = jumlah[2] * harga[2]

subtotal_pendapatan = [sub_kopiSusu, sub_matchaLatte, sub_americano]
total_seluruh = sum(subtotal_pendapatan)  

BIAYA_OPRASIONAL = 15000

pendapatan_bersih = total_seluruh - BIAYA_OPRASIONAL

jumlah_barangTerjual = sum(jumlah)

target_tercapai = (total_seluruh > 200000) and (jumlah_barangTerjual > 10)
 
print(f"Total Pendapatan = {total_seluruh}")
print(f"Pendapatan Bersih = {pendapatan_bersih}")
print(f"Target Tercapai = {target_tercapai}")