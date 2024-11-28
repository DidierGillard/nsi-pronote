import pytest

from src.Eleve import Eleve
from src.Note import Note


@pytest.fixture
def eleve():
    return Eleve(1, "Eleve1", [
        Note(1, 18),
        Note(1, None),
        Note(2, 0),
        Note(1, 6),
        Note(1, 0)
    ])


def test_liste_notes_matieres(eleve):
    assert eleve.liste_notes_matiere(1) == [18, 6, 0], "liste seulement les notes non null de la matière"

def test_liste_notes_matieres_vide(eleve):
    assert eleve.liste_notes_matiere(3) == []

def test_a_note_dans_matiere(eleve):
    assert eleve.a_note_dans_matiere(1) == True

def test_a_note_dans_matiere_sans_note(eleve):
    assert eleve.a_note_dans_matiere(3) == False

def test_moyenne_correct(eleve):
    assert eleve.moyenne_matiere(1) == 8.0

def test_moyenne_sans_note_raise_ValueError(eleve):
    with pytest.raises(ValueError):
        eleve.moyenne_matiere(3)
