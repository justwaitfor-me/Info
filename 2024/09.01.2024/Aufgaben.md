# Grundgatter
![Logo des digitalen Schulbuchs inf-schule.de. Schriftzug in Zustandsübergangsdiagramm eines endlichen Automaten.](https://www.inf-schule.de/assets/img/logo/logo_inf-schule_weiss2.png)

### [Link zur Aufgabe](https://www.inf-schule.de/rechner/digitaltechnik/gatter/ein_oder_tuer)

# Erkundung - Grundgatter
T: Tür
K: Knopf
M: Motor

Schaltfunktion:
M = T ^ K

# Erkundung - Grundgatter
> Aufgabe 1

	(a) Die Tür soll auf gehen wenn einer der beiden Schalter gedrückt wird
	
	(b) t1: türschalter 1, t2: türschalter 2, t: tür

    (c) t1 | t2 | t
        -----------
        X  | O | X
        O  | X | O

    (d) t = t1 v t2

# Einstieg - Kühlschrank
> Aufgabe 1

    (a) Die Lampe soll angegehn wenn der Türsensor nicht gedrückt ist 

    (b) l: licht, ts: türsensor

    (c) ts | l
        -------
        X  | O 
        O  | X 

    (d) l = !ts

