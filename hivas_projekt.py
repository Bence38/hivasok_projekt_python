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
ido = ido.strip().split(' ')
mp = mpbe(ido[0], ido[1], ido[2])
i = 0
while i < len(hivasok) and not mpbe(hivasok[i][0],hivasok[i][1],hivasok[i][2]) <= mp and mp < mpbe(hivasok[i][3],hivasok[i][4],hivasok[i][5]):
    i += 1
if i < len(hivasok):
    ugyfel = i + 1
else:
    ugyfel = 0
if (ugyfel):
    v_szama = -1
    for hivas1 in hivasok:
        if mpbe(hivasok[i][0],hivasok[i][1],hivasok[i][2])<= mp and mp <mpbe(hivasok[i][3],hivasok[i][4],hivasok[i][5]):    
            v_szama += 1
    print(f'A várakozók száma {v_szama} a beszélő {ugyfel} a hívó.')
else : 
    print('Nem volt beszélő')
print('6.feladat')
u_hivas = 0
ue_hivas = 0
muszak_vege = mpbe(12, 0, 0)
i = 0
for hivas1 in hivasok:
    kezdete = mpbe(hivas1[0], hivas1[1], hivas1[2])
    vege =mpbe(hivas1[3], hivas1[4], hivas1[5])
    if kezdete <= muszak_vege and vege >mpbe(hivasok[u_hivas][3],hivasok[u_hivas][4],hivasok[u_hivas][5]):
        ue_hivas = u_hivas
        u_hivas = i
    i += 1
ue_hivasvege = mpbe(hivasok[ue_hivas][3],hivasok[ue_hivas][4],hivasok[ue_hivas][5])
ue_hivaskezdete= mpbe(hivasok[u_hivas][0],hivasok[u_hivas][1],hivasok[u_hivas][2])
varakozas = ue_hivasvege - ue_hivaskezdete
if varakozas < 0:
    varakozas = 0
print(f'Az utolsó telefonáló adatai a(z){u_hivas + 1}sorban vannak, {varakozas} masodpercig tart.')

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
print(bekapcsolt)
