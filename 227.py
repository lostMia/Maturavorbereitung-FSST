'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_07 (5 Punkte)
Angabe:
Visualisieren Sie mit Hilfe von Matplotlib die Häufigkeitsverteilung
von Münzwürfen.

Der User soll eingeben können wie viele Münzen er verwenden will,
und wie viele Würfe simuliert werden sollen.

In einer eigenen Funktion die als Parameter die Anzahl der Münzen und die Würfe
hat, sollen die Anzahl der Zahl-Seiten der Münzen (Summe aller Kopf- und Zahl-Seiten)
in einer Liste gespeichert werden. Dabei zählt eine Kopf-Seite für den Wert 1 und
eine Zahl-Seite für den Wert 0.
Info zur Liste: Wenn z.B. mit zwei Münzen hundertmal geworfen wird, enthält die
Liste hundert Einträge, die jeweils 0, 1 oder 2 sein können.
Diese Liste soll an das Hauptprogramm zurückgegeben werden, und dort mit Hilfe 
von Matplotlibs Histogramplot visualisiert werden.
Im Titel soll die Anzahl der Münzen und der Würfe angezeigt werden -> siehe 
Beispiel Screenshot: 027_practice.png


##### Beispielcode für Matplotlib ######
import matplotlib.pyplot as plt

# Create the histogram, where results is the list from the dice throw
plt.hist(results, bins=range(min(results), max(results) + 2), edgecolor='black', align='left')

# Set the x-ticks to match the bin edges
plt.xticks(range(min(results), max(results) + 2))

# Add titles and labels
plt.title("some title")
plt.xlabel("some x label")
plt.ylabel("some y label")

# Show the plot
plt.show()
########################################


Erreichbare Punkte: 5
Aufteilung der Punkte:  
1 Punkt für die User-Eingabe 
2 Punkt für korrekte Implementierung der Funktion (Parameter, Berechnung, Rückgabe)
1 Punkt für die korrekte Erstellung des Diagramms
1 Punkt für die vollständige Beschriftung (Titel, Achsen) des Diagramms.
'''
# Lösung bitte ab hier!

import matplotlib.pyplot as plt
import random


def throw(coins, throws):
    # heads = 1, tails = 0
    # outcomes = [0, 1, 0, 2, 1, ...]
    outcomes = []

    for throw in range(throws):
        sum = 0

        for coin in range(coins):
            result = random.randint(0, 1)
            sum += result

        outcomes.append(sum)

    return outcomes


def plot(outcomes, coins, throws):
    # Create the histogram, where outcomes is the list from the dice throw
    plt.hist(outcomes, bins=range(min(outcomes), max(outcomes) + 2),
             edgecolor='black', align='left')

    # Set the x-ticks to match the bin edges
    plt.xticks(range(min(outcomes), max(outcomes) + 2, 20))

    # Add titles and labels
    plt.title(f"Number of {coins} and {throws} throws")
    plt.xlabel("Sum of toss")
    plt.ylabel("Frequency of occurances")

    # Show the plot
    plt.show()


def main():
    coins = int(input("How many coins do you want to flip? ->"))
    throws = int(input("How many times do you want to flip them? ->"))

    outcomes = throw(coins, throws)

    plot(outcomes, coins, throws)


if __name__ == "__main__":
    main()
