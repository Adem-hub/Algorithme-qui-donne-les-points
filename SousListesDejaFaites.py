ListesEleves=[["Adem","Othman","Jean"],["Baptiste","Jb","Jean","Adem"],["Alex","Gibaud","pzlce","Kevin"],["Gibaud","JeanBaptiste","Alex","Nouredaine","Jb"],["Gibaud","Baptiste"],["Othman","Adem","Noureddine"],["Noureddine","Jb","Baptiste","Jean"]]




def Algo():
    L=[]
    for item in ListesEleves:
        for nom in item:
            if nom not in L:
                L.append(nom)
    return L


def Determine():
    Dico={}
    ListeBase= Algo()
    for i in ListeBase:
        b=0
        for j in ListesEleves:
            for iti in j:
                if iti==i:
                    b+=100-(j.index(iti)*10)
        Dico[i]=round(b)

    for l in Dico:
        if Dico[l]==0:
            Dico.pop(l)
    return Dico

def Aide_Maj():
    Dico=Determine()
    a=0
    L=[]
    LL=[]
    Tri=[]
    for values in Dico.values():
        a+=values
    for index,i in enumerate(Dico):
        b= Dico[i]
        Pourcentage= (b*100)/a
        Pourcentage=round(Pourcentage,2)
        L.append((Pourcentage,index))
        Tri.append((Pourcentage,i))
    L=sorted(L)
    Tri=sorted(Tri)
    for item in range (len(Tri)):
        print("Dans la globalité de ton travail,",Tri[item][1],"t'as aidé(e) à:",Tri[item][0],"%")
    Aide= [index for Pourcentage,index in L[-1:]]
    for k in Aide:
        m=Dico.keys()
        m=list(m)
        LL.append(m[k])
    print()
    print("Celui qui t'as le plus aidé(e) est donc",LL[0])