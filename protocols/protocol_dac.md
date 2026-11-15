data/hull/rand1k.txt: 0.0049932003021240234 s
data/hull/rand2k.txt: 0.010002851486206055 s
data/hull/rand4k.txt: 0.019047975540161133 s
data/hull/rand8k.txt: 0.03972792625427246 s
data/hull/rand16k.txt: 0.07810235023498535 s
data/hull/rand32k.txt: 0.15674090385437012 s
data/hull/rand64k.txt: 0.31798386573791504 s
data/large/rand128k.txt: 0.6705939769744873 s
data/large/rand256k.txt: 1.3410961627960205 s
data/large/rand512k.txt: 2.7759690284729004 s
data/large/rand1M.txt: 5.686198949813843 s
data/hull/circle2k.txt: 0.01551198959350586 s
data/hull/circle4k.txt: 0.033208370208740234 s
data/hull/circle8k.txt: 0.07137274742126465 s
data/hull/circle16k.txt: 0.15398097038269043 s
data/hull/circle32k.txt: 0.33299899101257324 s
data/hull/circle64k.txt: 0.7193503379821777 s
data/large/circle128k.txt: 1.8027763366699219 s
data/large/circle256k.txt: 3.9419424533843994 s
data/large/circle512k.txt: 9.002359390258789 s
data/large/circle1M.txt: 19.088356971740723 s

Conclusion:
Random Punkte bilden den Average Case mit O(n log n).
Während im Kreis angeordnete Punkte theoretisch auch O(n log n) haben.
Die Schranke ist dieselbe, weil Sortieren und das Zusammenfügen über log n Ebenen in beiden Fällen O(n log n) bleiben. Auf dem Kreis liegt aber jeder Punkt auf der Hülle, deshalb müssen Tangentensuche und Merge die ganzen Ketten ablaufen, und die gemessene Zeit ist etwa dreimal so hoch.