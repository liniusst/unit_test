# pylint: disable= missing-docstring


def kmi(weight: float, height: float) -> float:
    if weight < 25:
        raise ValueError("per mazas svoris")
    if weight > 210:
        raise ValueError("biski per didelis svoris")
    if height < 1:
        raise ValueError("trumpas ugis")
    if height > 2.20:
        raise ValueError("per daug didelis zmogus")
    return weight / (height**2)
