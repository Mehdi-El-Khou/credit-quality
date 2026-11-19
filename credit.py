def calculate_risk(income, debt, age=None):
    """Calcule le niveau de risque crédit à partir du revenu et de la dette.

    Args:
        income: revenu (doit être > 0)
        debt: dette
        age: âge du client (réservé pour une évolution future)

    Returns:
        "HIGH", "MEDIUM", "LOW", ou -1 si le revenu est invalide
    """
    if income <= 0:
        return -1

    ratio = debt / income

    if ratio > 0.6:
        return "HIGH"
    elif ratio > 0.3:
        return "MEDIUM"
    else:
        return "LOW"
