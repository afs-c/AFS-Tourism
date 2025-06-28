import sys
from unittest.mock import MagicMock
from unittest.mock import Mock
from unittest.mock import patch

sys.modules['tkinter'] = MagicMock()
sys.modules['tkinter.ttk'] = MagicMock()

# apparently theres an uncallable version of magicmock
# for some reason it doesnt work unless i put it under sys.modules
# not sure if i completely understand it
# tkinter messes up sometimes if i get rid of this so i will keep it
# that simple

from project import tourGUI
from project import tour_guides

lorem = tourGUI()


@patch('project.tk.Tk')

def test_charity_tax(mock_tk):
    charitytax = lorem.charity_tax()
    assert 22 < charitytax < 35

def test_names_in_tourguide():
    names = [person.name for person in tour_guides]
    assert names == ['Mark', 'Ericsson', 'Zeynep']

def test_language_in_tourguide():
    langs = [person.language for person in tour_guides]
    assert langs == ['English', 'Finnish', 'Turkish']

def test_exp_in_tourguide():
    exp = [person.expertise for person in tour_guides if hasattr(person, 'expertise')]
    assert exp == ['Medieval History']
    spec = [person.specialty for person in tour_guides if hasattr(person, 'specialty')]
    assert spec == ['Wildlife and Photography']
    prof = [person.profession for person in tour_guides if hasattr(person, 'profession')]
    assert prof == ['None']

# the part above helped me with the get_recommendation function a lot.

