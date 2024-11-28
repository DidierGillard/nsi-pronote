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
