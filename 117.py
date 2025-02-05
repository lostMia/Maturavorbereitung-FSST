'''
Matura Übungsaufgabe_017 (4 Punkte)

Schreiben Sie eine Python Klasse, welche ein Konto beschreibt!
Die Klasse Konto soll folgende Attribute haben:
# Bank
# Typ
# Inhaber
# Bindung (in Jahren)
# Kontostand (in EUR)
Limit und Kontostand sollen optionale Parameter in der init-Methode sein. Wenn sie beim Erzeugen 
des Objekts nicht übergeben werden, sollen sie einen default Wert von 0 haben! Implementieren Sie 
eine Methode 'abheben()' welche abhängig von Kontostand unterschiedliche print-statements liefert. z.B.:
Kontostand - 0 -> Ausgabe: "Nope:-("
Kontostand - 100 -> Ausgabe: "not too much"
Kontostand -> 10,000 Ausgabe: "your'welcome:-)"
Implementieren Sie auch eine __str__(self) Methode, welche die String Repräsentation eines
Objekts darstellt. Alle Attribute sollen in einer Formatierung Ihrer Wahl dargestellt
werden.
Erstellen Sie dann ein paar Konto Objekte (mindestens drei mit unterschiedlichen Kontostand)
Speichern Sie diese in einer Liste. Iterieren Sie über die Liste und rufen Sie jeweils
die abheben() Methode und die print() Funktion auf.
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!
Ausführungsbeispiel:
Hypo, Sparbuch, Alice, 3 year(s), balance: 0EUR.
Nope:-(
Volksbank, Girokonto, Bob, 0 year(s), balance: 200EUR.
not too much
Post, Onlinekonto, Eve, 1 year(s), balance: 10,000EUR.
you're welcome:-)
Erreichbare Punkte: 4
Aufteilung der Punkte:
1 Punkt für die Definition der Klasse inklusive 'Konstruktor'
1 Punkt für die korrekte Implementierung der __str__() und abheben() Methoden
1 Punkt für die Erstellung und Speicherung der Objekte
1 Punkt für die korrekte Darstellung der Objekte und des Methodenaufrufe
'''


class Account:
    def __init__(self, bank, account_type, owner, years, money=0, limit=0):
        self.bank = bank
        self.account_type = account_type
        self.owner = owner
        self.years = years
        self.money = money
        self.limit = limit

    def withdraw(self):
        if self.money < 100:
            print("Nope :-(")
        elif self.money < 10000:
            print("not too much")
        else:
            print("You're welcome :-)")

    def __str__(self):
        return f"{self.bank}, {self.account_type}, {self.owner}, {self.years} year(s), balance {self.money} EUR"


accounts = []

accounts.append(Account("Hypo", "Sparbuch", "Alice", 3, 0))
accounts.append(Account("Volksbank", "Girokonto", "Bob", 0, 200))
accounts.append(Account("Post", "Onlinekonto", "Eve", 1, 10000))

for account in accounts:
    account.withdraw()
    print(account)
