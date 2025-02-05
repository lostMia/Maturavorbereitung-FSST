'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_06 (5 Punkte)
Angabe:
Erstellen Sie ein Programm für eine Werkzeugverleih. 
Bereits implementiert ist die Klasse Tool, welche einen Werkzeug im Verleih
repräsentiert, welches ausgeliehen werden kann. 

Implementieren Sie folgende Klassen mit den angegebenen Eigenschaften unter Verwendung der Klasse Tool:
* MotorSaw:        Marke (brand), Typ (type), Seriennummer (id), Leistung (power)
                   Kettenlänge (length_of_saw)
* Shovel:          Marke (brand), Identifikationsnummer (id), Länge (length), maximales Gewicht (max_weight)
* DrillingMachine: Marke (brand), Seriennummer (id)
                   max. Drehzahl (max_drive), Futtergröße (chuck_size)

Vergessen Sie nicht, einen sinnvollen Konstruktor bei den Klassen zu erstellen und die 
Methode _get_attributes() zu überschreiben.

Die Klasse Tool darf nicht verändert werden!!!

Erzeugen Sie folgenden Objekte und speichern Sie sie in einer Liste. Iterieren Sie anschließend 
über die Liste und geben Sie die Objektinformation mittels print() aus.
Objekte:
* MotorSaw: Husqvarna, 120 Mark II, AC1982364, 1.9, 35cm
* MotorSaw: STIHL, MS 170, XY098123, 1.6, 30cm
* Shovel: Cemo, SCH10, 130, 20
* Shovel: Nölle, SCH11, 140, 15
* DrillingMachine: Bosch, AB112233, 2800, 13
* DrillingMachine: Makita, CD556677, 3400, 10


Erwartetet Ausgabe:
AC1982364 has been borrowed.
SCH10 has been borrowed.
AB112233 has been borrowed.
CD556677 von Catan has been borrowed.
SCH10 been returned.

Husqvarna, 120 Mark II (AC1982364) borrowed
STIHL MS 170 (XY098123) in stock
Shovel Cemo (SCH10) in stock
Shovel Nölle (SCH11) in stock
Bosch (AB112233, drive=2800, chuck=13) borrowed
Makita (CD556677, 3400, 10) borrowed


Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 5
Aufteilung der Punkte:  
1 Punkt für die Kettensäge-Klasse 
1 Punkt für die Schaufel-Klasse
1 Punkt für die Bohrmaschine-Klasse
1 Punkt für die Erstellung der Objekte
1 Punkt für die richtige Verwendung der _get_attributes() Methode
'''
# Base class for stock item - NICHT VERÄNDERN !!!!!!!!!


class Tool:
    def __init__(self, id, brand):
        self.__id = id
        self.__brand = brand
        self.__is_borrowed = False

    def checkout(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"{self.__id} has been borrowed.")
        else:
            print(f"{self.__id} is already borrowed.")

    def return_item(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            print(f"{self.__id} has been returned.")
        else:
            print(f"{self.__id} has not been borrowed.")

    def _get_attributes(self):
        return f"{self.__id}"

    def __str__(self):
        if self.__is_borrowed:
            return f"{self.__brand} ({self._get_attributes()}) borrowed"
        else:
            return f"{self.__brand} ({self._get_attributes()}) in stock"


class MotorSaw(Tool):
    def __init__(self, id, brand, saw_type, power, length_of_saw):
        super().__init__(id, brand)

        self.saw_type = saw_type
        self.power = power
        self.length_of_saw = length_of_saw

    def _get_attributes(self):
        return f"{self.saw_type}, {self.power}, {self.length_of_saw} cm"


class Shovel(Tool):
    def __init__(self, id, brand, length, max_weight):
        super().__init__(id, brand)

        self.max_weight = max_weight
        self.length = length

    def _get_attributes(self):
        return f"{self.max_weight}, {self.length}"


class DrillingMachine(Tool):
    def __init__(self, id, brand, max_drive, chuck_size):
        super().__init__(id, brand)

        self.max_drive = max_drive
        self.chuck_size = chuck_size

    def _get_attributes(self):
        return f"{self.max_drive}, {self.chuck_size}"

# Erwartetet Ausgabe:
# AC1982364 has been borrowed.
# SCH10 has been borrowed.
# AB112233 has been borrowed.
# CD556677 von Catan has been borrowed.
# SCH10 been returned.
#
# Husqvarna, 120 Mark II (AC1982364) borrowed
# STIHL MS 170 (XY098123) in stock
# Shovel Cemo (SCH10) in stock
# Shovel Nölle (SCH11) in stock
# Bosch (AB112233, drive=2800, chuck=13) borrowed
# Makita (CD556677, 3400, 10) borrowed


tools = []
tools.append(MotorSaw("120 MarkII", "Husqvarne", "AC1982364", 1.9, 35))
tools.append(MotorSaw("MS 170", "STIHL", "XY098123", 1.6, 30))
tools.append(Shovel("SCH10", "Cemo", 130, 20))
tools.append(Shovel("SCH11", "Nölle", 140, 15))
tools.append(DrillingMachine("AB112233", "Bosch", 2800, 13))
tools.append(DrillingMachine("CD556677", "Makita", 3400, 10))

tools[0].checkout()
tools[2].checkout()
tools[4].checkout()
tools[5].checkout()
tools[2].return_item()


print("")

for tool in tools:
    print(tool)
