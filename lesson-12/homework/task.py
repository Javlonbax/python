#Exercise 1: Threaded Prime Number Checker

import threading

def prime(n):

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n//2)+1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(boshi, oxiri, natija, lock):
    local_primes = []
    for num in range(boshi, oxiri):
        if prime(num):
            local_primes.append(num)
    with lock:
        natija.extend(local_primes)

def main(bosh,oxir,soni):

    total_numbers = oxir - bosh
    step = total_numbers // soni

    primes = []
    lock = threading.Lock()

    threads = []

    for i in range(soni):
        start = bosh + i * step
        end = bosh + (i + 1) * step if i != soni - 1 else oxir
        t = threading.Thread(target=check_primes, args=(start, end, primes, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    primes.sort()

    print("Toq sonlar({0}, {1}) ichida:".format(bosh, oxir))
    print(primes)

bosh=int(input("Qaysi sondan boshlash: "))
oxir=int(input("Qaysi songacha: "))
soni=int(input("Nechchiga bo`lib hisoblansin: "))
main(bosh,oxir,soni)

##Exercise 2: Threaded File Processing

import threading
from collections import Counter
import re

def soz_sanoq(qatorlar, umumiy_sanoq, qulflash):
    local_sanoq = Counter()
    for qator in qatorlar:
        sozlar = re.findall(r'\b\w+\b', qator.lower())
        local_sanoq.update(sozlar)
    with qulflash:
        umumiy_sanoq.update(local_sanoq)

def bolish(lst, n):

    uzunlik = len(lst)
    qadam = uzunlik / float(n)
    qismlar = []
    boshlanish = 0.0
    while boshlanish < uzunlik:
        qismlar.append(lst[int(boshlanish):int(boshlanish + qadam)])
        boshlanish += qadam
    return qismlar

if __name__ == "__main__":
    fayl_nomi = 'katta_matn_fayli.txt'  
    ip_soni = 4 

    with open(fayl_nomi, 'r', encoding='utf-8') as f:
        qatorlar = f.readlines()

    qismlar = bolish(qatorlar, ip_soni)

    umumiy_sanoq = Counter()
    qulflash = threading.Lock()
    iplar = []

    for qism in qismlar:
        t = threading.Thread(target=soz_sanoq, args=(qism, umumiy_sanoq, qulflash))
        t.start()
        iplar.append(t)

    for t in iplar:
        t.join()

    for soz, soni in umumiy_sanoq.most_common(50):
        print(f"{soz}: {soni}")

