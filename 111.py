'''
Matura Übungsaufgabe_011 (3 Punkte)

Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe eines File-Namens bittet.
Im File befinden sich integer Zahlen (jeweils 4 Zahlen pro Zeile durch
Leerzeichen getrennt und eine unbekannte Anzahl von Zeilen)

Sie sollen Ausgeben wie viele Zahlen sie gefunden habe und wie
die Summe aller Zahlen lautet.

Ausführungsbeispiel:
File content:
3 4 5 6
7 8 9 10
11 12 13 14
15 16

Please enter the name of the file -> file.txt
Found 14 numbers in the file. The sum of all numbers = 133

Achten Sie auf sauberes Schliessen des file-streams!
Achten Sie auf Absicherung von möglichen Fehlern z.B. falscher Filename

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!
Please enter the name of the file -> file.txt
Found 14 numbers in the file. The sum of all numbers = 133
Erreichbare Punkte: 3
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität (User-Eingabe, öffnen des File) 
1 Punkt für die Absicherung der Usereingabe (z.B. falscher Filename)
1 Punkt für das korrekte Schliessen des File.
'''

file = input("Please enter the name of the file -> ")

numbers = []
open_file = None

try:
    open_file = open(file, 'r')
    content = open_file.read().split("\n")
    open_file.close()

    for line in content:
        nums_line = line.split(" ")

        for i, number in enumerate(nums_line):
            nums_line[i] = int(number)

        numbers += nums_line

except:
    if open_file != None:
        open_file.close()

print(f"Found {len(numbers)} in the file. The sum of all numbers = {sum(numbers)}")
