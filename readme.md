## Group
__TD 2__
- Alexandre Lascaux
- Alexandre Haas
- Antoine Maurel

## Sorts
### Bubble
Le "bubble sort" est un algorithme qui compare deux éléments consécutifs et les permutes si ils sont mal triés. Dans notre cas, pour chaque position du tableau on vérifie si l'élément suivant est plus petit que l'élément actuel et si c'est le cas nous les inversons.
### Selection
Le "selection sort" est un algorithme qui prend le plus petit élément et qui le positionne au début du tableau. Dans notre cas, pour chaque élément du tableau nous bouclons sur tout les autres éléments pour voir si notre élément est plus petit que les autres, si ce n'est pas le cas nous prenons le plus petit et nous venons inverser sa position avec l'élement courant et l'élément le plus petit.
### Insertion
Le "insertion sort" est un algorithme assez similaire au "bubble sort". Dans notre cas, on prend le deuxième élément du tableau, ensuite on regarde le premier, si le deuxième est inférieur au premier alors les deux sont permutés et la clef passe au troisième élément et ainsi de suite.
### Merge
Le "merge sort" est un algorithme qui divise à chaque fois en deux le tableau jusqu'à ce qu'il ne reste plus que des groupes contenant un seul élément, les éléments sont ensuite triés et rassemblés jusqu'à obtenir le tableau final trié. Dans notre cas, tant que le tableau de base contient plus de un élément on le divise en deux et redivise chaqu'un des sous tableaux obtenus par deux. Ensuite, on fusionne tout les sous tableaux en fesant un tri afin d'obtenir le tableau final trié.
### Quick
Le "quick sort" est un algorithme qui découpe le tableau en fonction d'un élément pivot. Dans notre cas, on prend le dernier élément du tableau qu'on appellera élément pivot, et pour chaque élément inférieur ou égal au pivot on le switch de place avec un élément supérieur au pivot et ainsi de suite.
### Shell
Le "shell sort" est un algorithme qui compare les éléments les plus éloignés les uns des autres jusqu'à arriver aux éléments les plus proches les uns des autres. Dans notre cas, on défini un interval qui est égale au nombre d'éléments dans le tableau divisé par deux et tant que cet interval est supérieur à 0 on boucle sur les éléments et on applique le même principe que pour le trie par insertion.
### Comb
Le "comb sort" est un algorithme assez similaire au "bubble sort" sauf que lui utilise un gap tout le temps supérieur à 1. Dans notre cas on prend le nombre total d'éléments puis on le divise par 1.3, et ce jusqu'à avoir un gap de 1.

