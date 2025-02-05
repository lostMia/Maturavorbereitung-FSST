'''
Matura Übungsaufgabe_014 (3 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe zweier Zahlenlimits bittet.
Zählen Sie in einer vom Benutzer gewählten Schrittweite nach oben und
schreiben Sie die Zahlen durch : getrennt in eine Datei test.csv
je 2 Zahlen pro Zeile, das obere Limit soll in jedem Fall in die Datei 
geschrieben werden.
Ausführungsbeispiel:
Please enter the lower limit ->0
Please enter the upper limit ->19
Please enter offset -> 3
File content:
0:3 
6:9
12:15
18:19
Achten Sie auf sauberes Schließen des file-streams!
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!
Erreichbare Punkte: 3
Aufteilung der Punkte:
1 Punkt für prinzipielle Funktionalität (User-Eingabe, Schreiben der Zahlen ins File)
1 Punkt für die Formatierung innerhalb des Files
1 Punkt für das korrekte Schließen des File.
'''

def get_input():
    # lower = int(input("Please enter the lower limit -> "))
    # upper = int(input("Please enter the upper limit -> "))
    # offset = int(input("Please enter the offset -> "))
    #
    # return [lower, upper, offset]
    return [0, 22, 3]

def write(lower, upper, offset):
    file = open("test.csv", 'w')

    index = 1
    last_index = 0
    for i in range(lower, upper, offset):
        last_index = i
        file.write(str(i))

        write_seperator(file, index)
        index += 1

    if last_index != upper:
        file.write(str(upper))

    file.close()

def write_seperator(file, index):
    if index % 2 == 0:
        file.write("\n")
    else:
        file.write(":")

def main():
    [lower, upper, offset] = get_input()
    write(lower, upper, offset)

if __name__ == "__main__":
    main()
