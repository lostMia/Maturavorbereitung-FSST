'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_04 (3 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches Zahlen (Gleitkomma- sowie Ganzzahlen)
aus der Datei 024_practice.txt liest. Es können beliebig viele Zahlen pro Zeile 
im File sein. Die erste Zahl ist durch einen Hashtag (#) von den anderen Zahlen getrennt.
Alle weiteren Zahlen innerhalb einer Zeile sind durch eine Welle (~) 
voneinander getrennt. Im File können beliebig viele Zeilen sein.
Pro Zeile ist die Differenz aus der ersten Zahl (getrennt durch #) und der Summe der 
weiteren Zahlen zu berechnen. Das Ergebnis der Summe ist 
pro Zeile auszugeben. Weiters soll die Gesamtsumme aller Ergebnisse berechnet
und am Ende ausgegeben werden. Die Zahlen sollen alle rechtsbündig und auf zwei Kommastelle gerundet
ausgegeben werden, damit das Komma bei allen Zahlen genau untereinander ist.

Ausführungsbeispiel:

File content:
123#4.5~5
15.4#7.1~3
9#10~11~12~13
32#14~15.3~0.23~1.12 

Ausgabe:
Difference line 1:   113.50
Difference line 2:     5.30
Difference line 3:   -37.00
Difference line 4:     1.35
Overall difference:   83.15


Achten Sie auf sauberes Schliessen des file-streams!

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 3
Aufteilung der Punkte:  
1 Punkt für das korrekte Arbeiten mit dem File (Öffnen, Schließen) 
1 Punkt für die richtige Berechnung der Summen
1 Punkt für die korrekte Formatierung bei der Ausgabe.
'''
# Lösung bitte ab hier!


file = open("124_practice.txt", "r")

contents = file.read().split("\n")

file.close()

contents = contents[:-1]

numbers_total = []
for line in contents:
    number_str = ""
    number_line = []

    for character in line:
        if character == "#" or character == "~":
            number = float(number_str)
            number_str = ""
            number_line.append(number)
            continue

        number_str += character

    number = float(number_str)
    number_line.append(number)

    numbers_total.append(number_line)

diffs = []
for i, number_line in enumerate(numbers_total):
    diff = number_line[0]

    for y in range(1, len(number_line)):
        diff -= number_line[y]

    diffs.append(diff)

    print("Difference line %i: %10.2f"%(i, diff))

print("Overall difference: %9.2f"%(sum(diffs)))
