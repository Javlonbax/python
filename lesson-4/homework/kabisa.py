yil=int(input("Yilni kiriting "))
if yil%4==0:
    if yil%100==0 and yil%400!=0:
        print(f"Siz tanlagan {yil} yil kabisa yili emas")
    else:
        print(f"Siz tanlagan {yil} yil kabisa yili hisoblanadi")
else:
    print(f"Siz tanlagan {yil} yil kabisa yili emas")
