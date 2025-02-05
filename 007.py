'''
Matura Übungsaufgabe_007 (2 Punkte)
Angabe:
Schreiben  Sie ein Python Commandline Programm, welches
dem User hilft 2er Potenzen (2^x) übersichtlich darzustellen.

Der User soll die Anzahl der Wiederholungen als Integer eingeben.
Die Formatierung der Ausgabe im Ausführungsbeispiel ist optional, aber
einen der möglichen Punkte wert!

Ausführungsbeispiel:
Please enter number of iterations -> 4
                  2^1 =  2
				  2^2 =  4
				  2^3 = 16
				  2^4 = 32
				 


Für Hilfe zur Formatierung siehe "Format Specification Mini-Language" im
"string" (nicht "str"!) Kapitel der Python Doc.

Erreichbare Punkte: 2
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität 
1 Punkt für die korrekte Formatierung der Ausgabe.
'''


rep = int(input("Please enter number of iterations -> "))

for i in range(1, rep + 1):
    print("2^%i = %2i"%(i, 2**i))

