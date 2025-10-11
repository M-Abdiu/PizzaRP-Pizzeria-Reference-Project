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


# break und continue        # Man möchte die Schleife beenden 
num = 0

while num < 10:
    num += 1
    
    if num == 5:
        print("Skip!")
        continue                       #weiter mit dem nächsten inkrement. Heisst 5 wird hier übersprungen und es geht mit 6 weiter
    if num == 8:
        print("Breaking at 8!")
        break                           #Wenn ich bei 8 bin, möchte ich raus aus der Schleife. man geht zur nächsten Zeile ausserhalb des Kasten

    print("Derzeitige Zahl: ", num)

print("Schleife beendet...")

#mit else
else:
    print("Nummer nicht gefunden")  # Wenn die break funktion nicht durchgeführt wird. ist auf der Höhe des while loops
