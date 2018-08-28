from unittest import TestCase
from my_rada.rada_models import Deputat, UkraineVerkhovnaRada
from unittest.mock import MagicMock


class TestDeputat(TestCase):

    def test_init(self):

        with self.assertRaises(TypeError) as e:
            dep = Deputat()

        # self.assertEqual(e.exception.args[0],
        #                  '')

        dep = Deputat(60, 180, 'Trush', 'Vasyl', 22)

        self.assertEqual(dep.weight, 60)
        self.assertEqual(dep.height, 180)
        self.assertEqual(dep.last_name, 'Trush')
        self.assertEqual(dep.first_name, 'Vasyl')
        self.assertEqual(dep.age, 22)

    def test_rada(self):

        rada = UkraineVerkhovnaRada()

        dep = MagicMock()
        dep.give_tribute.return_value = False
