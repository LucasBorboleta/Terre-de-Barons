# Retour sur les calamités

## Ressenti

Collecte de quelques impressions :

- C'est bien qu'après avoir joué pendant 1 heure et déjà bien bataillé, il y ait une fin de partie inéluctable.

- Un peu  de calamités est admissible.

- Mais c'est dommage que trop de calamités renverse la hiérarchie de la piste de score.

## Analyse de la mécanique actuelle

Analysons la mécanique actuelle :

* Il y a 37 tuiles au départ, mais après avoir enlever 4 montagnes, il reste 33 tuiles pouvant être occupées.
* En moyenne, 9.5 donjons sont construits dans une partie d'après les simulations Python. Mais, ici, on arrondira à 10 donjons.
* Focalisons-nous sur la calamité qui détruit les donjons (Courroux de la Terre).
* A 3 joueurs, si 3 cartes "Courroux de la Terre" sont tirées, ce sont 3x3 = 9 positions qui sont ciblées. C'est à dire 9 sur 33.
  * La probabilité qu'aucun donjon ne soit détruit est équivalent à la probabilité de choisir 9 fois une des (33 - 10 =) 23 tuiles parmi les 33.
    * Soit (23x22x21 x 20x19x18 X 17x16x15) / (33x32x31 x 30x29x28 x 27x26x25) = 2.1%
  * Donc à **3 joueur**s, la probabilité qu'au moins 1 donjon soit détruit est donc **97.9%** ; soit une très forte probabilité !
* A 2 joueurs, donc avec 2 cartes "Courroux de la Terre", ce sont 2x3 = 6 positions qui sont ciblées. C'est à dire 6 sur 33.
  * A **2 joueur**s, la probabilité qu'au moins 1 donjon soit détruit est donc **90.9%** ; soit une très forte probabilité !
* A 4 joueurs, donc avec 4 cartes "Courroux de la Terre", ce sont 4x3 = 12 positions qui sont ciblées. C'est à dire 12 sur 33.
  * A **4 joueur**s, la probabilité  qu'au moins 1 donjon soit détruit est donc **99.6%** ; soit une très forte probabilité !
* Globalement, avec la mécanique actuelle, la probabilité qu'au moins un donjon soit détruit est donc très élevée ; c'est quasiment certain!
* D'un autre côté pour que la menace soit crédible, il est cohérent d'avoir cette forte probabilité, au minimum de 90% (réalisée à 2 joueurs)
* Les calculs (cf. feuille Excel) montrent qu'à 2 joueurs, cette probabilité descend à 78% en tirant 2 cartes positions par événement, et à 52% en tirant juste une position par événement.
* **Conclusion** : afin de maintenir le niveau de menace assez élevé, tant en gardant des règles simples, gardons telle quelle cette mécanique des évènements calamiteux !

## Nouvel événement de fin de partie - La Diplomatie

Les événements calamiteux étant admis, comme faire en sorte de donner du temps aux joueurs pour s'en remettre. C'est à dire qu'il faut limiter le temps de jeu avec le second cycle des decks, mais ne pas terminer la partie abruptement sur des événements calamiteux qui, par exemple, inverse la hiérarchie des scores.

Voici une proposition :

* Dans le second cycle du deck, en plus des 3 calamités, chaque joueur insère un événement "**Messager pour la Paix**".
* L'événement Messager pour la Paix ne provoque aucun changement sur le plateau. Cet événement est juste gardé sur la table, face visible.
* Lorsque tous les joueurs ont révélé leurs Messager pour la Paix la partie s'arrête.
* Le joueur qui pioche le dernier Messager pour la Paix termine complètement son tour de jeu, puis la partie s'arrête et on procède à la détermination du vainqueur, comme d'habitude.
* Pour être complet, même si c'est improbable, convenons qu'un troisième cycle de deck est possible, et que dans ce cas, les cartes calamités sont à nouveau insérés dans le deck, mais pas la carte Messager pour la Paix.

Reste juste à trouver le nom et le design final pour cet événement "Messager pour la Paix".

## Thématisation

*  Carte "Héraut de Pourparlers"
* Fin par "Diplomatie"
* Zone du "Conseil des Hérauts"

Expressions :

* Il y a déjà deux Hérauts de Pourparlers au Conseil... si le troisième arrive, la Paix sera ratifiée et je n'aurai pas le temps de reprendre ma cité !
* La partie s’achève selon trois modalités distinctes : la **Suprématie**, l'**Épuisement** ou la **Diplomatie**

## Probabilités sur la fin par Diplomatie

Quelles fractions des seconds decks seront exploitées lorsque la fin par Diplomatie sera déclenchée ?

Considérons $(X_1, X_2, ... X_n)$ sont $n=2, 3, 4$ variables aléatoires indépendantes et uniforme sur $[0,1]$, qui représentent la position relative d'une carte Héraut, alors désignons par $Z_n=max(X_1, X_2, ... X_n)$ la position la plus reculée du dernier Héraut. Que dire sur $Z$ ?

Gemini nous dit que la fonction de répartition est assez simple :
$$
F(z) = P[Z_n \le z] = z^n
$$
Gemini en déduit facilement les moyennes et les quantiles. Voici les valeurs numériques:

| $n$  | Moyenne | Médiane | Quantile 90% |
| :--: | ------- | ------- | ------------ |
|  2   | 0.667   | 0.707   | 0.949        |
|  3   | 0.750   | 0.794   | 0.965        |
|  4   | 0.800   | 0.841   | 0.974        |

Ainsi, à 2 joueurs, en moyenne les parties sont nettement réduites. Mais à 3 et 4 joueurs, les seconds decks vont être en moyenne assez bien exploités; et si certains joueurs vont possiblement entamer un troisième deck, mécaniquement, au moins un joueur n'exploitera qu'un plus deux decks.

