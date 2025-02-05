'''
Matura Übungsaufgabe_015 (4 Punkte)

Schreiben Sie eine Python Klasse, welche ein Tier beschreibt!
Die Klasse Tier soll folgende Attribute haben:
# Gattung
# Name
# Unterarten (Anzahl der Subspezies)
# Lebensdauer (in Jahren)
# Population (als ganze Zahl)
Lebensdauer und Population sollen optionale Parameter in der init-Methode sein. Wenn sie beim Erzeugen 
des Objekts nicht übergeben werden, sollen sie einen default Wert von 0 haben! Implementieren Sie 
eine Methode 'ist_gefaehrdet()' welche abhängig von der Population unterschiedliche print-statements liefert. z.B.:
Population - 0 -> Ausgabe: "dead end:-("
Population - 10000 -> Ausgabe: "help me!"
Population - 1,000,000 -> Ausgabe: "fine, thanx:-)"
Implementieren Sie auch eine __str__(self) Methode, welche die String Repräsentation eines
Objekts darstellt. Alle Attribute sollen in einer Formatierung Ihrer Wahl dargestellt
werden.
Erstellen Sie dann ein paar Tier Objekte (mindestens drei mit unterschiedlichen Populationen)
Speichern Sie diese in einer Liste. Iterieren Sie über die Liste und rufen Sie jeweils
die ist_gefaehrdet() Methode und die print() Funktion auf.
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!
Ausführungsbeispiel:
Saeugetier, Pferd, 122 known subspecies and 10,000,000 known species.
fine, thanx:-)
Reptilien, Galpagosechse, 3 known subspecis and 500 known species.
help me!
Unbekannt, Dinosauerier, 1000 known subspecies and 0 known species.
dead end:-(
Erreichbare Punkte: 4
Aufteilung der Punkte:
1 Punkt für die Definition der Klasse inklusive 'Konstruktor'
1 Punkt für die korrekte Implementierung der __str__() und ist_gefaehrdet() Methoden
1 Punkt für die Erstellung und Speicherung der Objekte
1 Punkt für die korrekte Darstellung der Objekte und des Methodenaufrufe
'''

class Animal:
    def __init__(self, genus, name, subtype, lifetime=0, population=0):
        self.genus = genus
        self.name = name
        self.subtype = subtype
        self.lifetime = lifetime
        self.population = population

    def is_endangered(self):
        if self.population < 10000:
            print("dead end :-(")
        elif self.population < 1000000:
            print("help me!")
        else:
            print("fine, thanx :-)")

    def __str__(self):
        return f"Genus: {self.genus} | Name: {self.name} | Subtype: {self.subtype} | Lifetime: {self.lifetime} | Population: {self.population}"

def main():
    animals = []
    animals.append(Animal("Snaek", "Snake", 12, 50, 1156846))
    animals.append(Animal("Bear", "Bear", 23, 100, 266455))
    animals.append(Animal("BZZT", "Bee", 566, 3, 26578466))
    animals.append(Animal("eeeeeeeeel", "Eel", 45, 10, 2499))

    for animal in animals:
        animal.is_endangered()
        print(animal)

if __name__ == "__main__":
    main()
