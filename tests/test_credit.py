from credit import calculate_risk


# --- Partie A : cas normaux ---

def test_high_risk():
    result = calculate_risk(1000, 700, 30)
    assert result == "HIGH"


def test_medium_risk():
    result = calculate_risk(1000, 400, 30)
    assert result == "MEDIUM"


def test_low_risk():
    result = calculate_risk(1000, 100, 30)
    assert result == "LOW"


# --- Partie B : cas limites ---

def test_income_zero():
    result = calculate_risk(0, 100, 30)
    assert result == -1


def test_income_negative():
    result = calculate_risk(-500, 100, 30)
    assert result == -1


def test_debt_zero():
    result = calculate_risk(1000, 0, 30)
    assert result == "LOW"


def test_ratio_exactly_0_3():
    # ratio = 300/1000 = 0.3 → pas > 0.3 → LOW
    result = calculate_risk(1000, 300, 30)
    assert result == "LOW"


def test_ratio_exactly_0_6():
    # ratio = 600/1000 = 0.6 → pas > 0.6, mais > 0.3 → MEDIUM
    result = calculate_risk(1000, 600, 30)
    assert result == "MEDIUM"
