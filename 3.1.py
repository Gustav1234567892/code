minut_per_månad = float(input("Hur många minuter ringer du per månad?"))
pris_per_minut = float(input("Vad kostar det att ringa per minut?"))
pris_per_månad = minut_per_månad * pris_per_minut
if pris_per_månad >= 300:
   print("Du betalar",pris_per_månad * 0.9, "kr per månad för ditt telefonabonnemang")
else:
   print("Du betalar", pris_per_månad, "kr per månad för ditt telefonabonnemang")