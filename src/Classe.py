from typing import List

from src.Matiere import Matiere
from src.Eleve import Eleve


class Classe:
    """ :return la liste des moyennes générales des éléves ayant eu des notes """

    @staticmethod
    def moyennes_generales(classe: List[Eleve], matieres: List[Matiere]) -> List[float|None]:
        return [eleve.moyenne_generale(matieres) for eleve in classe]

    """ :return la liste des moyennes des matières """

    @staticmethod
    def moyennes_matieres(classe: List[Eleve], matieres: List[Matiere]) -> List[float|None]:
        return [matiere.moyenne(classe) for matiere in matieres]
