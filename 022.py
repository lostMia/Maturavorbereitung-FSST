'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_02 (2 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe zweier Gleitkommazahlen bittet. Das Programm
soll dann die zwei Zahlen vergleichen und die kleinere der beiden Zahlen ausgeben.
The smaller number of 3 and 5 is 3.

Beispiel:
Please enter number #1 -> 8
Please enter number #2 -> 5
The smaller number of 8 and 5 is 5.

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 2
Aufteilung der Punkte:  
1 Punkt für die richtige Funktionalität der Eingabe/Ausgabe
1 Punkt für die Auswertung, welche Zahl größer/kleiner
'''

# Lösung bitte ab hier!

num1 = float(input("Please enter number #1 -> "))
num2 = float(input("Please enter number #2 -> "))

print("The smaller number of %.0f and %.0f is %.0f"%(num1, num2, min([num1, num2])))
