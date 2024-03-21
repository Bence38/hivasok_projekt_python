def hiv(o,p,m):
    return o*60*60+p*60+m

hivasok = []
f = open("hivas.txt", "rt", encoding="utf-8")

for sor in f:
    sor = sor.strip().split(" ")
    sor = list(map(int, sor))
    sor.append(hiv(sor[0], sor[1], sor[2]))
    sor.append(hiv(sor[3], sor[4], sor[5]))
    hivasok.append(sor)

stat = {}

for hivas1 in hivasok:
    if hivas1[0] not in stat.keys():
        stat[hivas1[0]] = 0
    
for hivas1 in hivasok:
    stat[hivas1[0]] += 1

print("3. feladat")

for k, v in stat.items():
    print(f"{k} óra {v} hívás")

print("4. feladat")

maxH= 0
maxHS = 0
hivasS= 1

for hivas1 in hivasok:
    hivashossz = hiv(hivas1[3], hivas1[4], hivas1[5]) - hiv(hivas1[0], hivas1[1], hivas1[2])
    if maxH< hivashossz:
        maxH = hivashossz
        maxHS = hivasS
    hivasS += 1

print(f"A legtovább tartó hívás a {maxHS} sorban van, a hívás {maxH} másodperc hosszú volt.")

print("5. feladat")
idopont = input("Kérek egy időpontot!(óra, perc, másodperc)")
idopont = list(map(int, idopont.strip().split(" ")))
idomp= hiv(idopont[0], idopont[1], idopont[2])

i = 0

while i < len(hivasok) and not(hiv(hivasok[i][0], hivasok[i][1], hivasok[i][2]) <= idomp and idomp < hiv(hivasok[i][3], hivasok[i][4], hivasok[i][5])):
    i += 1

if i < len(hivasok):
    ugyfel = i + 1
else:
    ugyfel= 0

if ugyfel:
    varo = -1
    for hivas1 in hivasok:
        if hiv(hivas1[0], hivas1[1], hivas1[2]) <= idomp and idomp < hiv(hivas1[3], hivas1[4], hivas1[5]) :
            varo +=1
    print(f"A várakozók száma: {varo} a beszélő a {ugyfel}. hívó.")
else:
    print("Nem volt beszélő")

print("6. feladat")
utolsoh = 0
ueh = 0
muszakvege = hiv(12,0,0)
i = 0
for hivas1 in hivasok:
    kezdet = hiv(hivas1[0],hivas1[1],hivas1[2])
    veg = hiv(hivas1[3],hivas1[4],hivas1[5])
    if kezdet <= muszakvege and veg > hiv(hivasok[utolsoh][3],hivasok[utolsoh][4],hivasok[utolsoh][5]):
        ueh = utolsoh
        utolsoh = i
    i +=1

utolsoelottivege = hiv(hivasok[ueh][3],hivasok[ueh][4],hivasok[ueh][5])
utolsokezdet = hiv(hivasok[utolsoh][0],hivasok[utolsoh][1],hivasok[utolsoh][2])
varakozas = utolsoelottivege - utolsokezdet

if varo< 0:
    varo = 0
print(f"Az utolsó telefonáló adatai a(z) {utolsoh+1}. sorban vannak, {varo} másodpercig várt.")