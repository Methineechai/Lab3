import Lab2.bmi as BMI

def test_calc_bmi_function_normal_weight():
    expected = 0
    results = BMI.calculate_bmi(height= 1.84, weight=64)
    assert (results == expected)


def test_calc_bmi_function_over_weight():
    expected = 1
    results = BMI.calculate_bmi(height= 1.84, weight=94)
    assert (results == expected)


def test_calc_bmi_function_under_weight():
    expected = -1
    results = BMI.calculate_bmi(height= 1.84, weight=34)
    assert (results == expected)

