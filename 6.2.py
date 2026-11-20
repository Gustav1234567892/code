s = input ("Skriv ett godtyckligt antal heltal")
lista = s.split()
s = [float(t) for t in lista]
for i in range (len(s)):
    if s[i-1]<0:
        print (s[i-1])
