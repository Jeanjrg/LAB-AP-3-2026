
def ke_angka(teks):
    try:
        return int(teks) #return mengembalikan nilai ke fungsi yang di panggil
    except:
        return float(teks)

daftar_nilai = [] #list kososng
while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if masukan == "":
        break
    try:
        nilai = ke_angka(masukan)
    except:
        print("Input tidak valid, nilai harus berupa angka.")
        continue
    daftar_nilai.append(nilai) #append menambahkan nilai di belakang list

def rekap_nilai(*nilai): 
    rata = sum(nilai) / len(nilai) #jumlah bagi rata"
    return (rata, max(nilai), min(nilai)) #mencari nilai tertinggi dan terendah

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = rekap_nilai(*daftar_nilai) #mengirim nilai ke fungsi
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")