# pylint: disable= missing-docstring
from typing import List


# 1. Gražinti trijų paduotų skaičių sumą.
def skaiciu_suma(*kiek_tik_nori):
    return sum(kiek_tik_nori)


# 2. Gražintų paduoto sąrašo iš skaičių, sumą.
def saraso_suma(sarasas):
    return sum(sarasas)


# 3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
def didziausias_skaicius(*args):
    return max(args)


# 4. Gražintų paduotą stringą atbulai.
def stringas_atbulai(stringas):
    return stringas[::-1]


# 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
def info_apie_sakini(stringas) -> str:
    didziosios = 0
    mazosios = 0
    skaiciai = 0
    for simbolis in stringas:
        if simbolis.isupper():
            didziosios += 1
        if simbolis.islower():
            mazosios += 1
        if simbolis.isnumeric():
            skaiciai += 1
    return f"Didžiosios: {didziosios}, mažosios: {mazosios}, skaičiai: {skaiciai}"


# 6. Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
def unique_only(*args) -> List:
    return list(set(args))


# 7. Gražintų, ar paduotas skaičius yra pirminis.

# n = int(input("Įveskite skaičių "))


def ar_pirminis(skaicius):
    if skaicius > 1:
        for num in range(2, skaicius):
            if skaicius % num == 0:
                return False
        return True
    return False


# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
def isrikiuoti_nuo_galo(sakinys):
    zodziai = sakinys.split()[::-1]
    atvirksciai = " ".join(zodziai)
    return atvirksciai


# 9. Gražina, ar paduoti metai yra keliamieji, ar ne.
import calendar


def ar_keliamieji(metai):
    return calendar.isleap(metai)


# 10. Gražina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.
import datetime


def patikrinti_data(sukaktis):
    ivesta_data = datetime.datetime.strptime(sukaktis, "%Y-%m-%d")
    now = datetime.datetime.now()
    skirtumas = now - ivesta_data
    skirtumas_metai = skirtumas.days // 365
    skirtumas_men = int(skirtumas.days / 365 * 12)
    skirtumas_sav = skirtumas.days // 7
    skirtumas_dienos = skirtumas.days
    # skirtumas_val = skirtumas.total_seconds() / 3600
    # skirtumas_min = skirtumas.total_seconds() / 60
    # skirtumas_sec = skirtumas.total_seconds()
    return f"Praėjo metų: {skirtumas_metai} /nPraėjo mėnesių: {skirtumas_men} /nPraėjo savaičių: {skirtumas_sav} /nPraėjo dienų: {skirtumas_dienos}"
    # return f"Praėjo metų: {skirtumas_metai} /nPraėjo mėnesių: {skirtumas_men} /nPraėjo savaičių: {skirtumas_sav} /nPraėjo dienų: {skirtumas_dienos} /nPraėjo valandų: {skirtumas_val} /nPraėjo minučių: {skirtumas_min} /nPraėjo sekundžių: {skirtumas_sec}"
