
class Pemain:
    # Konstruktor untuk menyimpan data pemain
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    
    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    
    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    
    def tampilkan_data(self):
        print(f"{self.nama:<15} {self.id_pemain:<10} {self.role:<12} "
              f"{self.hitung_skor_akhir():<12.2f} {self.status_performa()}")



daftar_pemain = []

print("===SISTEM PENILAIAN PERFORMA PEMAIN===")


jumlah = int(input("Masukkan jumlah pemain: "))

# Perulangan untuk memasukkan data pemain
for i in range(jumlah):
    print(f"\nData Pemain ke-{i+1}")

    nama = input("Nama pemain: ")
    id_pemain = input("ID pemain: ")
    role = input("Role pemain: ")
    nilai_kill = float(input("Nilai Kill: "))
    nilai_assist = float(input("Nilai Assist: "))
    nilai_objective = float(input("Nilai Objective: "))

    
    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)

    
    daftar_pemain.append(pemain)


# Menampilkan seluruh data pemain
print("\n========== REKAPITULASI PERFORMA PEMAIN ==========")
print(f"{'Nama':<15} {'ID':<10} {'Role':<12} {'Skor Akhir':<12} {'Status'}")
print("-" * 70)

for pemain in daftar_pemain:
    pemain.tampilkan_data()
