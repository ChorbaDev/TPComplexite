#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "experimentateur.h"
#include <stdbool.h>

int rechercheDicho(int *pInt, int p, int i, int *pInt1);

int position(int *pInt, int m, int i);

// Fonction pour echanger deux entiers
void echange(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Fonction qui affiche un tableau de taille n
void affiche(int *t, int n) {
    int i;

    for (i = 0; i < n; ++i)
        printf("%d ", t[i]);
    printf("\n");
}

// Fonction qui cree une expérience et la stocke dans la structure passee en parametre
// Attention : il faut que p <= m
void cree_experience(EXPERIENCE *xp, int p, int m) {
    int i, j;

    xp->m = m;

    xp->marqueurs = (int *) malloc(m * sizeof(int));
    for (i = 0; i < m; ++i)
        xp->marqueurs[i] = i;

    // On melange les marqueurs dans l'ensemble des marqueurs par l'algorithme de Fisher-Yates
    for (i = m - 1; i >= 0; --i) {
        j = rand() % (i + 1);
        echange(&xp->marqueurs[i], &xp->marqueurs[j]);
    }

    // On choisit p marqueurs parmi les m qui seront les marqueurs positifs
    int *tmp = (int *) malloc(m * sizeof(int));
    for (i = 0; i < m; ++i)
        tmp[i] = i;

    xp->p = p;

    xp->marqueurs_positifs = (int *) malloc(p * sizeof(int));
    for (int i = 0; i < p; ++i) {
        j = rand() % (m - i);
        xp->marqueurs_positifs[i] = xp->marqueurs[tmp[j]];
        tmp[j] = tmp[m - i - 1];
    }

    free(tmp);
}

// Algorithme de tri fusion
// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    /* create temp arrays */
    int L[n1], R[n2];

    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    /* Copy the remaining elements of L[], if there
     are any */
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    /* Copy the remaining elements of R[], if there
     are any */
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

/* l is for left index and r is right index of the
 sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int m = l + (r - l) / 2;

        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

// Fonction qui libere la memoire dans une experience
void libere_experience(EXPERIENCE *xp) {
    free(xp->marqueurs);
    free(xp->marqueurs_positifs);
}

// Fonction a completer - Strategie 1
// Le second argument servira a compter le nombre d'utilisation de l'opérateur OP
int *marqueurs_negatifs1(EXPERIENCE *xp, int *cptOP) {
    *cptOP = 0;

    int *res = (int *) malloc((xp->m - xp->p) * sizeof(int));

    return res;
}

// Fonction a completer - Strategie 2
// Le second argument servira a compter le nombre d'utilisation de l'opérateur OP
int *marqueurs_negatifs2(EXPERIENCE *xp, int *cptOP) {
    *cptOP = 0;
    int nn=(xp->m - xp->p);
    int *res = (int *) malloc(nn * sizeof(int));
    mergeSort(xp->marqueurs_positifs, 0, xp->p-1);
    int j=-1;
    for (int i = 0; i < xp->m; i++) {
        (*cptOP)++;
        int trouver=rechercheDicho(xp->marqueurs_positifs,xp->p,xp->marqueurs[i],cptOP);
        if(trouver==-1){
            j++;
            res[j]=xp->marqueurs[i];
        }
        if (j==nn+1) break;
    }
    return res;
}
int rechercheDicho(int *t, int n, int elt, int *op) {
    int bas=0,haut=n-1,milieu;
    //printf("->elt = %d \n",elt);
    do{
        (*op)++;
        milieu=(bas+haut)/2;
        //printf("milieu = %d \n",milieu);
        if (elt==t[milieu]) return milieu;
        else if (t[milieu]<elt) bas=milieu+1;
        else haut=milieu-1;
    }while (bas<=haut);
    return -1;
}
// Fonction a completer - Strategie 3
// Le second argument servira a compter le nombre d'utilisation de l'opérateur OP
int *marqueurs_negatifs3(EXPERIENCE *xp, int *cptOP) {
    *cptOP = 0;
    int nn=(xp->m - xp->p);
    int *res = (int *) malloc((xp->m - xp->p) * sizeof(int));
    mergeSort(xp->marqueurs, 0, xp->m-1);
    mergeSort(xp->marqueurs_positifs, 0, xp->p-1);
    int debut=0,iDeN=-1;
    int pos;
    for (int p = 0; p < xp->p; ++p) {
        (*cptOP)++;
        pos=position(xp->marqueurs,xp->m,xp->marqueurs_positifs[p]);
        for (int i = debut; i < pos; ++i) {
            (*cptOP)++;
            iDeN++;
            res[iDeN]=xp->marqueurs[i];
        }
        debut=pos+1;
        if (iDeN==nn+1) break;
    }
    if (pos<xp->m-1){
        for (int i = pos+1; i <xp->m ; ++i) {
            (*cptOP)++;
            iDeN++;
            res[iDeN]=xp->marqueurs[i];
        }
    }
    return res;
}

int position(int *t, int n, int elt) {
    for (int j = 0; j < n; ++j) {
        if (t[j]==elt) return j;
    }
    return -1;
}

void test(int p, int m) {
    EXPERIENCE xp;
    int cpt, *marqueurs_negatifs;

    // Creation de l'experience
    cree_experience(&xp, p, m);

    printf("Marqueurs :\n");
    affiche(xp.marqueurs, m);
    printf("\nMarqueurs positfis :\n");
    affiche(xp.marqueurs_positifs, p);

    //marqueurs_negatifs = marqueurs_negatifs1(&xp, &cpt);
    //marqueurs_negatifs = marqueurs_negatifs2(&xp, &cpt);
    marqueurs_negatifs = marqueurs_negatifs3(&xp, &cpt);

    printf("\nStrategie: \n");
    printf("Marqueurs negatifs :\n");
    affiche(marqueurs_negatifs, xp.m - xp.p);
    printf("Strategie / nombres OP : %d\n\n", cpt);
    free(marqueurs_negatifs);

    libere_experience(&xp);
}