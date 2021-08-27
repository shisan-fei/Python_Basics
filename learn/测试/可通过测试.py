import unittest
from name_fun import get_name

class NameTest(unittest.TestCase):

    def test_name(self):
        name = get_name('wang','longfei')
        self.assertEqual(name,'wang longfei')