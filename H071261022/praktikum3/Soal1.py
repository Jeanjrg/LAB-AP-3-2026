
print("Selamat datang di Kasir Minimarket!")

def hitung_subtotal(harga, jumlah, adalah_member=False): 
    subtotal = harga * jumlah
    if adalah_member: #true
        subtotal = subtotal * 0.9  #pelanggan hanya perlu membayar 90%
    return int(subtotal) #return mengembalikan nilai ke fungsi yang di panggil

while True:
    status_member = input("Apakah Anda member? (ya/no): ").strip().lower()
    if status_member == "ya" or status_member == "no":
        break
    print("Input tidak valid, masukkan ya atau no.")
member = status_member == "ya" 

total = 0
while True:
    nama = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama == "":
        break
    while True:
        try:
            harga = int(input("Harga barang: "))
            break
        except:
            print("Input tidak valid, harga harus berupa angka.")
    while True:
        try:
            jumlah = int(input("Jumlah barang: "))
            break
        except:
            print("Input tidak valid, jumlah harus berupa angka.")
    subtotal = hitung_subtotal(harga, jumlah, member)
    print(f"Subtotal {nama}: Rp{subtotal}")
    total = total + subtotal

print(f"Total belanja: Rp{total}")