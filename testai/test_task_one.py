# pylint: disable= missing-docstring

import unittest
from task_one import (
    skaiciu_suma,
    saraso_suma,
    didziausias_skaicius,
    stringas_atbulai,
    info_apie_sakini,
    unique_only,
    ar_pirminis,
    isrikiuoti_nuo_galo,
    ar_keliamieji,
    patikrinti_data,
)


class TestTaskOne(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(
            skaiciu_suma(1, 2, 3),
            6,
        )
        self.assertEqual(
            skaiciu_suma(2, 3, 4),
            9,
        )
        self.assertEqual(
            skaiciu_suma(5, 6, 7),
            18,
        )

    def test_saraso_suma(self):
        self.assertEqual(saraso_suma([1, 2, 3, 4, 5]), 15)
        self.assertEqual(saraso_suma([6, 7, 8, 9, 10]), 40)
        self.assertEqual(saraso_suma([11, 12, 13, 14, 15]), 65)

    def test_didziausias_skaicius(self):
        self.assertEqual(didziausias_skaicius(5, 8, 789, 94, 78), 789)
        self.assertEqual(didziausias_skaicius(5, 8, 23, 94, 78), 94)
        self.assertEqual(didziausias_skaicius(5, 8, 123, 94, 78), 123)

    def test_stringas_atblulai(self):
        self.assertEqual(stringas_atbulai("Labas rytas"), "satyr sabaL")
        self.assertEqual(stringas_atbulai("Ka tu ka vakare?"), "?erakav ak ut aK")
        self.assertEqual(stringas_atbulai("Codeacademy"), "ymedacaedoC")

    def test_info_apie_sakini(self):
        expect_first = "Didžiosios: 1, mažosios: 9, skaičiai: 0"
        expect_second = "Didžiosios: 1, mažosios: 9, skaičiai: 4"
        experct_third = "Didžiosios: 0, mažosios: 10, skaičiai: 4"
        self.assertEqual(info_apie_sakini("Labas rytas"), expect_first)
        self.assertEqual(info_apie_sakini("Labas rytas 2023"), expect_second)
        self.assertEqual(info_apie_sakini("labas rytas 2023"), experct_third)

    def test_unique_only(self):
        self.assertEqual(unique_only(1, 2, 3, 3, 2), [1, 2, 3])
        self.assertEqual(unique_only(2, 3, 3, 4, 5), [2, 3, 4, 5])
        self.assertEqual(unique_only(3, 4, 3, 5, 5), [3, 4, 5])

    def test_ar_pirminis(self):
        self.assertTrue(ar_pirminis(3))
        self.assertTrue(ar_pirminis(11))
        self.assertTrue(ar_pirminis(13))

    def test_isrikiuoti_nuo_galo(self):
        self.assertEqual(isrikiuoti_nuo_galo("Vienas du trys"), "trys du Vienas")
        self.assertEqual(isrikiuoti_nuo_galo("Keturi  penki sesi"), "sesi penki Keturi")
        self.assertEqual(
            isrikiuoti_nuo_galo("Septyni astuoni devyni"), "devyni astuoni Septyni"
        )

    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji(1980))
        self.assertTrue(ar_keliamieji(2000))
        self.assertTrue(ar_keliamieji(2020))

    def test_patikrinti_data(self):
        self.assertEqual(
            patikrinti_data("2000-01-01"),
            "Praėjo metų: 23 /nPraėjo mėnesių: 280 /nPraėjo savaičių: 1218 /nPraėjo dienų: 8528",
        )
        self.assertEqual(
            patikrinti_data("2010-12-23"),
            "Praėjo metų: 12 /nPraėjo mėnesių: 148 /nPraėjo savaičių: 645 /nPraėjo dienų: 4519",
        )
        self.assertEqual(
            patikrinti_data("2023-05-01"),
            "Praėjo metų: 0 /nPraėjo mėnesių: 0 /nPraėjo savaičių: 1 /nPraėjo dienų: 7",
        )
