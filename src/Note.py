class Note:
    matiere: int
    valeur: float

    def __init__(self, matiere: int, valeur: float = None) -> None:
        self.matiere = matiere
        self.valeur = valeur
