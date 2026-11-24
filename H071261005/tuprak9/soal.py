class Pemain:
    def __init__(self, nama, id_pemain, role, kill, assist, objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.kill = float(kill)
        self.assist = float(assist)
        self.objective = float(objective)

    def hitung_skor_akhir(self):
        return (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, nomor):
        skor_akhir = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"{nomor:<4} | {self.nama:<10} | {self.id_pemain:<12} | {self.role:<10} | {skor_akhir:<10.2f} | {status}")

print("=" * 35)
print(" SISTEM PENILAIAN PERFORMA PEMAIN ")
print("=" * 35)

daftar_pemain = []
try:
    jumlah_pemain = int(input("Masukkan jumlah pemain: "))
except ValueError:
    print("Input jumlah pemain harus berupa angka.")
    exit()

for i in range(jumlah_pemain):
    print(f"\nData Pemain ke-{i+1}")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    kill = float(input("Nilai Kill: "))
    assist = float(input("Nilai Assist: "))
    objective = float(input("Nilai Objective: "))
    pemain = Pemain(nama, id_pemain, role, kill, assist, objective)
    daftar_pemain.append(pemain)

print("\n" + "=" * 65)
print("REKAPITULASI PERFORMA PEMAIN")
print("=" * 65)
print(f"{'No':<4} | {'Nama':<10} | {'ID Pemain':<12} | {'Role':<10} | {'Skor Akhir':<10} | Status")
print("-" * 65)

for idx, pemain in enumerate(daftar_pemain, 1):
    pemain.tampilkan_data(idx)
print("-" * 65)