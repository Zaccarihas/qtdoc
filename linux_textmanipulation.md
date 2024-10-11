# Linux Textmanipulering

Eftersom det mesta i Linux baseras på textfiler så är det en mycket viktig färdighet att kunna manipulera text på olika sätt. 
I Linux så kopplar man oftast ihop flera små kommandon med en begränsad men tydlig funktion till en mer komplex åtgärd som t ex kommandot **cat** som visar innehållet i en textfil
med kommandot **grep** som filtrerar texten i filen med ett reguljärt uttryck för att sedan presentera textrader med ett specifikt innehåll 
(se följande exempel som resulterar i alla rader som innehåller texten __mariadb__ i filen __apche.conf__)
~~~
cat apache.conf | grep mariadb
~~~

## Textmanipulerinskommandon
I tabellen som följer har jag listat några av de vanligaste och mest användbara kommandona för textmanipulering

|Kommando|Beskrivning                            |
|--------|---------------------------------------|
| grep   | applicerar regex-filter               |
| tr     | ersätter tecken                       |
| awk    | manipulerar texten via ett awk-script |
| cat    | skriver ut en text                    |
| sed    | inline texteditor                     |

