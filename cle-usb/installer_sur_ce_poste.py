# -*- coding: utf-8 -*-
"""
=============================================================================
  INSTALLER LE DOSSIER "GEEKS" SUR CE POSTE
=============================================================================
  A LANCER UNE FOIS SUR CHAQUE ORDINATEUR DE LA SALLE, avant la seance.

  Ce programme cree sur le Bureau un dossier  GEEKS  contenant :

      GEEKS/
        |-- xo_officiel/   <- le code de reference (LE FILET)
        |-- mon_xo/        <- le dossier de travail de l'eleve
        |     `-- jeu.py       (le fichier de la piste Bleue, deja pret)
        `-- LISEZ-MOI.txt

  COMMENT FAIRE
  -------------
  1. Branchez la cle USB.
  2. Ouvrez ce fichier dans Thonny (ou double-cliquez dessus).
  3. F5. Lisez le rapport. C'est tout.

  IL NE DETRUIT JAMAIS LE TRAVAIL D'UN ELEVE.
  Si un dossier GEEKS existe deja, les fichiers de l'eleve sont conserves :
  seuls les fichiers manquants sont ajoutes. Pour forcer la remise a neuf
  (debut d'annee, ou poste a nettoyer), lancez :  python installer_sur_ce_poste.py --neuf
=============================================================================
"""

import os
import shutil
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "2-A-COPIER-SUR-LES-POSTES", "GEEKS")
NOMS_DE_BUREAU = ("Desktop", "Bureau", "Escritorio", "Schreibtisch")


def trouver_le_bureau():
    """Renvoie le chemin du Bureau, en essayant plusieurs pistes."""
    maison = os.path.expanduser("~")

    # 1. le cas normal
    for nom in NOMS_DE_BUREAU:
        chemin = os.path.join(maison, nom)
        if os.path.isdir(chemin):
            return chemin

    # 2. Windows avec OneDrive : le Bureau est deplace
    for dossier in os.listdir(maison) if os.path.isdir(maison) else []:
        if dossier.lower().startswith("onedrive"):
            for nom in NOMS_DE_BUREAU:
                chemin = os.path.join(maison, dossier, nom)
                if os.path.isdir(chemin):
                    return chemin

    # 3. Linux configure dans une autre langue
    try:
        import subprocess
        chemin = subprocess.check_output(
            ["xdg-user-dir", "DESKTOP"], stderr=subprocess.DEVNULL).decode().strip()
        if chemin and os.path.isdir(chemin):
            return chemin
    except Exception:
        pass

    # 4. on abandonne : on installera dans le dossier personnel
    return maison


def copier(source, cible, ecraser, rapport):
    """Copie source -> cible en ajoutant seulement ce qui manque."""
    if not os.path.isdir(cible):
        os.makedirs(cible)
        rapport.append(("cree", cible))

    for nom in sorted(os.listdir(source)):
        if nom.startswith("."):             # fichiers techniques : on les ignore
            continue
        chemin_source = os.path.join(source, nom)
        chemin_cible = os.path.join(cible, nom)

        if os.path.isdir(chemin_source):
            copier(chemin_source, chemin_cible, ecraser, rapport)
        elif not os.path.exists(chemin_cible):
            shutil.copy2(chemin_source, chemin_cible)
            rapport.append(("copie", chemin_cible))
        elif ecraser:
            shutil.copy2(chemin_source, chemin_cible)
            rapport.append(("remplace", chemin_cible))
        else:
            rapport.append(("conserve", chemin_cible))


def principal():
    ecraser = "--neuf" in sys.argv

    print("=" * 64)
    print("  INSTALLATION DU DOSSIER GEEKS")
    print("=" * 64)

    if not os.path.isdir(SOURCE):
        print("[ERREUR] Je ne trouve pas le dossier modele :")
        print("         %s" % SOURCE)
        print()
        print("  Lancez ce programme DEPUIS LA CLE USB, sans deplacer les")
        print("  dossiers qui sont a cote de lui.")
        return 1

    bureau = trouver_le_bureau()
    cible = os.path.join(bureau, "GEEKS")
    print("  Bureau detecte : %s" % bureau)
    print("  Dossier a creer : %s" % cible)
    if ecraser:
        print("  Mode --neuf : les fichiers existants seront REMPLACES.")
    print("-" * 64)

    rapport = []
    try:
        copier(SOURCE, cible, ecraser, rapport)
    except PermissionError:
        print("[ERREUR] Ecriture refusee sur ce poste (droits insuffisants).")
        print("         Demandez a l'administrateur, ou installez le dossier")
        print("         GEEKS dans le dossier personnel de l'eleve.")
        return 1

    for action, chemin in rapport:
        marque = {"cree": "+ dossier ", "copie": "+ fichier ",
                  "remplace": "~ remplace", "conserve": "= conserve"}[action]
        print("  %s  %s" % (marque, os.path.relpath(chemin, bureau)))

    conserves = sum(1 for action, _ in rapport if action == "conserve")
    print("-" * 64)
    print("  TERMINE.")
    if conserves and not ecraser:
        print("  %d fichier(s) deja presents ont ete conserves (travail des eleves)." % conserves)
        print("  Pour tout remettre a neuf : python installer_sur_ce_poste.py --neuf")
    print()
    print("  A VERIFIER MAINTENANT SUR CE POSTE :")
    print("    1. Le dossier GEEKS est visible sur le Bureau")
    print("    2. Thonny s'ouvre")
    print("    3. GEEKS/mon_xo/jeu.py s'ouvre dans Thonny et s'execute avec F5")
    print("    4. La police de Thonny est en taille 18 (Outils > Options > Editeur)")
    print("=" * 64)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
