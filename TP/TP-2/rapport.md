# Travail pratique 2
## Analyse de differents containers

Voici les containers que nous allons analyser:

#### • binarytree
#### • deque
#### • fifo
#### • hashtable
#### • lifo
#### • linkedlist
#### • tree

## Résultats des tests

### Le binarytree

#### Avantages:

Pour ce qui est du binartTree, il permet de faire des recherches de façon très rapide. Surtout si il est balancé. Ce qui fait qu'il y a la meme quantité de recherche pour les deux cotés. Beaucoup plus vite qu'une recherche linaiaire comme dans un vector. Donc si le binaryTree a 5 niveaux donc une trentaine d'elements, il aura entre au plus 5 recherches pour trouver un nombre contrairement au vector dans lequel il faudrait iterer sur tous les elements pour avoir la meme quantité de recherche.

Tres performant dans les arbres decisionnels qui demande beaucoup de reponses oui/non. Comme dans le cas d'un jeu de damme ou le player doit choisir d'avancer a gauche ou droite avec un pion. Pour faire l'intelligence artificielle de ce jeu, le binaryTree est tres performant.

#### Inconvenients:

Les arbres binaires ne sont pas optimal pour les données qui changent très fréquemment comme le trading haute frequance qui consiste a ouvrir des positions et les fermer rapidement. Les arbres binaires sont generalemnt plus performant pour la recherche de données mais mois performant pour l,ajout et la suppression de donne surtout dans le cas d'un arbre balancé. Plus un arbre est gros, plus il est long de le balancer apres chaque ajout ou suppression de donne.

Il n'est pas aussi optimal pour les donnees qui doivent etre triées avec plusieurs critères. Prenons par exemple le cas d'une clinique medicale qui doit trier les patients selon plusieurs critères comme leur urgence, leur age, leur sexe, etc. Dans ce cas, on opterais plus pour un arbre multi-dimensionnel.


### Le deque

#### Avantages:

Il est tout indiqué pour un system de gestion de tache avec priorités car il permet l'insertion d'elements au debut ou a la fin. Prenons comme exemple un service de rendez-vous médical. On entre les rendez-vous a la fin de la pile mais pour une urgence, on peut ajouter le patient au debut de la liste avec un faible cout memoire.

Il est aussi exelent pour avoir une bidirectionnalité comme la navigation dans une application mobile pour naviguer facilement entre les pages.

#### Inconvenients:

N'est pas optimal pour les données qui nécéssite un tri fréquent. N'a pas d'algorithme de trie intégré comme dans un map. Exemple, garder des donnés trier en ordre chronologiques.

Ne gère pas les données avec relations complexes comme dans le cas d'une bases de données relationnelles qui fonctionnerait mieux avec un map pour garder la meme structure de donnée.


### Le fifo

#### Avantages:

Dans un container de type fifo, c'est le premier element qui est le premier a sortir. Il serait optimal de l'utiliser dans le cas d'une file d'attente. C'est comme aller a la SAAQ et prendre un ticket pour attendre son tour. Premier arriver, premier servi.

Peut etre tres utile dans un system de streaming. Permet d'avoir un buffer de donnee pour le traitement en continue pour difuser le contenue deja charger dans le buffer.

#### Inconvenients:

N'est pas optimal quand il sagit de traiter des priorites. Comme une Urgence dans un hopital pour gerer la priorite de traitement pour les nouveaux arrivants. Un deque serait plus approprie.

N'est pas non plus concu pour tout ce qui est de la gestion bidirectionnel comme pour la gestion de page web.


### Le hashtable

#### Avantages:

Permet de rechercher facilement un element par une cle. C'est a dire que meme si la value de la node<key, value>() contient beaucoup de donnee, si la cle est exemple un id "int", le hashtable va iterer sur la grandeur du int et non la grandeur de l'objet "value" contenue dans la node. Donc, tres rapide pour la recherche.

Serait tres optimal dans le cas d'un recencement de la population. node<int, class habitant>().

#### Inconvenients:

N'est pas optimal pour trier des objet exemple, par ordre de gandeur. Un arbre de recherche equilibre (red black tree) serait plus approprie.

Comme le binary tree, il n'est pas optimiser pour prendre des plages pour la recherche vue que les elements ne sont pas trie en ordre.


### Le tree

#### Avantages:

Il est tres couramment utiliser comme dans un system organisationnelle de donnees comme un arborescence de fichiers dans un projet. Permet d'avoir une structure avec une hierarchie plus naturelle que l'arbre balancé.

Les arbres sont aussi beaucoup utiliser dans l'industrie du jeu video comme dans l'algorithme Dijkstra qui utilise des arbres pour trouver le chemin le plus rapide entre 2 points. Exemple, trouver le chemin le plus rapide dans un labyrinthe.

#### Inconvenients:

Le tree est beaucoup moins optimal pour faire des recherches par plages. Comme le tree a beaucoup de ramifications, il peut etre couteux en mémoire. Comme dans le cas ou on aurait 2 nombres a chercher. Un serait tout au bout a gauche et l'autre tout au bout a droite. Il faudrait parcourrir toute l'arbre pour trouver ces 2 nombres.

Ils ne sont pas concus pour les acces aleatoires frequants. Comme les nodes sont a des addresse differents dans la memoire contrairement a un tableau avec des adresses une a la suite de l'autre. (La on entre dans la notion de pointeurs que je vois beaucoup quand je fais du c ou c++).


Voici le projet "[Container](https://github.com/dracken24/container/tree/main/includes/templates)" que j'ai eu a coder a 42Quebec. Il fallait coder en c++ un map, un vector et un stack en class template avec leurs iterators et avec std::allocator.
