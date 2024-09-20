# Murmelrechner
![Logo des digitalen Schulbuchs inf-schule.de. Schriftzug in Zustandsübergangsdiagramm eines endlichen Automaten.](https://www.inf-schule.de/assets/img/logo/logo_inf-schule_weiss2.png)

### [Link zur Aufgabe](https://inf-schule.de/rechner/bonsai/murmelrechner)

# Rechnen mit Murmeln
> Aufgabe 1
    (a) Um eine Addition durchzuführen, fügt man die entsprechende Anzahl von Murmeln zum Zielbecher hinzu. Beispielsweise für 3 + 4: Man beginnt mit 3 Murmeln im Becher und fügt dann 4 weitere hinzu, indem man viermal die Inkrementier-Operation ausführt.

    (b) Bei der Subtraktion entfernt man die entsprechende Anzahl von Murmeln aus dem Becher. Für 7 - 3: Man startet mit 7 Murmeln und wendet dreimal die Dekrementier-Operation an.

    (c) 1. Prüfe, ob Murmeln in Becher 0 sind.
        2. Wenn ja, entferne eine Murmel aus Becher 0 und füge sie Becher 1 hinzu.
        3. Wiederhole Schritte 1 und 2, bis Becher 0 leer ist.

    (d) 1. Verwende einen temporären Becher (Becher 2).
        2. Verschiebe den Inhalt von Becher 0 in Becher 2.
        3. Verschiebe den Inhalt von Becher 1 in Becher 0.
        4. Verschiebe den Inhalt von Becher 2 in Becher 1.

    (e) 1. Beginne mit einem leeren Zielbecher.
        2. Füge dreimal jeweils 4 Murmeln hinzu (also viermal inkrementieren, dreimal wiederholen)

#Befehle und Programme
> Aufgabe 1

    inc x: Fügt eine Murmel zum Becher x hinzu
    dec x: Entfernt eine Murmel aus Becher x
    tst x: Prüft, ob Murmeln in Becher x sind
    jmp n: Springt zur Programmzeile n
    hlt: Beendet das Programm

> Aufgabe 2

    0 tst 0
    1 jmp 3
    2 jmp 6
    3 dec 0
    4 inc 2
    5 jmp 0
    6 tst 1
    7 jmp 9
    8 jmp 12
    9 dec 1
    10 inc 0
    11 jmp 6
    12 tst 2
    13 jmp 15
    14 jmp 18
    15 dec 2
    16 inc 1
    17 jmp 12
    18 hlt