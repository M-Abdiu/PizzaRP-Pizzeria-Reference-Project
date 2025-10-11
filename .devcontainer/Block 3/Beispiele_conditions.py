#Einlesen
number = int(input("Bitte Zahl eingeben: "))

#Option 1 Verwendung von if
if number > 0:
    pass   #wenn man nichts machen möchte


if number > 0:   # Immer ned : nicht vergessen
    print("Ist eine Positive Zahl")


if number < 0:
    print("Ist eine Negative Zahl")


if number == 0:
    print("Die Zahl ist Null")

#Option 2 Verweundung von if - else
if number > 0:
    print("Ist eine Positive Zahl")
else:                                               # ist auf der gleichen Ebene wie das erste if
    if number < 0:                                  # dieses if ist eingerückt nach dem else weil es nur entweder oder oder sein kann
            print("Ist eine Negative Zahl")
    else:
                print("Die Zahl ist Null")

#Option 3 Verwendung von if - elif - else
if number > 0:
      print("Zahl grösser als Null")
elif number < 0:                            # elif = else if beachtet alles andere als die erste Bedingung
    print("Zahl kleiner als Null")  
else:
    print("Zahl ist Null")   

#Option 4 conditional expression (man möchte einen str zurückgeben, man kann alles in eine Zeile packen))
result = "Zahl ist grösser Null" if number > 0 else "Zahl ist kleiner Null" if number < 0 else "Zahl ist Null"    #immer die Bedinung nachher
print(result)

#Option 5 conditional expression + Walrus operator → Funktioniert nur mit einem vorgehenden code, kürzeste Variante (Phytonic style)
print(result := "Zahl ist grösser Null" if number > 0 else "Zahl ist kleiner Null" if number < 0 else "Zahl ist Null")

#Option 6 match-case statement 
match(number):
    case _ if number > 0:                   # _ ist ein Platzhalter für alles sonst kann man auch eine Variable hinschreiben
        print("Zahl ist grösser Null")      # Kann man mit konkreten Werten verwenden
    case _ if number < 0:
        print("Zahl ist kleiner Null")
    case _: 
        print("Zahl ist gleich Null")


