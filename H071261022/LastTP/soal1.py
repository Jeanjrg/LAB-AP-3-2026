class Pemain:
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

    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {no:<2} | {self.nama:<10} | {self.id_pemain:<10} | {self.role:<9} | {skor:<10.2f} | {status:<14} |")

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
print()

daftar_pemain = []
while True:
    try:
        jumlah = int(input("\nMasukkan jumlah pemain: "))
        if jumlah <= 0:
            print("Jumlah pemain harus lebih dari 0!")
            continue
        else:
            break
    except:
        print("Input yang anda masukkan tidak valid!")
        continue

i = 1
while i <= jumlah:
    try:
        print()
        print(f"-- Data Pemain ke-{i} --")
        nama = input("Nama: ")
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")
        nilai_kill = float(input("Nilai Kill: "))
        nilai_assist = float(input("Nilai Assist: "))
        nilai_objective = float(input("Nilai Objective: "))
    except ValueError:
        print("Input yang anda masukkan tidak valid!")
        continue

    p = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(p)
    i += 1

print()
print("=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 74)
print(f"| {'No':<2} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<9} | {'Skor Akhir':<10} | {'Status':<14} |")
print("=" * 74)

for nomor, p in enumerate(daftar_pemain, start=1):
    p.tampilkan_data(nomor)

print("=" * 74)