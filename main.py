from random import *

# definition des matrices utilisées par le DES
L = [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0,
     1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0]
M = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0,
     0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0,
     1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
cle = [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0,
       1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
print(len(cle))
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32,
      24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47,
      39, 31, 23, 15, 7]

E = [3, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4,
     25]
IP1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53,
       21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1,
       41, 9, 49, 17, 57, 25]

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63,
       55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 31, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

Sbox1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 00, 7],
         [00, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
s_boxes = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ],
]


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" traitement sur le message""""""""""""""""""""""""""""""""""""""""""

# fonction de traitement
def Permutation(listdef, listt):
    matrix = []
    for i in listdef:
        matrix.append(listt[i - 1])

    return matrix


# Fonction pour diviser le message en 2: R0 et L0
def divisionMatrix(listk):
    L0 = []
    R0 = []
    for i in range(0, 32):
        R0.append(listk[i])
    for i in range(32, 64):
        L0.append(listk[i])

    return R0, L0


# Traiment de R0 en appliquant la matrice E
def TraitementE(E, R0):
    resE = []
    for i in E:
        resE.append(R0[i - 1])
    return resE


# """"""""""""""""""""""""""""""""""""""" Traitement a realiser sur la cle""""""""""""""""""""""""""""""""""""""""""""""#
# declaration des données



# fonction utilisées
# fonction de Permutation
def Permutationcle(pc, cle):
    matrix1 = []
    for i in pc:
        matrix1.append(cle[i - 1])
    return matrix1


# Fonction pour diviser la cle en C0 et D0
def Divisioncle(clek):
    C0 = []
    D0 = []
    for i in range(0, 28):
        C0.append(clek[i])
    for i in range(28, 56):
        D0.append(clek[i])

    return C0, D0


# fonction decalage qui sera appelée dans la fonction DecalageDecle(co,do)
def decalage(L, type):
    K = []
    if type == '1':
        for i in range(1, len(L)):
            K.append(L[i])

        K.append(L[0])
        return K
    elif type == '2':
        for i in range(2, len(L)):
            K.append(L[i])
        K.append(L[0])
        K.append(L[1])
    return K


# Decalage a realiser sur C0 et D0
def DecalageDecle(co, do, numKl):
    decal1 = [1, 2, 9, 16]
    decal2 = [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]
    if numKl in decal1:
        type = '1'
    elif numKl in decal2:
        type = '2'
    C1 = decalage(co, type)
    D1 = decalage(do, type)
    return C1, D1


# fonction pour concatener les 2 cle apres decalage
def Concatenation(l1: list, l2: list):
    return l1 + l2


# fonction pour appliquer la matrice pc2 a la nouvelle cle obtenue apres concatenantion

def PC2Liste(list, pc2):
    rePc2 = []
    for i in pc2:
        rePc2.append(list[i - 1])
    return rePc2


# traitement a realiser apres l'obtention de la cle et du ro
"""fonction XOR"""


def FonctionXOR(ER, K):
    XOR = []
    i = 0
    if len(ER) != len(K):
        print("Erreur")
    else:
        while i < len(K):
            if ER[i] == K[i]:
                XOR.append(0)
            else:
                XOR.append(1)
            i += 1
    return XOR


# Fonction permettant de trouver la ligne et colonne qu'on va utiliser dans le sBoxes
def fonctionCalcul(listxor):
    listL = []
    listC = []
    i = 0
    k = 0
    while k < 8:
        # print(k) pour calculer le valeur decimal des elements en position 1 et 6 element en decimal et l'ajouter a
        # la liste ligne
        v = listxor[i]
        z = listxor[i + 5]
        l = 2 * v + 1 * z
        listL.append(l)
        # pour calculer la valeur decimale des elements en position  2,3,4,5 element en decimal et l'ajouter a la liste Colonne
        w = listxor[i + 1]
        x = listxor[i + 2]
        y = listxor[i + 3]
        s = listxor[i + 4]
        c = w * 8 + x * 4 + y * 2 + s * 1
        listC.append(c)
        i = i + 5 + 1
        k += 1

    return listC, listL


# application du Sboxe1 sur les valeurs obtenues
def SBoxe(Sbox1, LC, LL):
    Sbox = []
    for i in range(0, len(LC)):
        c = LC[i]
        l = LL[i]
        print
        resB = Sbox1[l][c]
        Sbox.append(resB)
    return Sbox


def SBoxet(S_box, ligne, colonne):
    Sbox = []
    resB = S_box[ligne][colonne]
    # Sbox.append(resB)
    return resB


# fonction pour faire les transformation decimale binaire
def transformationBinaire(nombre):
    return bin(nombre)


# fonction pour passer de 48 bit a  32
def transde4832bit(listsboxe):
    restrans = []
    list1 = []
    # pour tous les resultat retourne par le sboxe
    for i in range(0, len(listsboxe)):
        x = listsboxe[i]
        z = transformationBinaire(x)

        # dans le cas ou la taille du resultat est different de 6 et le cas ou il est egal a 6:
        if len(z) != 6:
            k = 6 - len(z)
            for i in range(0, k):
                list1.append('0')
            for char in z:
                list1.append(char)
        else:
            for char in z:
                list1.append(char)

        # prendre les  4 derniers de la liste traitement a faire si le resultat ne contient pas des 0 et  1 :
        for i in range(2, len(list1)):
            if list1[i] != '0' and list1[i] != '1':
                restrans.append(0)
            else:
                restrans.append(int(list1[i]))

        list1 = []

    return restrans


# print(f"resultat de 48-32 :{transde4832bit(listsboxe)}")
# appplication de la matrice P

def applicationP(P, restrans):
    resp = []
    for i in P:
        resp.append(restrans[i - 1])
    return resp


def ApplicationIP1(IP1, resC):
    resIP1 = []
    for i in IP1:
        resIP1.append(resC[i - 1])
    return resIP1


def fonctionDes16(cle, message):
    M1 = Permutationcle(PC1, cle)
    C, D = Divisioncle(M1)
    respm = Permutation(IP, message)
    L, R = divisionMatrix(respm)

    for f in range(1, 17):
        print(f"-------Iteration {f}-----------")
        print(f"le {f}em R :{R}")
        print(f"le {f}em L :{L}")

        # trouvons la cle correspondante de l iteration

        Ci, Di = DecalageDecle(C, D, f)
        C = Ci
        D = Di
        print(f"taille Ci:{len(Ci)} ,Ci:{Ci} ,")
        print(f"taille Di:{len(Di)} ,Di:{Di},")
        res = Concatenation(Ci, Di)

        K = PC2Liste(res, PC2)

        # trouvons le message :
        restE = TraitementE(E, R)


        rXOR = FonctionXOR(restE, K)
        colonne, ligne = fonctionCalcul(rXOR)

        # application des 8 sboxes
        listB = []
        for j in range(0, 8):
            resBoxe = SBoxet(s_boxes[j], ligne[j], colonne[j])
            listB.append(resBoxe)
        restran4832 = transde4832bit(listB)
        resaP = applicationP(P, restran4832)
        print(f" resap :{resaP}")
        print(L)
        Ri = FonctionXOR(resaP, L)
        print(Ri)

        Li = R
        R = Ri
        L = Li
        print(f"R de sorti:{R}")
        print(f"L de sortie:{L}")
    print("Fin des 16 iterations")
    conRiLi = Concatenation(Ri, Li)
    message = ApplicationIP1(IP1, conRiLi)
    return message


print(f"message chiffre:{fonctionDes16(cle, M)}")
