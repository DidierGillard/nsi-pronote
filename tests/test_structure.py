from src.Note import Note
from src.Matiere import Matiere
from src.Eleve import Eleve

def test_class_Note():
    note = Note(matiere=2, valeur=12.5)
    assert note.matiere == 2
    assert note.valeur == 12.5

def test_class_Matiere():
    mat = Matiere(identifiant=2, nom="histoire", coef=3)
    assert mat.id == 2
    assert mat.nom == "histoire"
    assert mat.coef == 3

def test_class_Eleve():
    note1 = Note(matiere=2, valeur=12.5)
    note2 = Note(matiere=2, valeur=None)
    eleve = Eleve(identifiant=2, nom="Dupont", notes=[note1, note2])
    assert eleve.id == 2
    assert eleve.nom == "Dupont"
    assert eleve.notes == [note1, note2]
