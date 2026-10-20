störst =0
minst = 1000

while True:
    tal = float(input("Skriv ett positivt tal(eller negativt tal för att avsluta)"))
    
    if tal <0:
        break
    if tal > störst:
        störst = tal
        
    if tal < minst:
        minst = tal
    
    
print("Största talet:", störst)
print("Minsta talet:", minst)