# -*- coding: utf-8 -*-
"""
=============================================================================
  SEANCE 1  -  LE LIVE CODING DU CAPITAINE   (78 - 90 min)
=============================================================================
  A QUOI SERT CE FICHIER ?

  C'est VOTRE anti-seche pour les 12 minutes de live coding.
  Le jour J, vous NE lancez PAS ce fichier : vous tapez devant les eleves,
  tres lentement, dans un fichier vide. Ce fichier est la pour :
    - repeter chez vous avant la seance,
    - vous rattraper si vous perdez le fil devant la classe.

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
#    "Voila. Vous venez de voir un ordinateur OBEIR. C'est tout le metier."


# =============================================================================
#  ETAPE B  (2 min)  -  L'ORDRE DES LIGNES
# =============================================================================
#  Vous ajoutez une deuxieme ligne.
#
#  >>> AVANT D'APPUYER : "Qu'est-ce que ca va afficher ? Dans quel ordre ?
#      Levez la main ceux qui pensent que Bonjour sortira en premier."

print("Bonjour")
print("Je suis ton ordinateur")

#  Apres l'execution :
#    "Regle numero un de la programmation : l'ordinateur lit de haut en bas,
#     ligne par ligne, dans l'ordre. Toujours."


# =============================================================================
#  ETAPE C  (4 min)  -  L'ERREUR VOLONTAIRE
#  >>> LE MOMENT LE PLUS IMPORTANT DE LA SEANCE <<<
# =============================================================================
#  Vous effacez le guillemet de fin. Le code devient :
#
#         print("Bonjour)
#
#  (Il est en commentaire ici pour que ce fichier reste executable.
#   Le jour J, vous le tapez VRAIMENT, et ca plante VRAIMENT.)
#
#  Vous lancez. Du rouge apparait. Vous SOURIEZ, et vous dites :
#
#    "Ah ! Du rouge ! ... Alors, qui a peur ?"
#    (laisser reagir, puis, tres calmement :)
#    "Moi je code depuis des annees, et j'ai du rouge TOUS LES JOURS.
#     Le rouge, ce n'est pas une punition. Ce n'est pas une mauvaise note.
#     C'est l'ordinateur qui vous explique ce qu'il n'a pas compris.
#     Il essaie de vous aider. Le probleme, c'est qu'il le dit en anglais.
#     Alors on va apprendre a le lire. Ensemble.
#     Il a ecrit : SyntaxError. Quelqu'un devine ?
#     ... Syntax, c'est la grammaire. Error, l'erreur.
#     Il nous dit : JE NE COMPRENDS PAS TA PHRASE.
#     Et regardez : il montre meme l'endroit avec une petite fleche."
#
#  Vous reparez devant tout le monde, vous relancez, ca marche :
#
#    "Repare en quatre secondes. Retenez ca : dans cette salle,
#     LE ROUGE N'EST PAS GRAVE. LE ROUGE EST UNE INFORMATION."
#
#  Puis vous allez ecrire SyntaxError sur l'affiche "Dictionnaire des
#  erreurs", et vous nommez le Gardien des erreurs de la seance.
#
#  ---------------------------------------------------------------------------
#  SI VOUS VOULEZ MONTRER UNE AUTRE ERREUR (au choix, une seule suffit) :
#         Print("Bonjour")      ->  NameError : "je ne connais pas ce mot"
#         print(Bonjour)        ->  NameError : le texte sans guillemets
#         print "Bonjour"       ->  SyntaxError : parentheses oubliees
#  ---------------------------------------------------------------------------


# =============================================================================
#  ETAPE D  (3 min)  -  LA CONSIGNE DE L'ATELIER
# =============================================================================
#  Vous projetez le resultat a obtenir, et vous annoncez les 3 pistes.
#  Le voici, tel quel :

print("===================================")
print("       BIENVENUE DANS LE JEU XO")
print("===================================")
print("Cree par : Damien")

#  Puis, mot pour mot :
#
#    "Votre mission : faire dire ca a votre ordinateur. Avec VOTRE prenom.
#     Trois pistes, vous choisissez :
#       BLEUE  - le debut est deja ecrit dans votre fichier, vous completez
#                les trous. Aucune honte : c'est la piste la plus maligne
#                quand on debute.
#       ROUGE  - vous ecrivez tout vous-memes, a partir de la consigne.
#       NOIRE  - tout ca, ET en plus vous dessinez la grille vide du morpion
#                en dessous. Avec des print, uniquement.
#
#     Personne ne vous jugera sur votre piste. LE JEU QUI SORT EST LE MEME.
#     Cartes de signalisation sorties. Pilotes, a vous.
#     Copilotes : vos mains restent sur vos genoux ! C'est parti."
#
#  >>> Vous lancez le minuteur. Rotation pilote/copilote a 99 min.
# =============================================================================
