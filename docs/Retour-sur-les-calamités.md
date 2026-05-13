# Retour sur les calamités

## Ressenti

- C'est bien qu'après avoir joué pendant 1 heure et déjà bien bataillé, il y ait une fin de partie inéluctable.

- Un peu  de calamités est admissible.

- Mais c'est dommage que trop de calamités renverse la hiérarchie de la piste de score.

## Analyse de la mécanique actuelle

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

