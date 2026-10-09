level = int(input("masukan persentase cabai :"))

if level >= 0 and level <= 10:
    print("level Aman")
elif level >= 11 and level <= 40:
    print("level sedang")
elif level >= 41 and level <= 70:
    print("level Pedas")
elif level >= 71 and level <= 100:
    print("level ekstrem")
else:
    print("level tidak valid")