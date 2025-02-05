'''
Matura Übungsaufgabe_003 (2 Punkte)
================
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe von zwei Gleitkommazahlen bittet.

Die zwei eingegeben Zahlen sollen dann von einander subtrahiert werden.
Geben Sie das Ergebnis in der Form "zahl1 - zahl2 = result" aus, wobei
das Ergebnis mit 4 Nachkommastellen angezeigt werden soll.

Achtung! Es soll nicht auf 4 Nachkommastellen gerundet werden,
nur im print-command so angezeigt werden! 
Tipp: f-Strings und Formatanweisungen im f-String
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Für Hilfe zur Formatierung siehe "Format Specification Mini-Language" im
"string" (nicht "str"!) Kapitel der Python Doc.

Ausführungsbeispiel:

Please enter the first floating point number ->2.345
Please enter the second floating point number ->5.055
2.345-5.055=-2.7100

Erreichbare Punkte: 2
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität 
1 Punkt für die korrekte Formatierung der Ausgabe.
'''

num1, num2 = None, None

num1 = float(input("Please enter the first floating point number ->"))
num2 = float(input("Please enter the second floating point number ->"))

subtraction = num1 - num2

print("%.4f-%.4f=%.4f"%(num1, num2, subtraction))
