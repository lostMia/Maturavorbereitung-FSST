'''
Matura Übungsaufgabe_013 (3 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe zweier Zahlenlimits bittet.
Zählen Sie in Zweierschritten nach oben und
schreiben Sie die Zahlen durch ; getrennt in eine Datei zahlen.txt
je 4 Zahlen pro Zeile, das obere Limit soll in jedem Fall in die Datei 
geschrieben werden.
Ausführungsbeispiel:
    Please enter the lower limit -> 0
    Please enter the upper limit -> 19
    File content:
    0;2;4;6 
    8;10;12;14
    16;18;19
    Achten Sie auf sauberes Schließen des file-streams!
    Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!
    Erreichbare Punkte: 3
    Aufteilung der Punkte:
    1 Punkt für prinzipielle Funktionalität (User-Eingabe, Schreiben der Zahlen ins File)
    1 Punkt für die Formatierung innerhalb des Files
    1 Punkt für das korrekte Schließen des File.
    '''

def get_input():
    lower = int(input("Please enter the lower limit -> "))
    upper = int(input("Please enter the upper limit -> "))

    return [lower, upper]

def write_to_file(lower, upper):
    file = open("zahlen.txt", 'w')

    index = 1
    for i in range(lower, upper, 2):
        file.write(str(i))

        if i > upper - 3:
            break

        if index % 4 == 0:
            file.write("\n")
        else:
            file.write(";")

        index += 1

    file.close()

def main():
    [lower, upper] = get_input()
    write_to_file(lower, upper)

if __name__ == "__main__":
    main()
