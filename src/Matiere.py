from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.Eleve import Eleve
    

class Matiere:
    id: int
    nom: str
    coef: float
    
    def __init__(self, identifiant: int, nom: str, coef: float) -> None:
        self.id = identifiant
        self.nom = nom
        self.coef = coef

    def moyenne(self, classe: List[Eleve]) -> float|None:
        somme_moyenne = 0
        nb_eleve = 0
        for eleve in classe:
            try:
                somme_moyenne += eleve.moyenne_matiere(self.id)
                nb_eleve += 1
            except ValueError:
                pass
        return somme_moyenne / nb_eleve if nb_eleve > 0 else None
