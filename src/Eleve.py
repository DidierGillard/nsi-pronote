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
