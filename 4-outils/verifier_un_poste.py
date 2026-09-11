# -*- coding: utf-8 -*-
"""
=============================================================================
  VERIFICATION AVANT LA SEANCE  -  a lancer chez vous, une fois
=============================================================================
  Ce petit programme verifie que tout est pret sur la machine :
    - la version de Python,
    - que la logique du jeu fonctionne (victoires, match nul, l'ordinateur),
    - que tkinter (la fenetre graphique) est bien installe.

  COMMENT L'UTILISER : ouvrez ce fichier dans Thonny, appuyez sur F5,
  et lisez le rapport. Tout doit etre marque [OK].
=============================================================================
"""

import sys, os, random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 62)
print("  VERIFICATION DU POSTE  -  JEU XO")
print("=" * 62)

# ---------------------------------------------------------------- 1. Python
version = "%d.%d.%d" % sys.version_info[:3]
if sys.version_info >= (3, 6):
    print("[OK]    Python %s" % version)
else:
    print("[ERREUR] Python %s est trop ancien. Il faut Python 3.6 ou plus." % version)
    sys.exit(1)

# ------------------------------------------------------------ 2. la logique
try:
    from jeu_xo_complet import (nouveau_plateau, gagnant, cases_libres,
                                partie_finie, coup_ordinateur, ALIGNEMENTS)
except ImportError as erreur:
    print("[ERREUR] Impossible de lire jeu_xo_complet.py : %s" % erreur)
    print("         Verifiez que verifier_un_poste.py et jeu_xo_complet.py sont bien")
    print("         dans le MEME dossier.")
    sys.exit(1)

problemes = 0

for trio in ALIGNEMENTS:
    plateau = nouveau_plateau()
    for case in trio:
        plateau[case] = "O"
    if gagnant(plateau) != "O":
        print("[ERREUR] alignement non detecte : %s" % (trio,))
        problemes += 1
if problemes == 0:
    print("[OK]    Detection du gagnant : les 8 alignements fonctionnent")

plateau_nul = list("XOXOXOOXO")
if gagnant(plateau_nul) is None and partie_finie(plateau_nul):
    print("[OK]    Detection du match nul")
else:
    print("[ERREUR] Le match nul n'est pas detecte correctement")
    problemes += 1

# ------------------------------------------ 3. l'ordinateur est-il imbattable ?
random.seed(1)
defaites = 0
for numero in range(40):
    plateau, tour = nouveau_plateau(), "X"
    ordinateur = "X" if numero % 2 == 0 else "O"
    while not partie_finie(plateau):
        if tour == ordinateur:
            case = coup_ordinateur(plateau, ordinateur)
        else:
            case = random.choice(cases_libres(plateau))
        plateau[case] = tour
        tour = "O" if tour == "X" else "X"
    vainqueur = gagnant(plateau)
    if vainqueur is not None and vainqueur != ordinateur:
        defaites += 1
if defaites == 0:
    print("[OK]    L'ordinateur est imbattable (40 parties, 0 defaite)")
else:
    print("[ERREUR] L'ordinateur a perdu %d fois sur 40" % defaites)
    problemes += 1

# ----------------------------------------------------------------- 4. tkinter
try:
    import tkinter
    print("[OK]    tkinter installe (version %s) : la fenetre s'ouvrira" % tkinter.TkVersion)
except ImportError:
    print("[ERREUR] tkinter n'est pas installe : le jeu graphique ne pourra pas")
    print("         s'ouvrir sur cette machine.")
    print("         Windows / Mac : reinstallez Python depuis python.org en")
    print("           cochant 'tcl/tk and IDLE'.")
    print("         Linux : sudo apt install python3-tk")
    problemes += 1

print("=" * 62)
if problemes == 0:
    print("  TOUT EST PRET.  Lancez maintenant jeu_xo_complet.py pour tester la demo.")
else:
    print("  %d PROBLEME(S) A REGLER avant la seance." % problemes)
print("=" * 62)
