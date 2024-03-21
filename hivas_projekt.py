def mpbe(o, p, mp):
    return o * 60 * 60 + p * 60 + mp
hivasok = []
stat = {}
f = open('hivas.txt','rt', encoding="utf-8")
for sor in f :
    sor = sor.strip().split(" ")
    hivasok.append(sor)
    #print(sor)

print('3.feladat')
for hivas1 in hivasok:
    if  hivas1[0] in stat.keys():
        stat[hivas1[0]] += 1 
    else:
        stat[hivas1[0]] = 1
for k, v in stat.items():
    print(f'{k} óra {v} hívás')

print('4.feladat')
max = 0
m_sorszam = 0
h_sorszam = 0
for hivas1 in hivasok:
    h_hossz = mpbe(hivas1[0], hivas1[1], hivas1[2])+ mpbe(hivas1[3], hivas1[4], hivas1[5])
    if max < h_hossz:
        max = h_hossz
        m_sorszam = h_sorszam
    h_sorszam += 1
print(f'A leghosszabb ideig vonalban lévő {max} ,sorban szerepel,a hivas hossza:{h_hossz} masodperc')

print('5.feladat')
ido = input('Adjon meg egy időpontot(óra perc másodperc):')
ido = ido.strip().split(' ')
mp = mpbe(ido[0], ido[1], ido[2])
i = 0
while i < len(hivasok) and not mpbe(hivasok[i][0],hivasok[i][1],hivasok[i][2])<= mp and mp <mpbe(hivasok[i][3],hivasok[i][4],hivasok[i][5]):
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
