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
import datetime
def age_calculator(d):
    hozir=datetime.date.today()
    tugkun=datetime.datetime.strptime(d,"%Y-%m-%d").date()

    hkun=hozir.year*365+hozir.month*30+hozir.day

    tkun=tugkun.year*365+tugkun.month*30+tugkun.day

    natija=hkun-tkun
    print(natija)
    
d=input("Tugilgan sanangizni korsating YYYY-MM-DD formatida: ")

age_calculator(d)

№ Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
from datetime import datetime, timedelta

def calculate_meeting_end(start_str, duration_hours, duration_minutes):
    start_time = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
    duration = timedelta(hours=duration_hours, minutes=duration_minutes)
    end_time = start_time + duration
    return end_time

start_input = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
hours = int(input("Uchrashuv davomiyligini soatda kiriting: "))
minutes = int(input("Uchrashuv davomiyligini daqiqada kiriting: "))

try:
    end = calculate_meeting_end(start_input, hours, minutes)
    print("Uchrashuv tugaydigan sana va vaqt:", end.strftime("%Y-%m-%d %H:%M"))
except ValueError:
    print("Kiritilgan format noto‘g‘ri. Iltimos, 'YYYY-MM-DD HH:MM' formatidan foydalaning.")
# Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

# Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

#Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

#Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

#Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

#Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

#Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
