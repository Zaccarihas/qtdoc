# Dataview

## Alternativ

| Alternativ   | Beskrivning                                     |
|--------------|-------------------------------------------------|
| file.name    | Filnamnet                                       |
| file.folder  | Mappnamnet där filen är placerad                |
| file.path    | Sökväg till filen (mapp+filnamn)                |
| file.ext     | Filtyp (vanligtvis .md)                         |
| file.link    | En länk till filen                              |
| file.size    | Filstorlek (Bytes)                              |
| file.ctime   | Datum då filen skapades (kräver Time-tillägget) |
| file.cday    | Datum då filen skapades                         |
| file.mtime   | Datum då filen ändrades (kräver Time-tillägget) |
| file.mday    | Datum då filen ändrades                         |
| file.tags	   | A list of all unique tags in the note. Subtags are broken down by each level, so #Tag/1/A will be stored in the list as [#Tag, #Tag/1, #Tag/1/A].
file.etags	A list of all explicit tags in the note; unlike file.tags, does not break subtags down, i.e. [#Tag/1/A]
file.inlinks	A list of all incoming links to this file, meaning all files that contain a link to this file.
file.outlinks	A list of all outgoing links from this file, meaning all links the file contains.
file.aliases	A list of all aliases for the note as defined via the YAML frontmatter.
file.tasks	A list of all tasks (I.e., |[ ] some task) in this file.
file.lists	A list of all list elements in the file (including tasks); these elements are effectively tasks and can be rendered in task views.
file.frontmatter	Contains the raw values of all frontmatter in form of key |value text values; mainly useful for checking raw frontmatter values or for dynamically listing frontmatter keys.
file.day	Only available if the file has a date inside its file name (of form yyyy-mm-dd or yyyymmdd), or has a Date field/inline field.
file.starred	if this file has been starred via the Obsidian Core Plugin “Starred Files”.


## Exempel

Exempel - Skapar lista över alla filer i ditt valv
~~~ Dataview
``` Dataview
LIST
```
~~~

## Syntax

~~~ Dataview
``` Dataview
FORMAT
[FROM "mapp/fil"|#etikett] [AND ""|#] 
```
~~~


## Beskrivning

### Sammanfattning

### Fördjupning

#### Format

Det finns fyra format:

- CALENDAR
- LIST
- TASK
- TABLE

#### Referenser
- [Dataview Beginners guide](https://obsidian.rocks/dataview-in-obsidian-a-beginners-guide/)
