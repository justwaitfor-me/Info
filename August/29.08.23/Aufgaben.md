# Binärdarstellung von Zahlen
![Info Bild](https://www.inf-schule.de/assets/img/logo/logo_inf-schule_weiss2.png)

### [Link zur Aufgabe](https://www.inf-schule.de/information/darstellunginformation/binaerdarstellungzeichen)

![ASCII Tabelle](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/ASCII-Table.svg/2522px-ASCII-Table.svg.png)

## Einstieg - Gefängnisausbruch

> Aufgabe 1

    (a) AB IN DIE FREI

    (b) 01001000
        01000101
        01001001
        01010100

> Aufgabe 2

    (a) Um den code zu entschlüsseln braucht man eine ASCII Tabelle

    (b) aus und vorbei

## Übungen

> Aufgabe 1

    Code: 01010000 01001001 01000001 01010101 01001110 01000100 01010000 01000001 01010101 01001100

    Übersetzung: PIAUNDPAUL 

> Aufgabe 2

    (a) Der Anfang des Textes lautet "MI,".

    (b) Der gesamte Text lautet "MI,\r\n28.10.09\r\n". 

    Zur Erklärung: Der gegebene Text besteht aus Hexadezimalzahlen, die im erweiterten ASCII-Code dargestellt sind. Um den Text zu dekodieren, muss man die Hexadezimalzahlen in ASCII-Zeichen umwandeln. Im erweiterten ASCII-Code entsprechen die Zahlen 4d und 49 den Buchstaben "M" und "I". Die Zahlen 0d und 0a sind Steuerzeichen für "Carriage Return" und "Line Feed", die in Kombination einen Zeilenumbruch ergeben. Daher ergibt sich für den gesamten Text "MI,\r\n28.10.09\r\n".

> Aufgabe 3

    (a) Zur Darstellung des Textes werden insgesamt 42 Bytes benötigt. 

    (b) Wenn man den Text in Notepad++ eingibt und im Hex-Editor anzeigen lässt, erhält man die folgende Darstellung:

    48 61 6E 6E 69 62 61 6C 20 7A 6F 67 0D 0A 6D 69 74 20 33 37 20 45 6C 65 66 61 6E 74 65 6E 0D 0A 75 65 62 65 72 20 64 69 65 20 41 6C 70 65 6E 2E

    Man erkennt, dass jeder Buchstabe und jedes Zeichen durch zwei Hexadezimalzahlen dargestellt wird.

    (c) Wenn man den Text in Notepad++ speichert und sich die Eigenschaften der Datei anzeigen lässt, wird eine Dateigröße von 42 Bytes angezeigt. Dies entspricht genau der Anzahl der Bytes, die zur Darstellung des Textes benötigt werden.
