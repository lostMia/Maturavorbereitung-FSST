'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_03 (4 Punkte)
Angabe:
Schreiben Sie eine Funktion, welche den Benutzer zur Eingabe einer
positiven Kommazahl auffordert.
Übergabe-Parameter: Ein Fragestring, der dem User bei der Eingabe angezeigt wird
Return-Wert: Die korrekt eingegebene Zahl soll ans Hauptprogramm zurückgegeben werden.

Absicherung:
Die Eingabe soll gegen falsche Eingaben abgesichert sein z.B. negative Zahlen
oder Buchstaben. 
Bei falschen Eingaben soll der User erneut zur Eingabe aufgefordert werden.
Einzige Ausnahme: Wenn der User den String 'stopp' eingibt, soll die Funktion None 
ans Hauptprogramm zurückgeben.

Erstellen Sie weiters ein Commandline-Programm, welches zuerst den Namen eines Produktes erfragt.
Dann soll Mithilfe obiger Funktion der Benutzer zur Eingabe einer 
Stückanzahl des Produktes und eines Preises aller Stücke in Euro aufgefordert werden. Anschließend 
ist der Einzelpreis zu berechnen und auf 2 Kommastellen genau auszugeben.
Sollte die Funktion allerdings None zurückgeben, soll das Programm mit exit() beendet werden. 

Ausführungsbeispiel:
Please enter the name of the product: sock
Enter the number of the product: -10
This is not a valid value. Please enter a positive number.
Enter the number of the product: No
This is not a valid value. Please enter a positive number.
Enter the number of the product: 10
Enter the price of all products in Euro: 15
One sock cost 1.50 Euro.

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 4
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität des Programms (User-Eingabe, 
  Berechnung und -Ausgabe) 
1 Punkt für die korrekte Definition und Verwendung der Funktion
1 Punkte für die Fehlerbehandlung der User-Eingabe 
1 Punkt für die Abbruchoption mittels eingabe von 'end'

'''
# Lösung bitte ab hier!


def get_number(message):
  number = None

  while True:
    input_str = input(message)

    if input_str == "stop":
      return None

    try:
      number = float(input_str)

      if number < 0:
        print("This is not a valid value. Please enter a positive number.")
        continue

      break

    except:
      print("This is not a valid value. Please enter a positive number.")

  return number


name = input("Please enter the name of the product: ")
amount = get_number("Please enter the number of the product: ")

if amount == None:
  exit()

total_price = get_number("Enter the price of all products in Euro: ")

if total_price == None:
  exit()

print("One %s cost %.2f Euro"%(name, total_price / amount))
