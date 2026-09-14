menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopisusu = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

totalcupterjual = sum(jumlah)

subtotalpendapatan =[sub_kopisusu, sub_matcha, sub_americano]
pendapatankotor = sum(subtotalpendapatan)

BIAYA_OPRASIONAL = 15000
pendapatanbersih = pendapatankotor - BIAYA_OPRASIONAL

targettercapai = pendapatankotor > 200000 and totalcupterjual > 10

print("pendapatan bersih:", pendapatanbersih)
print("target tercapai:", targettercapai)
print("pendapatan kotor:", pendapatankotor)