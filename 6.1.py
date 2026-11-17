n = int(input("Hur många tal önskas?"))
f = [2]
k=3
for i in range (1, n+1):
    f += [f[i-1] *k]
print(f)