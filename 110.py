'''
Matura Übungsaufgabe_010 (3 Punkte)

Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe eines beliebigen Satzes (ohne Satz- 
und Sonderzeichen) bittet.
Es soll dann ausgegeben werden aus wie vielen Wörtern er besteht und
im Anschluss daran sollen die Wörter in umgekehrter Reihenfolge
ausgegeben werden.

Vorgaben:
Die zwei Aufgaben sollen in eigenen Funktionen bearbeitet werden und
ihre Ergebnisse an das Hauptprogramm zurück geben.

Die Ausgabe der Ergebnisse soll mittels print Funktion in der Form:
"your string consists of #-words and backwards it looks like this:" erfolgen.
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Ausführungsbeispiel:
Please enter a string containing multiple words ->roger the rabbit runs fast
Your string contains 5 words and backwards it looks like this:
 fast runs rabbit the roger
 
 Erreichbare Punkte: 3
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität (User-Eingabe, Ermittlung
  von Wort- und Zeichenanzahl und Ausgabe)
1 Punkt für die Funktionsdefinitionen und -Aufruf (mit Übergabeparameter)
1 Punkt für den korrekten Rückgabewert
'''

def get_sentence():
    return input("Please enter a string containing multiple words ->")

def get_words(sentence):
    words = sentence.split()

    return words

def main():
    sentence = get_sentence()
    words = get_words(sentence)
    words.reverse()

    print(f"Your string consists of {len(words)}-words and backwards it looks like this: \n{" ".join(words)}")

if __name__ == "__main__":
    main()
