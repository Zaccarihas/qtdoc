- [https://www.geeksforgeeks.org/awk-command-unixlinux-examples/](https://www.geeksforgeeks.org/awk-command-unixlinux-examples/)
- [https://sv.wikipedia.org/wiki/Awk](https://sv.wikipedia.org/wiki/Awk)
- [https://www.gnu.org/software/gawk/manual/gawk.html](https://www.gnu.org/software/gawk/manual/gawk.html)
- [https://www.tutorialspoint.com/awk/index.htm](https://www.tutorialspoint.com/awk/index.htm)

# AWK

Det finns flera varianter av script-språket awk bl a:
- awk
- nawk
- gawk

## Workflow
- read
- execute
- repeat

Läs in en rad från strömmen
Utför ett kommando på raden
Upprepa tills strömmen är tom

## Structure
Alla kommandon skrivs med versaler
BEGIN { utförs före körning }
/pattern/ { kommandon att utföra på varje rad }
END { utförs efter strömmen av text är tom }

## Syntax
|Kommando|Beskrivning|
|--------|-----------|
|print   | Skriver ut raden till output strömmen |
|printf   | Skriver ut formaterat |

## Options
|Alternativ|Beskrivning|
|--------|-----------|
|-f __filnamn__   | Kör scriptet i en extern __.awk__ fil |
|-v __variabel = värde__ | Tillskriver en variabel ett värde |




