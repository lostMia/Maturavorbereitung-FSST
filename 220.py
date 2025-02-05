'''
Matura Übungsaufgabe_020 (4 Punkte)

Angabe:
OOP-Beispiel: Schreiben Sie eine Python Klasse, welche ein Auto beschreibt!
Die Klasse soll folgende Attribute haben:
# Hersteller
# Name
# Leistung in PS
# Verbrauch in l/100km
# Allrad (True/False)

Der Verbrauch und Allrad sollen optionale Parameter in der init-Methode sein.
Wenn sie beim Erzeugen des Objekts nicht übergeben werden, sollen sie einen default Wert
von 10l/100km und False haben!

Implementieren Sie eine Methode 'fahren' welche abhängig von der Leistung unterschiedliche
print-statements ausgibt. z.B.:
 Leistung 0 - 50PS -> Ausgabe: "slowly, slowly!"
 Leistung 50 - 100PS -> Ausgabe: "Juhu, that is fun!"
 Leistung größer 100PS -> Ausgabe: "Too much power - I am scard :/"

Implementieren Sie auch eine __str__(self) Methode, welche die String Repräsentation eines
Objekts darstellt. Alle Attribute sollen in einer Formatierung Ihrer Wahl dargestellt werden.

Erstellen Sie dann ein paar Auto Objekte (mindestens drei mit unterschiedlichen Leistungen)
Speichern Sie diese in einer Liste. Iterieren Sie über die Liste und rufen Sie jeweils die fahren() 
Methode und die print() Funktion auf.
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Ausführungsbeispiel:
Skoda, Fabia, 49 PS and 7 l/100km fuel consumption. All wheel drive = False
slowly, slowly!

BMW, X5, 120 PS and 10 l/100km fuel consumption. All wheel drive = True
Too much power - I am scard :/

Audi, A4, 75 PS and 10 l/100km fuel consumption. All wheel drive = False
Juhu, that is fun!


Erreichbare Punkte: 4
Aufteilung der Punkte:  
1 Punkt für die Definition der Klasse inklusive 'Konstruktor'
1 Punkt für die korrekte Implementierung der __str__ und fahren Methoden
1 Punkt für die Erstellung und Speicherung der Objekte
1 Punkt für die korrekte Darstellung der Objekte und des Methodenaufrufes
'''


class Car:
    def __init__(self, maker, name, hp, consumption=10, four_wheel_drive=False):
        self.maker = maker
        self.name = name
        self.hp = hp
        self.consumption = consumption
        self.four_wheel_drive = four_wheel_drive

    def drive(self):
        if self.hp < 50:
            print("slowly, slowly!")
        elif self.hp < 100:
            print("JUhu, that is fun!")
        else:
            print("Too much power - I am scared :/")

    def __str__(self):
        return f"{self.maker}, {self.name}, {self.hp} PS and {self.consumption} l/Z  km fuel consumption. All wheel drive = {self.four_wheel_drive}"


cars = []

cars.append(Car("Skoda", "Fabia", 49, 7, False))
cars.append(Car("BMW", "X5", 120, 10, True))
cars.append(Car("Audi", "A4", 75))

for car in cars:
    car.drive()
    print(car)
