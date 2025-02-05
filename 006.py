'''
Matura Übungsaufgabe_006 (2 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
dem User hilft die Gaußsche Summenformel zu illustrieren.

Der User soll die Anzahl der Wiederholungen als Integer eingeben.
Die Formatierung der Ausgabe im Ausführungsbeispiel ist optional, aber
einen der möglichen Punkte wert!

Ausführungsbeispiel:
Please enter number of iterations -> 5
    1 + 2 =  3
    3 + 3 =  6
    6 + 4 = 10
    10 + 5 = 15
    15 + 6 = 21
	


Für Hilfe zur Formatierung siehe "Format Specification Mini-Language" im
"string" (nicht "str"!) Kapitel der Python Doc.

Erreichbare Punkte: 2
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität 
1 Punkt für die korrekte Formatierung der Ausgabe.
'''


rep = int(input("Please enter number of iterations -> "))
sum = 1

for i in range(2, rep + 2):
    print(f"{sum} + {i} = {sum + i}")
    sum += i

