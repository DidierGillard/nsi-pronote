class Note:
    matiere: int
    valeur: float
    coef: float

    def __init__(self, matiere: int, valeur: float = None, coef: float = 1) -> None:
        self.matiere = matiere
        self.valeur = valeur
        self.coef = coef
