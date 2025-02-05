'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_01 (2 Punkte)
Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User um die Eingabe eines Wortes auffordert. Das Programm
soll dann die Morsezeichen für das Wort ausgeben. Ist ein Zeichen nicht im 
Morsealphabet vorhanden, so soll das Zeichen ausgegeben werden.

Beispiel:
I show you a word in Morse code!
Please enter the word: Jog_urt
The spelling is: .--- | --- | --. | _ | ..- | .-. | -

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 2
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität 
1 Punkt für die korrekte Formatierung der Ausgabe.
'''
morse = {
"A" : ".-", 
"B" : "-...", 
"C" : "-.-.", 
"D" : "-..", 
"E" : ".", 
"F" : "..-.", 
"G" : "--.", 
"H" : "....", 
"I" : "..", 
"J" : ".---", 
"K" : "-.-", 
"L" : ".-..", 
"M" : "--", 
"N" : "-.", 
"O" : "---", 
"P" : ".--.", 
"Q" : "--.-", 
"R" : ".-.", 
"S" : "...", 
"T" : "-", 
"U" : "..-", 
"V" : "...-", 
"W" : ".--", 
"X" : "-..-", 
"Y" : "-.--", 
"Z" : "--..", 
"0" : "-----", 
"1" : ".----", 
"2" : "..---", 
"3" : "...--", 
"4" : "....-", 
"5" : ".....", 
"6" : "-....", 
"7" : "--...", 
"8" : "---..", 
"9" : "----.", 
"." : ".-.-.-", 
"," : "--..--"
}


print("I'll show you a word in Morse Code!")
word = input("Please enter the word: ")

morse_str = ""
for character in word:
    try:
        morse_chrs = morse[character.upper()]
    except:
        morse_chrs = character

    morse_str += morse_chrs + " | "

morse_str = morse_str[:-2]

print(f"The spelling is: {morse_str}")
