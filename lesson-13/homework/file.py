# Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
import datetime
def age_calculator(d):
    hozir=datetime.date.today()
    tugkun=datetime.datetime.strptime(d,"%Y-%m-%d").date()
    hyil=hozir.year
    hoy=hozir.month
    hkun=hozir.day
    tyil=tugkun.year
    toy=tugkun.month
    tkun=tugkun.day
    nat_yil=hyil-tyil
    nat_oy=hoy-toy
    nat_kun=hkun-tkun
    if nat_kun<0:
        nat_oy-=1
        p_oy=(hoy-1) if hoy>1 else 12
        p_yil=hyil if hoy>1 else hoy-1
        p_oy_kun=(datetime.date(p_yil,p_oy+1,1)-datetime.date(p_yil,p_oy,1)).days
        nat_kun+=p_oy_kun
    if nat_oy<0:
        nat_yil-=1
        nat_oy+=12

    print(nat_yil,nat_oy,nat_kun)
    
d=input("Tugilgan sanangizni korsating YYYY-MM-DD formatida: ")

age_calculator(d)

# Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
