# -*- coding: utf-8 -*-
"""
=============================================================================
  SEANCE 2  -  LE LIVE CODING DE L'ENSEIGNANT
=============================================================================
  DEUX DEMONSTRATIONS, DEUX ATELIERS :

     13 h 07 - 13 h 15   etapes A, B, C   ->  print()
     13 h 15 - 13 h 27   les eleves font leur ecran d'accueil
     13 h 27 - 13 h 35   etapes D, E, F   ->  la variable, puis input()
     13 h 35 - 13 h 47   les eleves font "le jeu demande ton nom"

  A QUOI SERT CE FICHIER ?

  C'est VOTRE anti-seche. Le jour J, vous NE lancez PAS ce fichier :
  vous tapez devant les eleves, tres lentement, dans un fichier vide.
  Ce fichier est la pour repeter chez vous, et pour vous rattraper si
  vous perdez le fil devant la classe.

  REGLE D'OR : "JE CODE, VOUS PREDISEZ."
  Avant CHAQUE execution, vous vous arretez et vous demandez a la classe
  ce qui va s'afficher. Vous n'appuyez sur F5 qu'apres leur reponse.

  AVANT LA SEANCE : police de Thonny en taille 18 minimum (Outils >
  Options > Editeur), sinon le fond de la salle ne lit rien.
=============================================================================
"""

# =============================================================================
#  ETAPE A  (3 min)  -  LE PREMIER PRINT
# =============================================================================
#  Vous tapez caractere par caractere en verbalisant :
#    "p - r - i - n - t, ca veut dire AFFICHE.
#     Ensuite une parenthese : on l'ouvre, et on la fermera TOUJOURS.
#     Puis un guillemet, mon texte, un guillemet. Et on referme."
#
#  >>> AVANT D'APPUYER : "Qu'est-ce qui va se passer ? A trois. Un, deux, trois !"

print("Bonjour")

#  Apres l'execution :
#    "Voila. Vous venez de voir un ordinateur OBEIR. C'est tout le metier.
#     Attention au piege : print ne veut pas dire imprimer. Rien ne sort
#     sur du papier. print veut dire AFFICHE."
#
#  Montrez aussi, en une seconde, que les guillemets ne s'affichent pas :
#     ils disent seulement "ceci est du texte".


# =============================================================================
#  ETAPE B  (2 min)  -  IL LIT DE HAUT EN BAS, LIGNE PAR LIGNE
# =============================================================================
#  Vous ajoutez deux lignes, et vous demandez AVANT de lancer :
#     "Dans quel ordre ca va s'afficher ?"

print("Un")
print("Deux")
print("Trois")

#    "De haut en bas. Ligne par ligne. Toujours. Il ne devine pas,
#     il ne saute pas de ligne, il ne revient pas en arriere.
#     Si ca s'affiche dans le desordre, ce n'est pas lui : c'est l'ordre
#     de vos lignes."


# =============================================================================
#  ETAPE C  (3 min)  -  L'ERREUR VOLONTAIRE
# =============================================================================
#  >>> LE MOMENT LE PLUS IMPORTANT DE LA SEANCE <<<
#  Vous effacez un guillemet, devant eux, en l'annoncant :
#     "Maintenant, je casse tout."
#
#  (ligne volontairement fausse, laissee en commentaire pour que ce fichier
#   reste ouvrable dans Thonny — devant les eleves, vous la tapez pour de vrai)
# print("Bonjour)

#  Vous lancez. L'ecran devient rouge.
#
#    "Regardez. ROUGE. Est-ce que l'ordinateur est casse ? Non.
#     Est-ce que je suis puni ? Non.
#     Il m'explique ce qu'il n'a pas compris. Il dit SyntaxError :
#     j'ai mal ecrit quelque chose. Et il me montre meme la ligne.
#     Le rouge n'est pas une punition. LE ROUGE EST UNE INFORMATION.
#     Aujourd'hui, celui qui voit du rouge leve le pouce :
#     il a trouve quelque chose."
#
#  Vous remettez le guillemet, vous relancez, ca marche.
#
#  >>> ON S'ARRETE LA. Les eleves font leur ecran d'accueil : PARTIE 1
#      de leur fichier, etapes 1 a 5. Douze minutes.


# =============================================================================
#  ETAPE D  (3 min)  -  LA VARIABLE : UNE BOITE AVEC UNE ETIQUETTE
# =============================================================================
#  Tout le monde lache le clavier. Ecrans face a vous, mains sur la table.
#
#  D'abord SANS machine, avec les mains :
#     "J'ai une boite. Je colle une etiquette dessus : nom.
#      Je mets quelque chose dedans : Damien.
#      Quand je dis 'nom', l'ordinateur regarde dans la boite."

nom = "Damien"
print(nom)

#  >>> AVANT DE LANCER : "qu'est-ce qui va s'afficher ? nom, ou Damien ?"
#  C'est LA question du jour. Laissez-les se tromper : c'est comme ca
#  qu'ils comprennent. Puis vous lancez.
#
#    "Il affiche Damien. Parce que je n'ai pas mis de guillemets autour
#     de nom : je ne lui ai pas demande le mot 'nom', je lui ai demande
#     CE QU'IL Y A DANS LA BOITE."
#
#  Puis vous montrez la difference, en une ligne :

print("nom")

#    "La, avec les guillemets, il affiche le mot nom. Sans guillemets,
#     il affiche ce qu'il y a dans la boite. C'est toute la difference.
#     Souvenez-vous de ca : c'est l'erreur numero un de toute l'annee."


# =============================================================================
#  ETAPE E  (2 min)  -  input() : C'EST LE JOUEUR QUI REMPLIT LA BOITE
# =============================================================================
#     "Jusqu'ici, c'est MOI qui remplis la boite. Maintenant, je vais
#      laisser le JOUEUR la remplir."

nom = input("Comment t'appelles-tu ? ")
print(nom)

#  Vous lancez, et VOUS tapez un prenom d'eleve de la classe.
#  Effet garanti.
#
#    "Le programme s'est arrete et il m'attend. C'est ca, input :
#     il pose la question, il attend, et il range la reponse dans la boite."


# =============================================================================
#  ETAPE F  (2 min)  -  ON COLLE DU TEXTE ET UNE BOITE
# =============================================================================

print("Bonjour " + nom + " !")

#    "Le + colle des morceaux bout a bout.
#     Attention a l'espace apres Bonjour : sans lui, ca colle tout."
#
#  Montrez l'oubli de l'espace une fois : "BonjourDamien". Ils rient, ils retiennent.
#
#  >>> ET C'EST TOUT. On les envoie faire la PARTIE 2 de leur fichier,
#      etapes 6 a 8. Douze minutes.


# =============================================================================
#  LES QUATRE ERREURS QUI VONT ARRIVER PENDANT LES ATELIERS
# =============================================================================
#   SyntaxError ........ un guillemet ou une parenthese manque.
#                        "Compte tes guillemets : ils vont par deux."
#   NameError .......... du texte ecrit sans guillemets, ou une boite
#                        dont le nom est mal orthographie.
#                        "Tu as ecrit Nom et ta boite s'appelle nom."
#   BonjourDamien ...... l'espace manque dans "Bonjour ".
#                        "Il colle exactement ce que tu lui donnes."
#   Rien ne se passe ... l'eleve a ecrit dans la zone grise du bas.
#                        "Remonte dans la zone blanche, en haut."
#
#  Le dictionnaire complet : 1-methode/annexes/dictionnaire-des-erreurs.pdf
# =============================================================================
