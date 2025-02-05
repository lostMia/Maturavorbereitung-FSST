'''
Matura Übungsaufgabe_018 (4 Punkte)

Angabe:
Visualisieren Sie mit Hilfe von Matplotlib eine kubische Gleichung der Form:
y=ax³+bx²+cx+d
Der User soll die Paramter a,b,c und d eingeben sowie die Start und Stoppunkte
auf der x-Achse und die Anzahl der Punkte auf der x-Achse.

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

### Beispielhafte Eingabe:
Welcome to the cubic visualizer!
Form of the equation: ax³+bx²+cx+d=0
Enter the parameter a=1
Enter the parameter b=3
Enter the parameter c=0
Enter the parameter d=-2
Enter starting point on the x-axis ->-4
Enter end point on the x-axis ->3
Enter number of points on the x-axis ->20


##### Beispielcode für Matplotlib #####
import matplotlib.pyplot as plt
import math

x_values = []
y_values = []

#calculate values for a sine function
for deg in range (0,361,10):
    y = math.sin(math.radians(deg))
    y_values.append(y)
    x_values.append(deg)

plt.plot(x_values, y_values)
plt.title("The sine function")
plt.ylabel("f(x)=sin(x)")
plt.xlabel("Degrees")
plt.show()
########################################

Erreichbare Punkte: 4
Aufteilung der Punkte:
1 Punkt für die User-Eingabe
2 Punkt für die korrekte Berechung der y-Werte
1 Punkt für die korrekte Erstellung des Diagramms inklusive Beschriftungen
'''
import matplotlib.pyplot as plt


def show(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.title("The sine function")
    plt.ylabel("f(x)=sin(x)")
    plt.xlabel("Degrees")
    plt.show()


def get_parameters():
    a = int(input("Enter the parameter a="))
    b = int(input("Enter the parameter b="))
    c = int(input("Enter the parameter c="))
    d = int(input("Enter the parameter d="))
    start = int(input("Enter starting point on the x-axis ->"))
    end = int(input("Enter end point on the x-axis ->"))
    points = int(input("Enter number of points on the x-axis ->"))

    return [a, b, c, d, start, end, points]


def calculate_points(a, b, c, d, start, end, points):
    diff = (end - start) / points
    x_values = [
        i / 100 for i in range(start * 100, end * 100, int(diff * 100))]
    y_values = []

    for x in x_values:
        value = a * (x ** 3) + b * (x ** 2) + c * x + d
        y_values.append(value)

    return [x_values, y_values]


def main():
    print("Welcome to the cubic visalizer!")

    [a, b, c, d, start, end, points] = get_parameters()
    [x_values, y_values] = calculate_points(a, b, c, d, start, end, points)

    show(x_values, y_values)


if __name__ == "__main__":
    main()
