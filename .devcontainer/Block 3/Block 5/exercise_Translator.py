from deep_translator import GoogleTranslator    # nach der installation von pypi trotzdem noch importieren 

#Aufruf (Stop wort ist: "stop")
text = str(input("Bitte Text eingeben:"))

#Aufruf deep_translator (von Google Translate)
def translation(text)->str:             #->str dient nur um zu wissen was wiedergegeben wird.
    translated = GoogleTranslator(source='auto', target='en').translate(text=text)
    return translated

while text.strip().lower() != "stop":              #.strip() = blanks löschen .lower() = alles in Kleinbuchstaben machen
    print(translation(text))
    text = str(input("Bitte Text eingeben:"))     # bis der User stop eingibt, ist die Schleife "Endlos" drum nochmal eibgabe
print("Programmende...Bye")                        # geht nich zu diesem print ohne das die schleife beendet ist. 