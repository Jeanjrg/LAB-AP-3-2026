level = int(input("masukkan presentase cabai: "))

if level >= 0 and level <= 10:
    print("level aman")
elif level >= 11 and level <= 40:
    print("level sedang")
elif level >= 41 and level <= 70:
    print("level pedas")
elif level > 70:
    print("level ekstrem")
else:
    print("tidak valid")

