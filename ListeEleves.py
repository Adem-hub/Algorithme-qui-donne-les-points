import random as rd

TousLesEleves=["Othman","Aya","Mehdi","Nour","Adem","Yanis","Alex","Noureddine","Alexandre","Aminata","Clément","Dayna","Fatima","Ismaël","Jeras","Kevindra","Nolan","Ruben","Rémi","Sidy","Tom","Walid","Yassine","Youcef","Younes","Younouss"]


def Random():
    L=[]
    for i in range(rd.randint(5,20)):
        k=rd.randint(1,len(TousLesEleves)-1)
        L.append( [0,]*k)
    for j in range (len(L)):
        for l in range (len(L[j])):
            a=rd.randint(0,len(TousLesEleves)-1)
            L[j][l]=TousLesEleves[a]
            if TousLesEleves[a] in L[j]:
                while L[j].count(TousLesEleves[a])>1:
                    a=rd.randint(0,len(TousLesEleves)-1)
                    L[j][l]=TousLesEleves[a]
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
                    b+=200-(j.index(iti)*10)
        Dico[i]=round(b)
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
        print("Dans la globalité de ton travail,",Tri[item][1],"t'as aidé à:",Tri[item][0],"%")
    Aide= [index for Pourcentage,index in L[-1:]]
    for k in Aide:
        m=Dico.keys()
        m=list(m)
        LL.append(m[k])
    print()
    print("Celui ou celle qui t'as le plus aidé est donc",LL[0])