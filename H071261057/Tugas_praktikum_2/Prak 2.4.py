tujuan = input("masukkan tujuan (pantai/pegunungan/kota):") 
waktu = input("masukkan waktu (pagi/malam):") 
pengunjung = input("masukkan tipe pengunjung (anak/dewasa):") 
 
match tujuan: 
    case "pantai": 
         
        if waktu == "pagi": 
            print("Paket Rekomendasi: Paket A") 
 
        
        elif waktu == "malam": 
            if pengunjung == "dewasa": 
                print("Paket Rekomendasi: Paket C") 
            else: 
                print("Paket Rekomendasi: Tidak ada paket yang cocok") 
 
        else: 
            print("Paket Rekomendasi: Tidak ada paket yang cocok") 
 
    case "pegunungan": 
         
        if waktu == "pagi": 
            if pengunjung == "dewasa": 
                print("Paket Rekomendasi: Paket B") 
            else: 
                print("Paket Rekomendasi: Tidak ada paket yang cocok") 
 
         
        elif waktu == "malam": 
            if pengunjung == "dewasa": 
                print("Paket Rekomendasi: Paket C") 
            else: 
                print("Paket Rekomendasi: Tidak ada paket yang cocok") 
 
        else: 
            print("Paket Rekomendasi: Tidak ada paket yang cocok") 
 
    case "kota": 
         
        if waktu == "malam": 
            print("Paket Rekomendasi: Paket C") 
 
         
        else: 
            print("Paket Rekomendasi: Tidak ada paket yang cocok") 
 
    case _: 
         
        print("Paket Rekomendasi: Tidak ada paket yang cocok") 
