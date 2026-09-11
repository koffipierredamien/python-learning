# -*- coding: utf-8 -*-
"""
=============================================================================
  JEU XO  -  VERSION TERMINEE
=============================================================================
  A QUOI SERT CE FICHIER ?

  C'est le jeu fini : celui que l'enseignant lance au videoprojecteur
  pendant les 4 premieres minutes de la seance 1 (le "WOW"), pour montrer
  aux eleves ce qu'ils vont construire en 22 samedis.

  CE FICHIER N'EST PAS DONNE AUX ELEVES.
  Ils ne doivent pas le lire : ils doivent avoir envie de le refaire.

  COMMENT LE LANCER
  -----------------
  1. Ouvrir ce fichier dans Thonny
  2. Appuyer sur F5 (ou le bouton vert)
  3. Une fenetre s'ouvre. Cliquer sur "2 JOUEURS" et jouer contre un eleve.

  CONSEILS POUR LA DEMO
  ---------------------
  - Lancez-le AVANT que les eleves entrent, puis reduisez la fenetre.
    Chercher le fichier devant la classe casse tout l'effet.
  - Jouez a "2 JOUEURS" avec un eleve volontaire, pas contre l'ordinateur.
  - Perdez. C'est meilleur pour la suite.
  - Le bouton "ORDINATEUR (difficile)" est imbattable : gardez-le pour
    la fin, ou pour un eleve tres avance qui voudrait un defi.

  Teste avec Python 3.8 et suivants. Aucune installation supplementaire.
=============================================================================
"""

# tkinter sert uniquement a la fenetre graphique. On l'importe prudemment :
# ainsi la logique du jeu reste lisible (et testable) meme sur une machine
# ou tkinter n'est pas installe.
try:
    import tkinter as tk
    from tkinter import font as tkfont
    TKINTER_DISPONIBLE = True
except ImportError:                      # pragma: no cover
    tk = None
    tkfont = None
    TKINTER_DISPONIBLE = False


# =============================================================================
#  PARTIE 1 : LA LOGIQUE DU JEU
#  (du Python pur : c'est ce que les eleves ecriront des la seance 6)
# =============================================================================

VIDE = " "

# Les 8 facons de gagner : 3 lignes, 3 colonnes, 2 diagonales
ALIGNEMENTS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),      # lignes
    (0, 3, 6), (1, 4, 7), (2, 5, 8),      # colonnes
    (0, 4, 8), (2, 4, 6),                 # diagonales
]


def nouveau_plateau():
    """Renvoie un plateau vide : une liste de 9 cases."""
    return [VIDE] * 9


def alignement_gagnant(plateau):
    """Renvoie le trio de cases gagnant, ou None si personne n'a gagne."""
    for trio in ALIGNEMENTS:
        a, b, c = trio
        if plateau[a] != VIDE and plateau[a] == plateau[b] == plateau[c]:
            return trio
    return None


def gagnant(plateau):
    """Renvoie 'X', 'O', ou None."""
    trio = alignement_gagnant(plateau)
    if trio is None:
        return None
    return plateau[trio[0]]


def cases_libres(plateau):
    """Renvoie la liste des numeros de cases encore vides."""
    return [i for i in range(9) if plateau[i] == VIDE]


def partie_finie(plateau):
    """Vrai si quelqu'un a gagne ou si le plateau est plein."""
    return gagnant(plateau) is not None or len(cases_libres(plateau)) == 0


def _minimax(plateau, joueur, ordinateur, profondeur):
    """
    Explore tous les coups possibles et renvoie (score, case).
    Score du point de vue de l'ordinateur : +10 s'il gagne, -10 s'il perd, 0 si nul.
    On retranche la profondeur pour qu'il prefere gagner VITE et perdre TARD.
    """
    vainqueur = gagnant(plateau)
    if vainqueur == ordinateur:
        return 10 - profondeur, None
    if vainqueur is not None:
        return profondeur - 10, None
    libres = cases_libres(plateau)
    if not libres:
        return 0, None

    autre = "O" if joueur == "X" else "X"
    meilleur_score = None
    meilleure_case = libres[0]

    for case in libres:
        plateau[case] = joueur
        score, _ = _minimax(plateau, autre, ordinateur, profondeur + 1)
        plateau[case] = VIDE

        if joueur == ordinateur:            # l'ordinateur maximise
            if meilleur_score is None or score > meilleur_score:
                meilleur_score, meilleure_case = score, case
        else:                                # l'humain minimise
            if meilleur_score is None or score < meilleur_score:
                meilleur_score, meilleure_case = score, case

    return meilleur_score, meilleure_case


