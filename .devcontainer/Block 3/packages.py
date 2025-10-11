# Primzahlen mit sympy
import sympy

number = int(input("Gib deine Zahl ein: "))

if sympy.isprime(number):               #spezifischer code die die library verwendet
    print(number, "ist Primzahl")
else:
    print(number, "ist keine Primzahl")


# import
import math         # diese muss man nicht von pypi.org runterladen sondern einfach "import" 

print(math.pi)


# from bei qualifizierten libraries
from math import pi
print(pi)                   #direkt aus der library verwenden ohne die ganze zu drucken
