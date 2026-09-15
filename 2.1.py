mätarställning_idag = float(input("Mätarställning idag?"))
mätarställning_för_ett_år_sedan = float(input("Mätarställning för ett år sedan?"))
Antal_liter_bensin = float(input("Hur många liter bensin har du förbrukat under året?"))
antal_mil = mätarställning_idag - mätarställning_för_ett_år_sedan
förbrukning_per_mil = Antal_liter_bensin / antal_mil
print ("Förbrukning per mil", förbrukning_per_mil)
print("Antal mil", antal_mil)