def coup_ordinateur(plateau, symbole):
    """Renvoie le meilleur coup possible pour 'symbole'. Imbattable."""
    _, case = _minimax(list(plateau), symbole, symbole, 0)
    return case


# =============================================================================
#  PARTIE 2 : LA FENETRE
#  (Tkinter : c'est ce que les eleves construiront a partir de la seance 14)
# =============================================================================

FOND        = "#12122a"
FOND_CASE   = "#1e1e3f"
SURVOL      = "#2a2a5c"
GAGNANT     = "#1e9e4a"
TRAIT       = "#3a3a6e"
BLANC       = "#f4f4ff"
COULEUR_X   = "#4fc3f7"
COULEUR_O   = "#ffb74d"
ACCENT      = "#b06fd8"


class JeuXO:

    def __init__(self, racine):
        self.racine = racine
        self.racine.title("JEU XO  -  Jerusalem Geeks & Jeremiah Geeks")
        self.racine.configure(bg=FOND)
        self.racine.minsize(520, 720)

        self.plateau = nouveau_plateau()
        self.joueur = "X"
        self.contre_ordinateur = False
        self.partie_terminee = False
        self.score = {"X": 0, "O": 0, "N": 0}

        self.police_titre = tkfont.Font(family="Trebuchet MS", size=26, weight="bold")
        self.police_info  = tkfont.Font(family="Trebuchet MS", size=15)
        self.police_case  = tkfont.Font(family="Trebuchet MS", size=54, weight="bold")
        self.police_bouton= tkfont.Font(family="Trebuchet MS", size=11, weight="bold")
        self.police_score = tkfont.Font(family="Trebuchet MS", size=13)

        self._construire()
        self._rafraichir()

    # ---------------------------------------------------------------- interface
    def _construire(self):
        tk.Label(self.racine, text="⨯  JEU  XO  ○", font=self.police_titre,
                 bg=FOND, fg=BLANC).pack(pady=(22, 2))
        tk.Label(self.racine, text="construit brique par brique, un samedi a la fois",
                 font=("Trebuchet MS", 10), bg=FOND, fg=ACCENT).pack(pady=(0, 14))

        # Choix du mode
        barre = tk.Frame(self.racine, bg=FOND)
        barre.pack(pady=(0, 14))
        self.bouton_duo = self._bouton(barre, "👥  2 JOUEURS", lambda: self._mode(False))
        self.bouton_ia  = self._bouton(barre, "🤖  ORDINATEUR (difficile)", lambda: self._mode(True))
        self.bouton_duo.pack(side="left", padx=5)
        self.bouton_ia.pack(side="left", padx=5)

        self.info = tk.Label(self.racine, text="", font=self.police_info, bg=FOND, fg=BLANC)
        self.info.pack(pady=(0, 12))

        # La grille
        grille = tk.Frame(self.racine, bg=TRAIT)
        grille.pack(padx=26)
        self.cases = []
        for i in range(9):
            case = tk.Label(grille, text=" ", font=self.police_case, width=2, height=1,
                            bg=FOND_CASE, fg=BLANC, cursor="hand2")
            case.grid(row=i // 3, column=i % 3, padx=3, pady=3, sticky="nsew")
            case.bind("<Button-1>",  lambda e, n=i: self._clic(n))
            case.bind("<Enter>",     lambda e, n=i: self._survol(n, True))
            case.bind("<Leave>",     lambda e, n=i: self._survol(n, False))
            self.cases.append(case)

        self.etiquette_score = tk.Label(self.racine, text="", font=self.police_score,
                                        bg=FOND, fg=ACCENT)
        self.etiquette_score.pack(pady=(18, 8))

        bas = tk.Frame(self.racine, bg=FOND)
        bas.pack(pady=(0, 22))
        self._bouton(bas, "↻  REJOUER",        self.rejouer).pack(side="left", padx=5)
        self._bouton(bas, "0  REMETTRE A ZERO", self.remise_a_zero).pack(side="left", padx=5)

    def _bouton(self, parent, texte, action):
        return tk.Button(parent, text=texte, font=self.police_bouton, command=action,
                         bg=FOND_CASE, fg=BLANC, activebackground=SURVOL, activeforeground=BLANC,
                         relief="flat", padx=14, pady=8, cursor="hand2", bd=0,
                         highlightthickness=0)

    # ------------------------------------------------------------------- actions
    def _mode(self, contre_ordinateur):
        self.contre_ordinateur = contre_ordinateur
        self.rejouer()

    def _survol(self, numero, dedans):
        if self.partie_terminee or self.plateau[numero] != VIDE:
            return
        self.cases[numero].configure(bg=SURVOL if dedans else FOND_CASE)

    def _clic(self, numero):
        if self.partie_terminee or self.plateau[numero] != VIDE:
            return
        self._jouer(numero, self.joueur)
        if self.partie_terminee:
            return
        if self.contre_ordinateur and self.joueur == "O":
            self.racine.after(350, self._tour_ordinateur)

    def _tour_ordinateur(self):
        if self.partie_terminee:
            return
        case = coup_ordinateur(self.plateau, "O")
        if case is not None:
            self._jouer(case, "O")

    def _jouer(self, numero, symbole):
        self.plateau[numero] = symbole
        self.joueur = "O" if symbole == "X" else "X"
        self._rafraichir()

        vainqueur = gagnant(self.plateau)
        if vainqueur is not None:
            self.partie_terminee = True
            self.score[vainqueur] += 1
            for case in alignement_gagnant(self.plateau):
                self.cases[case].configure(bg=GAGNANT)
            self.info.configure(text="🏆   %s A GAGNE !" % vainqueur, fg=BLANC)
        elif not cases_libres(self.plateau):
            self.partie_terminee = True
            self.score["N"] += 1
            self.info.configure(text="🤝   MATCH NUL", fg=BLANC)
        self._rafraichir_score()

    def rejouer(self):
        self.plateau = nouveau_plateau()
        self.joueur = "X"
        self.partie_terminee = False
        for case in self.cases:
            case.configure(text=" ", bg=FOND_CASE)
        self._rafraichir()

    def remise_a_zero(self):
        self.score = {"X": 0, "O": 0, "N": 0}
        self.rejouer()

    # ------------------------------------------------------------------ affichage
    def _rafraichir(self):
        for i, valeur in enumerate(self.plateau):
            couleur = COULEUR_X if valeur == "X" else COULEUR_O
            self.cases[i].configure(text=valeur, fg=couleur)
        if not self.partie_terminee:
            if self.contre_ordinateur:
                qui = "A toi de jouer  (tu es X)" if self.joueur == "X" else "L'ordinateur reflechit..."
            else:
                qui = "Au tour de  %s" % self.joueur
            self.info.configure(text=qui, fg=BLANC)
        self._rafraichir_score()
        self.bouton_duo.configure(bg=SURVOL if not self.contre_ordinateur else FOND_CASE)
        self.bouton_ia.configure(bg=SURVOL if self.contre_ordinateur else FOND_CASE)

    def _rafraichir_score(self):
        self.etiquette_score.configure(
            text="X : %d      O : %d      Nuls : %d"
                 % (self.score["X"], self.score["O"], self.score["N"]))


def lancer():
    if not TKINTER_DISPONIBLE:
        print("tkinter n'est pas installe sur cette machine : la fenetre ne peut")
        print("pas s'ouvrir. Windows / Mac : reinstallez Python depuis python.org")
        print("en cochant 'tcl/tk and IDLE'.  Linux : sudo apt install python3-tk")
        return
    racine = tk.Tk()
    JeuXO(racine)
    racine.mainloop()


if __name__ == "__main__":
    lancer()
