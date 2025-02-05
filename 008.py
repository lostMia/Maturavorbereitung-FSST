'''
Matura Übungsaufgabe_008
 (2 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe von zwei Kommazahlen bittet.

Die zwei eingegeben Zahlen sollen dann exponentiell verknüpft werden.
Geben Sie das Ergebnis in der Form "zahl1´`zahl2 = result" aus, wobei
das Ergebnis mit 5 Nachkommastellen angezeigt werden soll.

Achtung! Es soll nicht auf 5 Nachkommastellen gerundet werden,
nur im print-command so angezeigt werden! 
Tipp: f-Strings und Formatanweisungen im f-String
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Für Hilfe zur Formatierung siehe "Format Specification Mini-Language" im
"string" (nicht "str"!) Kapitel der Python Doc.

Ausführungsbeispiel:

Please enter 1st floating point ->3
Please enter 2nd floating point ->2
3´`2=9.00000

Erreichbare Punkte: 2
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität 
1 Punkt für die korrekte Formatierung der Ausgabe.
'''


num1 = float(input("Please enter the first floating point ->"))
num2 = float(input("Please enter the second floating point ->"))

res = num1 ** num2

print("%.0f^%.0f=%.5f"%(num1, num2, res))
