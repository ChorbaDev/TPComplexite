#ifndef TPCOMPLEXITE_EXPERIMENTATEUR_H
#define TPCOMPLEXITE_EXPERIMENTATEUR_H

// Fonction pour echanger deux entiers
void echange(int *a, int *b);
// Fonction qui affiche un tableau de taille n
void affiche(int *t, int n);

// Structure representant une experience
// Un marqueur est un entier compris entre 0 et m
typedef struct {
    int m; // Nombre de marqueurs
    int *marqueurs; // Tous les marqueurs

    int p; // Nombre de marqueurs positifs
    int *marqueurs_positifs; // Les marqueurs positifs
} EXPERIENCE;
// Fonction qui cree une expérience et la stocke dans la structure passee en parametre
// Attention : il faut que p <= m
void cree_experience(EXPERIENCE *xp, int p, int m);
// Algorithme de tri fusion
// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r);
/* l is for left index and r is right index of the
 sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r);
// Fonction qui libere la memoire dans une experience
void libere_experience(EXPERIENCE *xp);
// Fonction a completer - Strategie 1
// Le second argument servira a compter le nombre d'utilisation de l'opérateur OP
int *marqueurs_negatifs1(EXPERIENCE *xp, int *cptOP);
// Fonction a completer - Strategie 2
// Le second argument servira a compter le nombre d'utilisation de l'opérateur OP
int *marqueurs_negatifs2(EXPERIENCE *xp, int *cptOP);
// Fonction a completer - Strategie 3
// Le second argument servira a compter le nombre d'utilisation de l'opérateur OP
int *marqueurs_negatifs3(EXPERIENCE *xp, int *cptOP);
void test(int p, int m);
#endif //TPCOMPLEXITE_EXPERIMENTATEUR_H
