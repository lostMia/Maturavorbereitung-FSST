'''
Matura Übungsaufgabe_005 (2 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe von zwei ganzen Zahlen bittet.

Die zwei eingegeben Zahlen sollen dann dividiert werden.
Geben Sie das Ergebnis in der Form "zahl1/zahl2 = result" aus, wobei
das Ergebnis mit 2 Nachkommastellen angezeigt werden soll.

Achtung! Es soll nicht auf 4 Nachkommastellen gerundet werden,
nur im print-command so angezeigt werden! 
Tipp: f-Strings und Formatanweisungen im f-String
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!
Es soll zudem auf Division durch 0 geprüft werden. 

Für Hilfe zur Formatierung siehe "Format Specification Mini-Language" im
"string" (nicht "str"!) Kapitel der Python Doc.

Ausführungsbeispiel:

Please enter the first number ->3
Please enter the second floating point number ->2
3/2=1.50

Erreichbare Punkte: 2
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität 
1 Punkt für die korrekte Formatierung der Ausgabe.
'''

num1, num2, div = None, None, None

num1 = int(input("Please enter the first number -> "))
num2 = int(input("Please enter the second floating point number -> "))

div = num1 / num2

print("%i/%i=%.2f"%(num1, num2, div))
