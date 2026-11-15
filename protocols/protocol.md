# Testprotokoll: Andrew vs. Divide & Conquer

Beide Algorithmen liegen in O(n log n). Andrew ist bei zufälligen Punkten etwa 3-mal, bei Punkten auf einem Kreis etwa 9-mal schneller.

**Messung:** i7-10700K, Python 3.10, `time.perf_counter()`, Median aus 5 Läufen (ab 512k: 3). Das Einlesen der Datei ist nicht mitgemessen.

**Testdaten:** `rand` = zufällig im Quadrat, nur wenige Punkte auf der Hülle (12 bis 32). `circle` = alle Punkte auf einem Kreis, fast alle auf der Hülle.

## Laufzeiten

| n | Andrew rand | D&C rand | Andrew circle | D&C circle |
| ---: | ---: | ---: | ---: | ---: |
| 1k | 1,4 ms | 6,1 ms | 1,9 ms | 11,4 ms |
| 2k | 2,8 ms | 11,4 ms | 2,4 ms | 20,1 ms |
| 4k | 6,2 ms | 24,4 ms | 4,8 ms | 43,2 ms |
| 8k | 12,1 ms | 46,6 ms | 10,9 ms | 94,4 ms |
| 16k | 24,5 ms | 96,4 ms | 22,5 ms | 201,8 ms |
| 32k | 53,4 ms | 196,8 ms | 51,8 ms | 451,6 ms |
| 64k | 117,4 ms | 401,3 ms | 106,6 ms | 1,04 s |
| 128k | 274,6 ms | 830,7 ms | 257,6 ms | 2,35 s |
| 256k | 588,9 ms | 1,72 s | 594,8 ms | 5,04 s |
| 512k | 1,30 s | 3,55 s | 1,22 s | 11,12 s |
| 1M | 2,70 s | 7,17 s | 2,64 s | 24,28 s |

## Big O

| | Andrew | Divide & Conquer |
| --- | --- | --- |
| Sortieren | O(n log n) | O(n log n) |
| Hauptteil | O(n): jeder Punkt wird pro Kette höchstens einmal angehängt und einmal entfernt | T(n) = 2·T(n/2) + O(n) = O(n log n): log n Ebenen, Zusammenfügen O(n) pro Ebene |
| Best Case | Θ(n log n) | Θ(n log n), wenige Hüllenpunkte (`rand`) |
| Worst Case | Θ(n log n) | Θ(n log n), alle Punkte auf der Hülle (`circle`) |
| Abhängig von der Lage der Punkte | nein | nur im konstanten Faktor |

## Theorie gegen Messung

Bei doppeltem n erwartet man für O(n log n) einen Faktor von etwa 2,1, für O(n²) einen Faktor von 4. Gemessen wurden ab 4k Punkten Faktoren zwischen 1,9 und 2,4, für beide Algorithmen und beide Testfälle. (Bei 1k und 2k dauert eine Messung nur wenige Millisekunden, dort schwanken die Werte stärker.) Die Messung bestätigt also O(n log n), kein Algorithmus wächst quadratisch.

## Warum ist Divide & Conquer langsamer?

Die O-Notation ignoriert konstante Faktoren. D&C macht pro Punkt mehr Arbeit: Rekursion, Kopieren der Teillisten, Tangentensuche und Entfernen kollinearer Punkte nach jedem Zusammenfügen. Liegen alle Punkte auf der Hülle (`circle`), muss jedes Zusammenfügen die vollständigen Teilhüllen ablaufen. Darum braucht D&C dort 3,4-mal so lange wie bei `rand` (1M: 24,3 s gegenüber 7,2 s). Andrew ist davon unabhängig (2,6 s gegenüber 2,7 s), bei ihm entfällt etwa die Hälfte der Zeit auf das Sortieren.
