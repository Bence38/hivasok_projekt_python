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

