> Programme fait par : Gabriel PONS / Lilia Michau

**- Quel était votre projet initial ?**

Notre but était de reproduire la roulette dans un casino où l’on pouvait parier une mise choisie parmi un somme d’argent définie.

**-Qu’avez-vous réalisé ?**

Nous avons réalisé un programme qui nous donne une somme d’argent définie lorsqu’on le lance (ici 1000$), puis il nous propose de miser sur un nombre entre 0 et 49 (comme dans une roulette classique) puis de choisir le montant de son pari. Si l’on tombe sur la bonne couleur l’on gagne notre mise plus 0.5 fois notre mise et si l’on a parié sur le numéro gagnant alors l’on gagne 3 fois notre mise. Si la couleur est mauvaise et que vous n’êtes pas tombé sur le numéro gagnant alors vous perdez votre mise.

**-Le programme fonctionne-t-il ? L’avez-vous éventuellement enrichi ?**

Oui, le programme fonctionne et nous l’avons enrichi avec :
-Un système qui donne le nombre d’argent restant à chaque fin de paris.
-Un système pour prévenir les éventuelles tricheries ou tentatives de bugs en mettant un nombre supérieur à ce qui est demandé lors du pari ou de la mise.
-Un système qui permet de terminer la partie si le joueur ne possède plus d’argents.
-Un système qui propose au joueur de quitter ou non le casino à chaque fin de paris s’il souhaite s’arrêté.

**-Quelles difficultés avez-vous rencontré ?**

Nous avons rencontré deux difficultés majeures.
La première était lors de la création du système qui permettait de proposer au joueur de quitter ou non le casino car nous n’avions aucune idée de comment faire en sorte que le programme se ferme si le joueur souhaite quitter le casino (erreur remédiée en mettant une grande partie du programme dans une boucle qui se ferme si le joueur quitte le casino, se qui entraîne la fin du programme).
La deuxième difficulté était que l’on ne peut pas afficher un long texte sur la calculatrice, l’on a donc étés obligés de raccourcir le texte tout en restant compréhensibles (ex : « Vous avez misez sur la bonne couleur ! Vous gagnez ! »  était trop grand pour être afficher sur la calculatrice, l’on a donc été obligés de raccourcir le texte en : « Bonne couleur ! Vous gagnez ! »
