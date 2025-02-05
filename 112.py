'''
Matura Übungsaufgabe_012 (3 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe zweier Zahlenlimits bittet.
Berechnen Sie ein bestimmte Menge an Zufallszahlen in diesem Bereich.
Die Anzahl der Zufallszahlen soll ebenfalls vom Benutzer eingegeben werden.
Schreiben Sie dann alle Zahlen durch , getrennt in eine Datei numbers.txt
je 3 Zahlen pro Zeile
keine Sortierung
Ausführungsbeispiel:
Please enter the lower limit -> 2
Please enter the upper limit -> 20
Please enter number of values -> 5
File content:
2,20,3
4,19
Achten Sie auf sauberes Schließen des file-streams!
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!
Erreichbare Punkte: 3
Aufteilung der Punkte:
1 Punkt für prinzipielle Funktionalität (User-Eingabe, Schreiben der Zahlen ins File)
1 Punkt für die Formatierung innerhalb des Files
1 Punkt für das korrekte Schließen des File.
'''

import random

def get_input():
    lower = int(input("Please enter the lower limit -> "))
    upper = int(input("Please enter the upper limit -> "))
    numbers = int(input("Please enter number of values -> "))

    return [lower, upper, numbers]

def generate_numbers(lower, upper, numbers):
    number_list = []
    for i in range(numbers):
        number_list.append(random.randint(lower, upper))

    return number_list

def write_to_file(number_list):
    file_name = "numbers.txt"

    file = open(file_name, "w")

    for i in range(1, len(number_list) + 1):
        file.write(str(number_list[i - 1]))

        if i == len(number_list):
            break

        if i % 3 == 0 and i != 0:
            file.write("\n")
        else:
            file.write(",")

    file.close()

def main():
    [lower, upper, numbers] = get_input()
    number_list = generate_numbers(lower, upper, numbers)
    write_to_file(number_list)

if __name__ == "__main__":
    main()
