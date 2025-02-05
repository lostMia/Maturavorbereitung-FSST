'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_05 (4 Punkte)

Angabe:
Thread-Beispiel:
Erstellen Sie ein Programm, welches vier Threads erzeugt. Jeder dieser Threads bekommt
aufsteigend eine Zahl zugewiesen und zusätzlich eine zufällige Zahl zwischen 5 und 15 zugewiesen.
Der Thread soll von seiner Thread-Nummer bis zur zufälligen Zahl zählen, 
z.B. Thread 3 mit Zahl 21 soll von 3 bis 21 zählen.
Zwischen jedem Zählschritt soll eine Pause von 10ms liegen. Jede Zahl ist auszugeben im Format:
* 15 * (Thread 3)
Zusätzlich ist in jedem Thread das Produkt der ausgegebenen Zahlen zu berechnen.

Erstellen Sie eine globale Variable overall_result und initialisieren Sie diese mit dem Wert 0.
Am Ende eines jeden Threads soll in dieser Variable die Produkte der Zahlen hinzuaddiert werden.
Gewährleisten Sie, dass der Zugriff auf diese Variable geschützt ist (Lock/Mutex).

Beispielausgabe:
* 1 * (Thread 1)
* 2 * (Thread 2)
* 3 * (Thread 3)
* 4 * (Thread 4)
* 2 * (Thread 1)
* 3 * (Thread 2)
.
.
.
* 10 * (Thread 1)
* 12 * (Thread 3)
Sum of all threads: 1200


Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 4
Aufteilung der Punkte:
1 Punkt für die korrekte Erzeugung der Threads
1 Punkt für die korrekte Funktionalität (Zählen, Produkt/Summe bilden und Ausgabe)
1 Punkt für die richtige Absicherung der overall_result Variable
1 Punkt für das Abwarten auf alle Threads
'''
#


from threading import Thread, Lock
import random
import time


def count(start, end):
    global overall_result, result_lock

    sum = 0
    for i in range(start, end):
        print(f"* {i} * (Thread {start})")
        sum += i * start
        time.sleep(0.010)

    result_lock.acquire()
    overall_result += sum
    result_lock.release()


overall_result = 0
result_lock = Lock()
threads = []

for i in range(1, 5):
    thread = Thread(target=count, args=(i, random.randint(5, 15)))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Sum of all threads: {overall_result}")
