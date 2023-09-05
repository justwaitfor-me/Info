# Binärdarstellung von Zeichen
![Logo des digitalen Schulbuchs inf-schule.de. Schriftzug in Zustandsübergangsdiagramm eines endlichen Automaten.](https://www.inf-schule.de/assets/img/logo/logo_inf-schule_weiss2.png)

### [Link zur Aufgabe](https://www.inf-schule.de/information/darstellunginformation/darstellunginformation)

## Exkurs - Experimente mit einem Hexeditor
> Aufgabe 1

    B = 0100 0010
    C = 0100 0011

    00001101 = carrige return (/r)
    00001010 = line feed

    Man kann 256 Zeichen darstellen (2^8).

    UTF-8 Sonderzeichen, wie zum Beispiel [space], werden als '.' dargestellt.

> Aufgabe 2
 
    Bei einem anderen OS braucht man keine tube (/r oder 00001101).

## Einstieg - Unicode
Um die Bitfolgen für die Währungssymbole zu identifizieren, müssen wir uns auf die gegebenen 16-Bit-Folgen konzentrieren und herausfinden, welche davon den Währungssymbolen entsprechen. Hier sind die 16-Bit-Folgen, die den Währungssymbolen entsprechen:

> Aufgabe 1

    (a) Die Bitfolgen für die Währungssymbole sind:

    - Euro (€): 0010000010101100
    - Japanischer Yen (¥): 0010000010100101
    - Russischer Rubel (₽): 0010000010111101
    - Südkoreanischer Won (₩): 0010000010101001
    - Israelischer Schekel (₪): 0010000010101010

    (b) Um die entsprechenden Symbole im Internet zu recherchieren, können wir die Bitfolgen in Dezimal- oder Hexadezimalzahlen umrechnen und den Suchtext "Unicode [Hexadezimalwert]" verwenden. Zum Beispiel:

    - Euro (€): Unicode 20AC
    - Japanischer Yen (¥): Unicode 00A5
    - Russischer Rubel (₽): Unicode 20BD
    - Südkoreanischer Won (₩): Unicode 20A9
    - Israelischer Schekel (₪): Unicode 20AA

    (c) Um weitere Währungssymbole darzustellen, wie den thailändischen Baht (฿) oder den vietnamesischen Dong (₫), können wir eine Unicode-Tabelle verwenden und einen Converter benutzen, der Unicode in Textsymbole umwandelt. Zum Beispiel:

    - Thailändischer Baht (฿): Unicode 0E3F
    - Vietnamesischer Dong (₫): Unicode 20AB


