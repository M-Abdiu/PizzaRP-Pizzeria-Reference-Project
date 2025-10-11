#While Schleife
i = 0           #wird häufig verwendet wenn der Benutzer etwas eingeben soll
                #Man kennt die Anzahl der Durchläufe nicht
while i <= 10:   #Alles was eingerückt ist wird ausgeführt solange die Bedingung wahr ist
    if i % 2 == 0:  #Wenn i durch 2 teilbar ist (gerade Zahl). Gibt keinen Rest wenn man i durch 2 teilt, sondern der Rest ist 0
        print(i)    #Man springt immer nach ausführung wieder zur Schleifenbedingung zurück und führt neu aus. 
    i = i + 1   #i wird um 1 erhöht / Abbruchbedingung

#For Schleife            #Wenn man die Anzahl der Durchläufe kennt
for i in range(1, 11, 1):   #zeigt in der Klammer an von wo bis wo gezählt wird (inklusive, exklusive) / der letzte Parameter ist die Inkrementierung also hier 1. Bei z.B: 2 wird immer um 2 erhöht
    if i % 2 == 0:        #Wenn i durch 2 teilbar ist (gerade Zahl). Gibt keinen Rest
        print(i)             #Alles was eingerückt ist wird für jeden Wert von i ausgeführt


