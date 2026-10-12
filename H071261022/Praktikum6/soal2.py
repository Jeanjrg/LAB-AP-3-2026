alfabet = "abcdefghijklmnopqrstuvwxyz"

teks = input("Masukkan Teks: ")

def cek_kata(teks, kata):
    huruf_kecil = teks.lower()    
    huruf_kecil_target = kata.lower()
 
    daftar_posisi = []           
    mulai_cari = 0               
 
    while True:
        posisi_kata = huruf_kecil.find(huruf_kecil_target, mulai_cari)  
        if posisi_kata == -1:                    
            break                                
        daftar_posisi.append(posisi_kata)        
        mulai_cari = posisi_kata + 1            
    return daftar_posisi

kata = input("Masukkan kata target: ")

def cek_batas_kata(teks, posisi_kata, panjang_kata):
    if posisi_kata > 0:
        karakter_sebelum = teks[posisi_kata - 1].lower()
        if karakter_sebelum in alfabet:      
            return False

    posisi_setelah_kata = posisi_kata + panjang_kata   
    if posisi_setelah_kata < len(teks):
        karakter_sesudah = teks[posisi_setelah_kata].lower()
        if karakter_sesudah in alfabet:      
            return False
    return True                              

simbol = input("Masukkan simbol: ")

def sensor_kata(teks, kata, simbol):
    semua_posisi = cek_kata(teks, kata)   
    posisi_disensor = []                  
    hasil = ""                            
    posisi_salin = 0                      
 
    for posisi_kata in semua_posisi:
        if posisi_kata >= posisi_salin:
            hasil += teks[posisi_salin:posisi_kata] + simbol * len(kata)
            posisi_salin = posisi_kata + len(kata)
            posisi_disensor.append(posisi_kata)

    hasil = hasil + teks[posisi_salin:]   
    return (hasil, len(posisi_disensor), posisi_disensor)

 
hasil, jumlah, daftar_posisi = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", daftar_posisi)