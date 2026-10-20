längd = float(input("Hur långt är ditt brev i milimeter?"))
tjocklek = float(input("Hur tjockt är ditt brev i milimeter?"))
bredd = float(input("Hur brett är ditt brev i milimeter?"))

if bredd + längd + tjocklek > 900:
    print("Ditt brev är för stort")
elif längd > 600 or tjocklek > 100:
    print("Ditt brev är för stort")
elif längd < 140 or bredd < 90:
    print("Ditt brev är för litet")
else:
    print("Ditt brev är godkänt")