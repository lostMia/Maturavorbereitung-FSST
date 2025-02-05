'''
Matura Übungsaufgabe_016 (4 Punkte)

Schreiben Sie eine Python Klasse, welche ein Fahrzeug beschreibt!
Die Klasse Fahrzeug soll folgende Attribute haben:
# Marke
# Name
# Fuehrerscheintyp
# PS
# Listenpreis
PS und Listenpreis sollen optionale Parameter in der init-Methode sein. Wenn sie beim Erzeugen 
des Objekts nicht übergeben werden, sollen sie einen default Wert von 0 haben! Implementieren Sie 
eine Methode 'fahren()' welche abhängig von den PS unterschiedliche print-statements liefert. z.B.:
PS - 0 -> Ausgabe: "slowly slowly!"
PS 100 -> Ausgabe: "come on..."
PS 500 -> Ausgabe: "let's go:-)"
Implementieren Sie auch eine __str__(self) Methode, welche die String Repräsentation eines
Objekts darstellt. Alle Attribute sollen in einer Formatierung Ihrer Wahl dargestellt
werden.
Erstellen Sie dann ein paar Fahrzeug Objekte (mindestens drei mit unterschiedlichen PS)
Speichern Sie diese in einer Liste. Iterieren Sie über die Liste und rufen Sie jeweils
die fahren() Methode und die print() Funktion auf.
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!
Ausführungsbeispiel:
Audi, R8, B, power 300, price: 3,000,000EUR.
let's go:-)
Mistral, Citybike, NONE, power 9, price: 200EUR.
slowly slowly!
Triumph, 3R, A, power 90, price: 10,000EUR.
come on...
Erreichbare Punkte: 4
Aufteilung der Punkte:
1 Punkt für die Definition der Klasse inklusive 'Konstruktor'
1 Punkt für die korrekte Implementierung der __str__() und fahren() Methoden
1 Punkt für die Erstellung und Speicherung der Objekte
1 Punkt für die korrekte Darstellung der Objekte und des Methodenaufrufe
'''

class Vehicle:
    def __init__(self, brand, name, drivers_license_type, hp=0, price=0):
        self.brand = brand
        self.name = name
        self.drivers_license_type = drivers_license_type
        self.hp = hp
        self.price = price

    def drive(self):
        if self.hp < 100:
            print("slowly slowly!")
        elif self.hp < 500:
            print("come on...")
        else:
            print("let's go :-)")

    def __str__(self):
        return f"brand: {self.brand} | name: {self.name} | drivers license: {self.drivers_license_type} | hp: {self.hp} | price: {self.price}"

vehicles = []

vehicles.append(Vehicle("Audi", "R8", "B", 300, 3000000))
vehicles.append(Vehicle("Mistral", "Citybike", "NONE", 9, 200))
vehicles.append(Vehicle("Triumph", "33", "A", 120, 10000))

for vehicle in vehicles:
    vehicle.drive()
    print(vehicle)
