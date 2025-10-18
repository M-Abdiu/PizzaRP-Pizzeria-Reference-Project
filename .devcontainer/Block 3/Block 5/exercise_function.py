
def find_max(val1, val2, val3):   # Funktion: maximum von 3 ints
    largest = val1                 # man setzt val1 mal als erstes
    if val2 > largest:
        largest = val2
    if val3 > largest:
        largest = val3
    return largest              #was soll die funkton zurückgeben


print("Maximum", find_max(3, 5, 2))                 #Aufruf
