def bersihkan_teks(teks): 
    huruf = "abcdefghijklmnopqrstuvwxyz" 
    hasil = "" 
    for char in teks.lower(): 
        if char in huruf: 
            hasil += char 
    return hasil 

def cek_palindrome(teks): 
    dibalik = "".join(reversed(teks)) 
    if teks == dibalik: 
        return (True, -1) 
    else: 
        return (False, 0)

def inti_palindrome(teks): 
    teks_bersih = bersihkan_teks(teks)
    panjang_maks = 0 
    indeks_awal = 0 
    substring_maks = ""

    n = len(teks_bersih)
    for i in range(n): 
        for j in range(i + 1, n + 1):
            sub = teks_bersih[i:j]
            if sub == "".join(reversed(sub)):
                panjang = len(sub)
                
                if panjang > panjang_maks:
                    panjang_maks = panjang
                    indeks_awal = i
                    substring_maks = sub

    return {"teks": substring_maks, "panjang": panjang_maks, "indeks_awal": indeks_awal}    

if __name__ == "__main__": 
    while True:
        teks_1 = input("Masukkan teks prasasti: ")
        print(f"Teks Bersih: {bersihkan_teks(teks_1)}")
        print(f"Output Terharap: {inti_palindrome(teks_1)}")