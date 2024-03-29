# Instructions

* Installez Python (version >= 3.11.5)
* Clonez ce repo dans un répertoire local
* Exécutez les programme **bruteforce.py** ou **optimized.py** avec la commande `py bruteforce.py <dataset>` ou `py optimized.py <dataset>`, où `<dataset>` doit être le nom d'un des trois fichiers csv qui contiennent des portefeuilles d'actions.
* **Attention !** Le programme **bruteforce.py** ne peut fonctionner qu'avec le dataset 0.

# Contexte

Ces deux scripts permettent de trouver la meilleure combinaison d'actions dans un portefeuille, étant donné que chaque action a un coût et un profit (un pourcentage de son coût) et que l'on dispose d'un budget limité (500€ par défaut).

# Présentation des méthodes de résolution du problème
Le programme **bruteforce.py** utilise la fonction *combinations* de la librairie *itertools* pour tester toutes les combinaisons possibles. Sa complexité est de **O(2^N)** où N est le nombre d'actions, ce qui est très inefficace et explique pourquoi le programme ne peut fonctionner avec les datasets de plus de 20 actions.   
Le programme **optimized.py** utilise la *programmation dynamique* pour résoudre le problème. Il construit une matrice de N par M où N est le nombre d'actions et M le budget. Le programme parcourt chaque cellule et y résout un sous-problème du problème final (c-à-d avec moins d'actions et/ou moins de budget). La dernière cellule donne le profit maximal. Sa complexité est **O(N*M)**, ce qui est beaucoup plus efficace que l'autre programme et permet de résoudre des problèmes à plusieurs centaines d'actions en quelques secondes.

# Résultat attendu des programmes
Chacun de ces programmes fournit en sortie:
1. La meilleure combinaison d'actions
2. Le profit qu'elle génère
3. Son coût total
4. Le temps de calcul de la solution