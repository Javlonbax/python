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
from datetime import datetime
import pytz
def timezone_converter(date_str, from_tz_str, to_tz_str):
    from_timezone = pytz.timezone(from_tz_str)
    to_timezone = pytz.timezone(to_tz_str)
    naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    local_datetime = from_timezone.localize(naive_datetime)
    converted_datetime = local_datetime.astimezone(to_timezone)
    return converted_datetime
date_input = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_timezone_input = input("Hozirgi vaqt zonangizni kiriting (masalan, Asia/Tashkent): ")
to_timezone_input = input("O‘girmoqchi bo‘lgan vaqt zonangizni kiriting (masalan, US/Eastern): ")
try:
    result = timezone_converter(date_input, from_timezone_input, to_timezone_input)
    print("O‘girilgan sana va vaqt:", result.strftime("%Y-%m-%d %H:%M (%Z%z)"))
except Exception as e:
    print("Xatolik yuz berdi:", str(e))
    print("Iltimos, vaqt zonalarini to‘g‘ri formatda kiriting (masalan, Europe/London, Asia/Tashkent, US/Eastern).")
# Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
import time
from datetime import datetime
def countdown_timer(target_time_str):
    target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")
    while True:
        now = datetime.now()
        remaining = target_time - now
        if remaining.total_seconds() <= 0:
            print(" Vaqt tugadi!")
            break
        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"\rQolgan vaqt: {days} kun, {hours:02} soat, {minutes:02} daqiqa, {seconds:02} soniya", end="")
        time.sleep(1)
user_input = input("Kelajakdagi sanani kiriting (YYYY-MM-DD HH:MM:SS): ")
try:
    countdown_timer(user_input)
except ValueError:
    print(" Sana va vaqt noto‘g‘ri formatda. Iltimos, YYYY-MM-DD HH:MM:SS formatidan foydalaning.")
#Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None
email_input = input("Email manzilingizni kiriting: ")
if is_valid_email(email_input):
    print(" Email manzili to‘g‘ri!")
else:
    print(" Noto‘g‘ri email manzili. Iltimos, qayta tekshirib kiriting.")
#Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
def format_phone_number(phone):
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) != 10:
        return " Noto'g'ri raqam: 10 ta raqam kiritilishi kerak."
    area_code = digits[:3]
    central_office = digits[3:6]
    line_number = digits[6:]
    return f" Formatlangan raqam: ({area_code}) {central_office}-{line_number}"
user_input = input("Telefon raqamingizni kiriting (faqat raqamlar): ")
formatted = format_phone_number(user_input)
print(formatted)
#Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
def is_strong_password(password):
    if len(password) < 8:
        return False, "Parol kamida 8 ta belgidan iborat bo'lishi kerak."
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    if not has_upper:
        return False, "Parolda kamida 1 ta KATTA harf bo'lishi kerak."
    if not has_lower:
        return False, "Parolda kamida 1 ta kichik harf bo'lishi kerak."
    if not has_digit:
        return False, "Parolda kamida 1 ta raqam bo'lishi kerak."
    return True, " Parol kuchli!"
password = input("Parol kiriting: ")
is_strong, message = is_strong_password(password)
print(message)

#Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
def find_word_occurrences(text, word):
    word = word.lower()
    text_lower = text.lower()
    start = 0
    occurrences = []
    while True:
        pos = text_lower.find(word, start)
        if pos == -1:
            break
        occurrences.append(pos)
        start = pos + 1  # keyingi qidiruv uchun pozitsiyani siljitish
    return occurrences
sample_text = """Python — bu yuqori darajadagi, interpretatsiya qilinadigan dasturlash tili. Python dasturlash tili juda mashhur va o‘rganish uchun qulay."""
search_word = input("Qidiriladigan so'zni kiriting: ")
positions = find_word_occurrences(sample_text, search_word)
if positions:
    print(f"'{search_word}' so'zi matnda {len(positions)} marta uchradi. Pozitsiyalari:")
    for pos in positions:
        print(f"- Indeks: {pos}")
else:
    print(f"'{search_word}' so'zi matnda topilmadi.")
#Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
import re
def extract_dates(text):
    date_patterns = [
        r'\b\d{4}-\d{2}-\d{2}\b',               # YYYY-MM-DD
        r'\b\d{2}/\d{2}/\d{4}\b',               # DD/MM/YYYY
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}\b',  # Month DD, YYYY
    ]
    found_dates = []
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        found_dates.extend(matches)
    return found_dates
user_input = input("Matn kiriting (sanalari bo'lishi mumkin): ")
dates = extract_dates(user_input)
if dates:
    print(f"Topilgan sanalar ({len(dates)} ta):")
    for d in dates:
        print("-", d)
else:
    print(" Hech qanday sana topilmadi.")
