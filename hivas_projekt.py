def mpbe(o, p, mp):
    return o * 60 * 60 + p * 60 + mp
hivasok = []
stat = {}
f = open('hivas.txt','rt', encoding="utf-8")
for sor in f :
    sor = sor.strip().split(" ")
    sor.append(mpbe(sor[0], sor[1], sor[2]))
    sor.append(mpbe(sor[3], sor[4], sor[5]))
    hivasok.append(sor)
    #print(sor)

print('3.feladat')
for egyhivas in hivasok:
    if  egyhivas[0] in stat.keys():
        stat[egyhivas[0]] += 1 
    else:
        stat[egyhivas[0]] = 1
for k, v in stat.items():
    print(f'{k} óra {v} hívás')

print('4.feladat')
maxhivas = 0
maxhivassorszam = 0
hivassorszam = 1
for egyhivas in hivasok:
    hivashossz = mpbe(egyhivas[0], egyhivas[1], egyhivas[2]) + mpbe(egyhivas[3], egyhivas[4], egyhivas[5])
    if str(maxhivas) < hivashossz:
        maxhivas = hivashossz
        maxhivassorszam = hivassorszam
    hivassorszam += 1
print(f'A leghosszabb ideig vonalban lévő {maxhivassorszam} ,sorban szerepel,a hívás hossza:{maxhivas} \n másodperc')

print('5.feladat')
ido = input('Adjon meg egy időpontot(óra perc másodperc):')
ido = list(map(int,ido.strip().split(" ")))
Idomp = mpbe(ido[0], ido[1], ido[2])

i = 0
while i < len(hivasok) and not (mpbe(hivasok[i][0],hivasok[i][1],hivasok[i][2]) <= Idomp and Idomp < mpbe(hivasok[i][3],hivasok[i][4],hivasok[i][5])):
    i += 1
if i < len(hivasok):
    ugyfel = i + 1
else:
    ugyfel = 0
if (ugyfel):
    varakozok = -1
    for hivas1 in hivasok:
        if mpbe(hivasok[i][0],hivasok[i][1],hivasok[i][2])<= Idomp and Idomp < mpbe(hivasok[i][3],hivasok[i][4],hivasok[i][5]):    
            varakozok += 1
    print(f'A várakozók száma {varakozok} a beszélő {ugyfel} a hívó.')
else : 
    print('Nem volt beszélő')
print('6.feladat')
uH = 0
uEH = 0
muszakVege = mpbe(12, 0, 0)
i = 0
for egyhivas in hivasok:
    kezdete = mpbe(egyhivas[0], egyhivas[1], egyhivas[2])
    vege =mpbe(egyhivas[3], egyhivas[4], egyhivas[5])
    if kezdete <= muszakVege and vege > mpbe(hivasok[uH][3],hivasok[uH][4],hivasok[uH][5]):
        uEH = uH
        uEH = i
    i += 1
uehvege = mpbe(hivasok[uEH][3],hivasok[uEH][4],hivasok[uEH][5])
uehkezdete= mpbe(hivasok[uH][0],hivasok[uH][1],hivasok[uH][2])
varakozas = uehvege - uehkezdete
if varakozas < 0:
    varakozas = 0
print(f'Az utolsó telefonáló adatai a(z){uH + 1}sorban vannak, {varakozas} masodpercig tart.')

print('7.feladat')
bekapcsolt = []
elotte = 0
muszak_kezdete = mpbe(8,0,0)
i = 0
for hivas1 in hivasok:
    if muszak_kezdete < hivas1[7] and hivasok[elotte][7] < hivas1[7] and hivas1[6] <= muszak_vege:
        bekapcsolt.append(i)
        elotte = i
    i += 1
#print(bekapcsolt)
#siker = open('sikeres.txt', 'wt' enconding='utf-8')
#if hivasok[bekapcsolt[0]][6]< muszak_kezdete:
   # kezdet ='08 00 00'
#else:
    #kezdet = str(hivasok[bekapcsolt[0]][0])+" "+str(hivasok[bekapcsolt[0]][1])+" "  +str(hivasok[bekapcsolt[0]][2])