Conclusion : mission accomplie pour les Hérauts de Pourparlers, qui empêchent de joueur à l'infini des decks.

## Probabilités sur la Calamité Courroux de la Terre

Voici un résumé d'étude menée par Gemini où $X$ est la variable aléatoire qui représente le nombre de Donjons détruits :

* $D$ Donjons sont construits, et que cette valeur est supposée déterministe, de l'ordre de 8, 9 ou 10. Par défaut $D=10$.
* $J$ désigne le nombre de joueurs.
* $C$ désigne le nombre de positions tirées par carte Calamité. Les positions sont tirées sans remise. Par défaut $C=3$.
* 33 tuiles sont constructibles, une fois les 4 montagnes placées parmi les 37 tuiles du terrain de base.

Alors $X$ suit une loi dite hypergéométrique $H(n, p, N) = H(J\times C, \frac{D}{33}, 33)$.

Comme il n'y a pas remise de positions, c'est équivalent de cibler en une seule fois les positions.

| Nombre  de joueurs     | Nb de Donjons  (K) | Moyenne théorique | Médiane (50%  cumulé) | Quantile 90% (Pire cas) |
| ---------------------- | ------------------ | ----------------- | --------------------- | ----------------------- |
| 2 joueurs (6 tirages)  | 8  Donjons         | 1,45              | 1                     | 2                       |
|                        | 9  Donjons         | 1,64              | 2                     | 3                       |
|                        | 10  Donjons        | 1,82              | 2                     | 3                       |
| ---                    | ---                | ---               | ---                   | ---                     |
| 3 joueurs (9 tirages)  | 8  Donjons         | 2,18              | 2                     | 3                       |
|                        | 9  Donjons         | 2,45              | 2                     | 4                       |
|                        | 10  Donjons        | 2,73              | 3                     | 4                       |
| ---                    | ---                | ---               | ---                   | ---                     |
| 4 joueurs (12 tirages) | 8  Donjons         | 2,91              | 3                     | 4                       |
|                        | 9  Donjons         | 3,27              | 3                     | 5                       |
|                        | 10  Donjons        | 3,64              | 4                     | 5                       |

Si on raisonne sur le quantile 90%, et à 8 Donjons, alors le nombre de Donjons touchés est à peu près égal au nombre de joueurs. Donc, en gros, 1 Donjon par joueur. Ce ratio augmente un peu en passant à 9 ou 10 Donjons.

## Probabilités sur l'ensemble des Calamités

Comment évolue le nombre $X$ de tuiles touchées par une des 3 Calamités ?

Voici la synthèse et aussi des décisions de Game-Design que j'explique après. Le modèle d'occupation des tuiles est $T = 10 + 2 \times J$.

| Nombre  de Joueurs (J) | Calamités / deck | Tirages max (n) | Tuiles occupées  (T) | Moyenne globale | Moyenne / J | Médiane globale | Médiane / J | Quantile 90%  global | Quantile 90% / J |
| ---------------------- | ---------------- | --------------- | -------------------- | --------------- | ----------- | --------------- | ----------- | -------------------- | ---------------- |
| J=2                    | 2                | 12              | 14                   | 5,09            | 2,55        | 5               | 2,5         | 7                    | 3,5              |
| J=3                    | 2                | 18              | 16                   | 8,73            | 2,91        | 9               | 3           | 11                   | 3,67             |
| J=4                    | 1                | 12              | 18                   | 6,55            | 1,64        | 7               | 1,75        | 9                    | 2,25             |

Pour le second cycle du deck, le joueur insère dans sa défausse :

* une carte Héraut de Pourparlers, 

* 2 cartes Calamités qu'il choisit secrètement,
* et même 1 seul carte Calamité (secrètement choisie) à 4 joueurs.



## Remplacer les Calamités par Ordres-Interceptés

Lorsque l'événement Ordres-Interceptés est révélé par le joueur actif :

- Le joueur actif désigne un adversaire.
- Le joueur actif choisit en aveugle 2 cartes de la main adverse.
- Le joueur montre à tous ces 2 cartes, puis les place face visible dans la défausse de l'adversaire.
- Le joueur adverse reste avec 4 cartes en main jusqu'à la fin de son tour.
- A la fin de son tour, le joueur adverse se retrouvera toujours avec 6 cartes en main.

Au second cycle, en plus de la carte événement Héraut de Pourparlers, chaque joueur insère :

* Deux cartes événements Ordres-Interceptés à 2 et 3 joueurs.
* Une seule carte événement Ordres-Interceptés à 4 joueurs.

Le gameplay de la carte action Complot à la Cour est légèrement modifié:

* Le joueur pioche 6 cartes qu'il place dans sa main.
* Il défausse des cartes pour n'en conserver que 6 en main.

Gemini m'assure les probabilités suivantes pour un seul deck:

- Probabilité que les deux cartes Ordres-Interceptés soient placées avant la carte Héraut : 1/3
- Probabilité que les deux cartes Ordres-Interceptés soient placées après la carte Héraut : 1/3
- Probabilité que une et une seule carte Ordres-Interceptés soit placée avant la carte Héraut : 1/3
- Probabilité que une ou deux cartes Ordres-Interceptés soient placées avant la carte Héraut : 2/3

Raisonnement de Gemini :

* Si on considère que les 45 cartes du second deck sont équi-distribuées alors il suffit de considérer la répartition des 3 cartes $\{F_1, F_2, H\}$.
* Il y a 6 configurations équiprobables : $(F_1, F_2, H)$, $(F_2, F_1, H)$, $(F_1, H, F_2)$, $(F_2, H, F_1)$, $(H,F_1,F_2)$,$(H,F_2,F_1)$.
* Il n'y a plus qu'à compter ...
