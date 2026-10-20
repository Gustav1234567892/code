#Beräkning av summan 1 + 2 + 3 + ..+n
import time
import math
while True:
    n =int(input("n?, skriv ett tal mindre än eller lika med 0 för att avsluta"))
    start = time.time()
    if n <= 0:
        break
    summa = 0
    k = 1
    while k<=n:
        summa = summa + k
        k = k + 1
    slut = time.time()
    print("Summar blir", summa, "Det tog", round(slut - start), "sekunder att räkna ut.")