import pytest
import requests

from src.Eleve import Eleve
from src.Matiere import Matiere
from src.Note import Note
from src.Classe import Classe


@pytest.fixture
def classe():
    """ récupération des élèves et matière à partir de l'api """
    response = requests.get("http://localhost:3000/classe")
    classe = []
    for eleve in response.json():
        notes = [Note(matiere=note["idMatiere"], valeur=note["valeur"], coef=note["coef"] if "coef" in note else 1) for
                 note in eleve["notes"]]
        classe.append(Eleve(identifiant=eleve["id"], nom=eleve["nom"], notes=notes))
    return classe


@pytest.fixture
def matieres():
    response = requests.get("http://localhost:3000/matieres")
    return [Matiere(identifiant=matiere["id"], nom=matiere["nom"], coef=matiere["coef"]) for matiere in response.json()]


def test_moyennes_classe(classe, matieres):
    eleves_avec_moyenne = Classe.moyennes_generales(classe, matieres)

    assert eleves_avec_moyenne == [8.5, 0.0, 9.75, None]


def test_moyennes_classe_utilise_notes_moyenne(mocker, classe, matieres):
    spy = mocker.spy(Eleve, "moyenne_generale")

    Classe.moyennes_generales(classe, matieres)

    spy.assert_called()
    assert spy.call_count == 4
    spy.assert_any_call(classe[0], matieres)
    spy.assert_any_call(classe[1], matieres)
    spy.assert_any_call(classe[2], matieres)
    spy.assert_any_call(classe[3], matieres)
