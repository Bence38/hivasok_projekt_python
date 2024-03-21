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
print(stat)

