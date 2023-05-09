# pylint: disable= missing-docstring
import unittest
from task_two import StringTriukai


class TestSakinys(unittest.TestCase):
    def setUp(self) -> None:
        self.sakinys1 = StringTriukai("Ka tu ka vakare?")
        self.sakinys2 = StringTriukai("Hello world!")
        self.sakinys3 = StringTriukai("Print line()")

    def test_pirmas_zodis(self):
        self.assertEqual(self.sakinys1.pirmas_zodis(), "Ka")
        self.assertEqual(self.sakinys2.pirmas_zodis(), "Hello")
        self.assertEqual(self.sakinys3.pirmas_zodis(), "Print")

    def test_paskutinis_zodis(self):
        self.assertEqual(self.sakinys1.paskutinis_zodis(), "vakare?")
        self.assertEqual(self.sakinys2.paskutinis_zodis(), "world!")
        self.assertEqual(self.sakinys3.paskutinis_zodis(), "line()")

    def test_atbulai(self):
        self.assertEqual(self.sakinys1.atbulai(), "?erakav ak ut aK")
        self.assertEqual(self.sakinys2.atbulai(), "!dlrow olleH")
        self.assertEqual(self.sakinys3.atbulai(), ")(enil tnirP")

    def test_nuo_galo(self):
        self.assertEqual(self.sakinys1.nuo_galo(), "vakare? ka tu Ka")
        self.assertEqual(self.sakinys2.nuo_galo(), "world! Hello")
        self.assertEqual(self.sakinys3.nuo_galo(), "line() Print")

    def test_didziosiomis(self):
        self.assertEqual(self.sakinys1.didziosiomis(), "KA TU KA VAKARE?")
        self.assertEqual(self.sakinys2.didziosiomis(), "HELLO WORLD!")
        self.assertEqual(self.sakinys3.didziosiomis(), "PRINT LINE()")

    def test_mazosiomis(self):
        self.assertEqual(self.sakinys1.mazosiomis(), "ka tu ka vakare?")
        self.assertEqual(self.sakinys2.mazosiomis(), "hello world!")
        self.assertEqual(self.sakinys3.mazosiomis(), "print line()")

    def test_info(self):
        expect_first = "Žodžių kiekis: 4, Skaičių kiekis: 0, Didžiųjų raidžių: 1, Mažųjų raidžių: 11"
        expect_second = "Žodžių kiekis: 2, Skaičių kiekis: 0, Didžiųjų raidžių: 1, Mažųjų raidžių: 9"
        experct_third = "Žodžių kiekis: 2, Skaičių kiekis: 0, Didžiųjų raidžių: 1, Mažųjų raidžių: 8"
        self.assertEqual(self.sakinys1.info(), expect_first)
        self.assertEqual(self.sakinys2.info(), expect_second)
        self.assertEqual(self.sakinys3.info(), experct_third)
