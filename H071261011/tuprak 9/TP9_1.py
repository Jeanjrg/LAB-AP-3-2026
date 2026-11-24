class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id = id_pemain
        self.role = role
        self.kill = nilai_kill
        self.assist = nilai_assist
        self.objective = nilai_objective
        self.status = None
        self.skor_akhir = 0

    def hitung_skor_akhir(self):
        skor_akhir = (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)
        self.skor_akhir = skor_akhir
        return self.skor_akhir

    def status_performa(self):
        status = "Unggul" if self.skor_akhir >= 60 else "Perlu Evaluasi"
        self.status = status
        return self.status

    def tampilkan_data(self, no):
        skor_akhir = self.hitung_skor_akhir()
        status = self.status_performa()


        return (
            f"| {no:<3} | {self.nama:<12} | {self.id:^11} | "
            f"{self.role:<11} | {skor_akhir:<11.2f} | {status:<16} |"
        )

list_pemain = []

try:
    jumlah = int(input("Masukkan Jumlah: "))
except ValueError:
    print("Harus Angka Bang")

for i in range(jumlah):
    nama = input("Masukkan Nama: ").capitalize()
    id = input("Masukkan ID: ")
    role = input("Masukkan Role: ").capitalize()

    try:
        kill = int(input("Nilai Kill: "))
        assist = int(input("Nilai Assist: "))
        objective = int(input("Nilai Objective: "))
    except ValueError:
        print("Harus Angka Bang")

    pemain_baru = Pemain(nama, id, role, kill, assist, objective)

    list_pemain.append(pemain_baru)

print("=== REKAPITULASI PERFORMA PEMAIN ===")
garis_pembatas = "=" * 82

print(garis_pembatas)
print(
    f"| {'No':<3} | {'Nama':<12} | {'ID Pemain':<11} | {'Role':<11} |"
    f" {'Skor Akhir':<11} | {'Status':<16} |"
)
print(garis_pembatas)

for idx, p in enumerate(list_pemain, 1):
    print(p.tampilkan_data(idx))
print(garis_pembatas)      



               




               