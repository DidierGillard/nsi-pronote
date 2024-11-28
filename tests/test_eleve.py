import pytest

from src.Eleve import Eleve
from src.Note import Note
from src.Matiere import Matiere


@pytest.fixture
def eleve():
    return Eleve(1, "Eleve1", [
        Note(1, 18),
        Note(1, None),
        Note(2, 0),
        Note(1, 6),
        Note(1, 0)
    ])


@pytest.fixture
def eleve_sans_note():
    return Eleve(1, "Eleve1", [])


@pytest.fixture
def matieres():
    return [
        Matiere(identifiant=1, nom="NSI", coef=2),
        Matiere(identifiant=2, nom="Mathématique", coef=4),
        Matiere(identifiant=3, nom="Histoire", coef=1),
    ]


class TestListeNotesMatieres:
    def test_liste_correct(self, eleve):
        assert eleve.liste_notes_matiere(1) == [18, 6, 0], "liste seulement les notes non null de la matière"

    def test_liste_vide(self, eleve):
        assert eleve.liste_notes_matiere(3) == []


class TestANoteDansMatiere:
    def test_vrai(self, eleve):
        assert eleve.a_note_dans_matiere(1) == True

    def test_faux(self, eleve):
        assert eleve.a_note_dans_matiere(3) == False


class TestMoyenneMatiere:
    def test_moyenne_correct(self, eleve):
        assert eleve.moyenne_matiere(1) == 8.0

    def test_moyenne_sans_note_raise_ValueError(self, eleve):
        with pytest.raises(ValueError):
            eleve.moyenne_matiere(3)


class TestSommePondereeMoyennes:
    def test_somme_correcte(self, eleve, matieres):
        assert eleve.somme_ponderee_moyennes(matieres) == 16

    def test_sans_note_est_None(self, eleve_sans_note, matieres):
        assert eleve_sans_note.somme_ponderee_moyennes(matieres) is None


class TestSommePonderationsMatieres:
    def test_somme_correct(self, eleve, matieres):
        assert eleve.somme_ponderations_matieres(matieres) == 6

    def test_sans_note_est_None(self, eleve_sans_note, matieres):
        assert eleve_sans_note.somme_ponderations_matieres(matieres) is None


class TestMoyenneGenerale:
    def test_moyenne_correcte(self, eleve, matieres):
        assert eleve.moyenne_generale(matieres) == 16 / 6

    def test_moyenne_sans_note_est_None(self, eleve_sans_note, matieres):
        assert eleve_sans_note.moyenne_generale(matieres) is None

    def test_moyenne_correcte_mock_sommes(self, mocker, eleve, matieres):
        mocker.patch("src.Eleve.Eleve.somme_ponderee_moyennes", return_value=10)
        mocker.patch("src.Eleve.Eleve.somme_ponderations_matieres", return_value=5)

        assert eleve.moyenne_generale(matieres) == 10 / 5

    def test_moyenne_correcte_mock_moyenne(self, mocker, eleve, matieres):
        mock = mocker.patch("src.Eleve.Eleve.moyenne_matiere")
        mock.side_effect = [8, 5, 0]

        assert eleve.moyenne_generale(matieres) == 6
