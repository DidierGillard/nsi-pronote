from typing import List
from src.Note import Note
from src.Matiere import Matiere

class Eleve:
    id: int
    nom: str
    notes: List[Note]
    def __init__(self, identifiant: int, nom: str, notes: List[Note]) -> None:
        self.id = identifiant
        self.nom = nom
        self.notes = [*notes]

    """ :return la liste des valeurs non nulles, des notes de la matière passée en paramètre ou un tableau vide si aucune note pour cette matière """

    def liste_notes_matiere(self, matiere: int) -> List[float]:
        return [
            note.valeur
            for note in self.notes
            if note.matiere == matiere and note.valeur is not None
        ]

    """ :return vrai si l'élève à au moins une note dans la matière passée en paramètre, ou faux dans le cas contraire """

    def a_note_dans_matiere(self, matiere: int) -> bool:
        return len(self.liste_notes_matiere(matiere)) != 0

    """ :return la moyenne arithmétique des notes non nulles de la matière passée en paramètre """
    """ :exception ValueError si l'atudiant n'a aucune note dans cette matière """

    def moyenne_matiere(self, matiere: int) -> float:
        notes = self.liste_notes_matiere(matiere)
        nb_notes = len(self.liste_notes_matiere(matiere))
        if nb_notes == 0:
            raise ValueError

        return sum(notes) / nb_notes

    """ :return la somme pondérée des moyennes des matieres de l'éléve. None si l'éléve n'a aucune note """
    def somme_ponderee_moyennes(self, matieres: List[Matiere]) -> float|None:
        somme = 0
        a_note = False
        for matiere in matieres:
            try:
                moy = self.moyenne_matiere(matiere.id)
                somme += moy * matiere.coef
                a_note = True
            except ValueError:
                pass

        return somme if a_note else None

    """ :return la somme des coéfficients des matières pour lesquelles l'éléve à au moins une note non null """
    def somme_ponderations_matieres(self, matieres: List[Matiere]) -> float|None:
        somme = 0
        a_note = False
        for matiere in matieres:
            if self.a_note_dans_matiere(matiere.id):
                somme += matiere.coef
                a_note = True

        return somme if a_note else None

    """ :return la moyenne générale de l'éléve. None si l'éléve n'a aucune note """

    def moyenne_generale(self, matieres: List[Matiere]) -> float|None:
        somme_ponderee = self.somme_ponderee_moyennes(matieres)
        ponderations = self.somme_ponderations_matieres(matieres)
        return somme_ponderee / ponderations if somme_ponderee is not None else None
