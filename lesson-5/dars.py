countr=['az6s','uzsssss','rus']
sorted(countr,key=len)                  ##### so`zzi uzunligiga qarab sortirovka qiladi

### -  ()
#1 - oddiy qavslar tuple da ishlatiladi
#2 - funksiyalar bilan print(), id(), print
#3 - metodlaar bilan ishlatiladi upper(), append(), split()

#  - []
#1 - list da ishlatiladi
#2 - indexing da a[1],
#3 - slicingsa ls[1:2:3]
#4 - list comprehention, yani listni ichida for loop ishlatganda

# - {}
#1 - dictionary va set da ishlatamiz
#2 - str formatda f"str{v} gdfh"

ls=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in ls:
    if i%2==0:
        print(i,end=' ')

num=int(input('raqam kirit'))
for i in range(2,num):
    if num%i==0:
        print('tubsonmas')
        break
else:                           ### bu for loop ni else, agar for loop muammosiz ohirgacha ishlap tugasa, keyin else ishliydi
    print('tubson')
