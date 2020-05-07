ListesEleves=[["Adem","Othman","Jean"],["Baptiste","Jb","Jean","Adem"],["Alex","Gibaud","pzlce","Kevin"],["Gibaud","JeanBaptiste","Alex","Nouredaine","Jb"],["Gibaud","Baptiste"],["Othman","Adem","Noureddine"],["Noureddine","Jb","Baptiste","Jean"]]

TousLesEleves=["Othman","Aya","Mehdi","Nour","Adem","Yanis","Alex","Noureddine","Alexandre","Aminata","Clément","Dayna","Fatima","Ismaël","Jeras","Kevindra","Nolan","Ruben","Rémi","Sidy","Tom","Walid","Yassine","Youcef","Younes","Younouss Soussi"]


"""Cette fonction peut être utilisée à la place de ListesEleves dans for j in ListeEleves à la ligne 33 . Faudra faire un truc comme ListeTous=Random(), puis templacer la ligne 33 par for j in ListeTous, à ce moment, il faudra aussi remplacer ListeBase= Algo() l.30 par ListeBase= TousLesEleves
"""

def Random():
    Eleves=["Othman","Aya","Mehdi","Nour","Adem","Yanis","Alex","Noureddine","Alexandre","Aminata","Clément","Dayna","Fatima","Ismaël","Jeras","Kevindra","Nolan","Ruben","Rémi","Sidy","Tom","Walid","Yassine","Youcef","Younes","Younouss Soussi"]
    L=[]
    for i in range(rd.randint(5,30)):
        k=rd.randint(1,len(Eleves)-1)
        L.append( [0,]*k)
    for j in range (len(L)):
        for l in range (len(L[j])):
            a=rd.randint(0,len(Eleves)-1)
            L[j][l]=Eleves[a]
            if Eleves[a] in L[j]:
                while L[j].count(Eleves[a])>1:
                    a=rd.randint(0,len(Eleves)-1)
                    L[j][l]=Eleves[a]
    return L

def Algo():
    L=[]
    for item in ListesEleves:
        for nom in item:
            if nom not in L:
                L.append(nom)
    return L


def Determine():
    Dico={}
    ListeBase = TousLesEleves
    ListeTous=Random()
    for i in ListeBase:
        b=0
        for j in ListeTous:
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