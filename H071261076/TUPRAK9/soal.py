#program penilaian performa pemain game

class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul" 
        return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        print(f"| {no:<3} | {self.nama:<10} | {self.id_pemain:<10} | {self.role:<9} | {skor:<10.2f} | {self.status_performa():<14} |")


daftar_pemain = [] 

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
print()
jumlah = int(input("Masukkan jumlah pemain: "))

for i in range(1, jumlah + 1): 
    print()
    print(f"-- Data Pemain ke-{i} --")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    nilai_kill = float(input("Nilai Kill: "))
    nilai_assist = float(input("Nilai Assist: "))
    nilai_objective = float(input("Nilai Objective: "))

    daftar_pemain.append(Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective))

garis = "=" * 76
print()
print("=== REKAPITULASI PERFORMA PEMAIN ===")
print(garis)
print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<9} | {'Skor Akhir':<10} | {'Status':<14} |")
print(garis)

for nomor, pemain in enumerate(daftar_pemain, start=1): 
    pemain.tampilkan_data(nomor)

print(garis)