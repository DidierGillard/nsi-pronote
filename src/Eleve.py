from typing import List
from src.Note import Note

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

        return sum(notes) / nb_notes
