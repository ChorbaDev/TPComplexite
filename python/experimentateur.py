import random


def echange(a: int, b: int) -> [int, int]:
    """Fonction pour échanger deux entiers"""
    temp = a
    a = b
    b = temp
    return a, b


def affiche(table: list) -> None:
    """Fonction qui affiche un tableau"""
    print(table)
    print("\n")


class Experience:
    def __init__(self, m: int, p: int) -> None:
        """
        Fonction qui cree une expérience et la stocke dans la structure passée en paramètre
        Attention : il faut que p ≤ m
        :param m: Nombre de marqueurs
        :type m: int
        :param p: Nombre de marqueurs positifs
        :type p: int
        marqueurs: Tous les marqueurs
        marqueurs_positifs: Les marqueurs positifs
        """
        self.m = m

        self.marqueurs = [i for i in range(0, m)]
        # random.shuffle uses fisher-yates algorithm
        random.shuffle(self.marqueurs)

        tmp = [i for i in range(0, m)]
        self.p = p
        self.marqueurs_positifs = []
        for i in range(0, p):
            j = random.randint(0, m - i)
            self.marqueurs_positifs.insert(i, self.marqueurs[tmp[j]])
            tmp[j] = tmp[m - i - 1]

    def free_xp(self):
        self.marqueurs.clear()
        self.marqueurs_positifs.clear()


def merge(arr: list, left_index: int, middle_index: int, right_index: int) -> None:
    """
    Algorithme de tri fusion
    Merges two subarrays of arr[].
    First subarray is arr[l..m]
    Second subarray is arr[m+1..r]
    :param arr:
    :param left_index:
    :param middle_index:
    :param right_index:
    :return:
    """
    n1 = middle_index - left_index + 1
    n2 = right_index - middle_index
    left, right = [], []
    for i in range(0, n1):
        left.insert(i, arr[left_index + i])
    for j in range(0, n2):
        right.insert(j, arr[middle_index + 1 + j])

    i, j, k = 0, 0, left_index
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr: list, left_index: int, right_index: int) -> None:
    """
    l is for left index and r is right index of the sub-array of arr to be sorted
    :param arr:
    :param left_index:
    :param right_index:
    :return:
    """
    if left_index < right_index:
        m = left_index + (right_index - left_index) // 2

        merge_sort(arr, left_index, m)
        merge_sort(arr, m + 1, right_index)

        merge(arr, left_index, m, right_index)


def marqueurs_negatifs1(xp: Experience, cpt_op: int) -> [list, int]:
    """
    Fonction a completer - Stratégie 1
    Le second argument servira à compter le nombre d'utilisations de l'opérateur OP
    :param xp:
    :param cpt_op:
    :return:
    """
    cpt_op = 0
    res = []
    for i in range(0, xp.m):
        found, cpt_op = rech_seq(xp, xp.marqueurs[i], cpt_op)
        if not found:
            res.append(xp.marqueurs[i])
    return res, cpt_op


def rech_seq(xp, marqueur_rech, op):
    for i in range(0, xp.p):
        op += 1
        if xp.marqueurs_positifs[i] == marqueur_rech:
            return True, op
    return False, op


def marqueurs_negatifs2(xp: Experience, cpt_op: int) -> [list, int]:
    """
    Fonction a completer - Stratégie 2
    Le second argument servira à compter le nombre d'utilisations de l'opérateur OP
    :param xp:
    :param cpt_op:
    :return:
    """
    cpt_op = 0
    nn = xp.m - xp.p
    res = []
    merge_sort(xp.marqueurs_positifs, 0, xp.p - 1)
    j = -1
    for i in range(0, xp.m):
        trouver, tmpop = rechercher_dico(xp.marqueurs_positifs, xp.p, xp.marqueurs[i], cpt_op)
        cpt_op = tmpop + 1
        if not trouver:
            j += 1
            res.insert(j, xp.marqueurs[i])
        if j == nn + 1:
            break

    return res, cpt_op


def rechercher_dico(table: list, n: int, elt: int, op: int):
    bas, haut = 0, n - 1
    condition = True
    while condition:
        op += 1
        milieu = (bas + haut) // 2
        if elt == table[milieu]:
            return True, op
        elif table[milieu] < elt:
            bas = milieu + 1
        else:
            haut = milieu - 1
        if not bas <= haut:
            break
    return False, op


def marqueurs_negatifs3(xp: Experience, cpt_op: int) -> [list, int]:
    """
    Fonction a completer - Stratégie 1
    Le second argument servira à compter le nombre d'utilisations de l'opérateur OP
    :param xp:
    :param cpt_op:
    :return:
    """
    cpt_op = 0
    nn = xp.m - xp.p
    res = []
    merge_sort(xp.marqueurs, 0, xp.p - 1)
    merge_sort(xp.marqueurs_positifs, 0, xp.p - 1)
    debut, iden, pos = 0, 1, 0
    for p in range(0, xp.p):
        cpt_op += 1
        pos = position(xp.marqueurs, xp.m, xp.marqueurs_positifs[p])
        for i in range(debut, pos):
            cpt_op += 1
            iden += 1
            res.insert(iden, xp.marqueurs[i])
        debut = pos + 1
        if iden == nn + 1:
            break
    if pos < xp.m - 1:
        for i in range(pos + 1, xp.m):
            cpt_op += 1
            iden += 1
            res.insert(iden, xp.marqueurs[i])
    return res, cpt_op


def position(table: list, n: int, elt: int):
    for j in range(0, n):
        if table[j] == elt:
            return j
    return -1


def test(p: int, m: int) -> None:
    xp = Experience(m, p)
    cpt = 0

    print("Marqueurs :\n")
    affiche(xp.marqueurs)
    print("Marqueurs positifs :\n")
    affiche(xp.marqueurs_positifs)

    print("Stratégie 1\n")
    marqueurs_negatifs, cpt = marqueurs_negatifs1(xp, cpt)
    print("Marqueurs négatifs :\n")
    affiche(marqueurs_negatifs)
    print("Stratégie 1 / Nombres d'opérations : " + str(cpt) + "\n\n")
    marqueurs_negatifs.clear()

    print("Stratégie 2\n")
    marqueurs_negatifs, cpt = marqueurs_negatifs2(xp, cpt)
    print("Marqueurs négatifs :\n")
    affiche(marqueurs_negatifs)
    print("Stratégie 2 / Nombres d'opérations : " + str(cpt) + "\n\n")
    marqueurs_negatifs.clear()

    print("Stratégie 3\n")
    marqueurs_negatifs, cpt = marqueurs_negatifs3(xp, cpt)
    print("Marqueurs négatifs :\n")
    affiche(marqueurs_negatifs)
    print("Stratégie 3 / Nombres d'opérations : " + str(cpt) + "\n\n")
    marqueurs_negatifs.clear()
