bliste = []
aliste = []
liste = []

for i in range(100,1000):
    for j in range(100,1000):
        listetall1 = []
        listetall2 = []
        for k in range (3):
            x = str(i)
            y = str(j)
            listetall1.append((x[k]))
            listetall2.append((y[k]))
        if sorted(listetall1) == sorted(listetall2):
            listetall3 = []
            svar = i - j
            if(len(str(svar))) == 3:
                for l in range(3):
                    strsvar = str(svar)
                    listetall3.append((strsvar[l]))
                    if sorted(listetall3) == sorted(listetall1):
                        aliste.append(i)
                        bliste.append(j)
                        liste.append(svar)

print(aliste)
print(bliste)
print(liste)