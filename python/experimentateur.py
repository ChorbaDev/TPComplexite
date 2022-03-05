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
        left[i] = arr[left_index + i]
    for j in range(0, n2):
        right[j] = arr[middle_index + 1 + j]

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
    res = [i for i in range(0, xp.m - xp.p)]
    return res, cpt_op


def marqueurs_negatifs2(xp: Experience, cpt_op: int) -> [list, int]:
    """
    Fonction a completer - Stratégie 2
    Le second argument servira à compter le nombre d'utilisations de l'opérateur OP
    :param xp:
    :param cpt_op:
    :return:
    """
    cpt_op = 0
    res = [i for i in range(0, xp.m - xp.p)]
    return res, cpt_op


def marqueurs_negatifs3(xp: Experience, cpt_op: int) -> [list, int]:
    """
    Fonction a completer - Stratégie 1
    Le second argument servira à compter le nombre d'utilisations de l'opérateur OP
    :param xp:
    :param cpt_op:
    :return:
    """
    cpt_op = 0
    res = [i for i in range(0, xp.m - xp.p)]
    return res, cpt_op


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

    print("Stratégie 2\n")
    marqueurs_negatifs, cpt = marqueurs_negatifs2(xp, cpt)
    print("Marqueurs négatifs :\n")
    affiche(marqueurs_negatifs)
    print("Stratégie 2 / Nombres d'opérations : " + str(cpt) + "\n\n")

    print("Stratégie 3\n")
    marqueurs_negatifs, cpt = marqueurs_negatifs3(xp, cpt)
    print("Marqueurs négatifs :\n")
    affiche(marqueurs_negatifs)
    print("Stratégie 3 / Nombres d'opérations : " + str(cpt) + "\n\n")
