class Matiere:
    id: int
    nom: str
    coef: float
    
    def __init__(self, identifiant: int, nom: str, coef: float) -> None:
        self.id = identifiant
        self.nom = nom
        self.coef = coef