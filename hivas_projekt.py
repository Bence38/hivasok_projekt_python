def mpbe(o, p, mp):
    return o * 60 * 60 + p * 60 + mp
hivasok = []
f = open('hivas.txt','rt', encoding="utf-8")
for sor in f :
    sor = sor.strip().split(" ")
    print(sor)

