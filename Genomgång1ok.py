ålder = int(input("Hur gammal är du?"))

if ålder == 17:
    print("Du är lika gammal som de flesta i EE25")
    
if ålder != 43:
    print("Du är inte lika gammal som Per")
else:
    print("Du är lika gammal som Per")
    
if ålder <= 13:
    print("Du är väldigt ung")
elif ålder <18:
    print ("Du bist gut genug")
elif ålder < 20:
    print("Du får ta körkort")
else:
    print("Du får handla på systembolaget")
    
namn = input("Vad är ditt namn?")

if namn == "Gustav":
    print("Du bist gut genug!")
elif namn == "Gustav":
    print("Så stavar man inte!")

if ålder == 43 and namn == "Per":
    print("Du är 43 år gammal och heter Per")