kepedasan=int(input("masukkan presentase cabai:"))

if kepedasan >=0 and kepedasan <=10:
    print("level aman")
elif kepedasan >=11 and kepedasan <=40:
    print("level sedang")
elif kepedasan >=41 and kepedasan <=70:
    print("level pedas")
elif kepedasan >=71 and kepedasan <=100:
    print("level ekstrem")
else: print ("input tidak valid")