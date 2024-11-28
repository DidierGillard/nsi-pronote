from src.Eleve import Eleve
from src.Note import Note


def test_liste_notes_matieres():
    eleve = Eleve(1, "Eleve1", [
        Note(1, 18),
        Note(1, None),
        Note(2, 0),
        Note(1, 6),
        Note(1, 0)
    ])
    assert eleve.liste_notes_matiere(1) == [18, 6, 0], "liste seulement les notes non null de la matière"


def test_liste_notes_matieres_vide():
    eleve = Eleve(1, "Eleve1", [])
    assert eleve.liste_notes_matiere(3) == []
