import functions

def test_average():

    actual_result = functions.average([1, 3, 4, 5, 2])
    expected_result= 3.0
    assert actual_result == expected_result

def test_average_float():
    actual_result = functions.average([1.5, 3.5, 4.5, 5.5, 2.5])
    expected_result = 3.5
    assert actual_result == expected_result

def test_kredit_payment():

    actual_result = functions.kredit_payment(1650, 12)
    expected_result= 19800
    assert actual_result == expected_result

def test_sum_all():

    actual_result = functions.sum_all(33,678)
    expected_result= '711 км2'
    assert actual_result == expected_result

def test_remainder():

    actual_result = functions.remainder(344,34)
    expected_result = 4
    assert actual_result == expected_result

def test_remainder_minus():

    actual_result = functions.remainder(-344,-34)
    expected_result= -4
    assert actual_result == expected_result

def test_multiplication_table():

    actual_result = functions.multiplication_table(4)
    expected_result= [4, 8, 12, 16, 20, 24]
    assert actual_result == expected_result
    assert isinstance(actual_result, list), f'Actual result {actual_result} should be a list'

def test_triangle_area():

    actual_result = functions.triangle_area(3, 4, 5)
    expected_result = 6.0
    assert actual_result == expected_result

def test_is_anagram():

    actual_result = functions.is_anagram("art", "tra")
    expected_result = True
    assert actual_result == expected_result

def test_is_not_anagram():

    actual_result = functions.is_anagram('marry', 'ball')
    expected_result = False
    assert actual_result == expected_result

def test_filter_even_numbers():

    actual_result = functions.filter_even_numbers([1, 2, 3, 4, 5])
    expected_result = [2, 4]
    assert actual_result == expected_result

def test_filter_even_numbers_empty():
    actual_result = functions.filter_even_numbers([1, 3, 5, 7])
    expected_result = []
    assert actual_result == expected_result


def test_convert_to_24_hour():
    actual_result = functions.convert_to_24_hour('09:09 pm')
    expected_result = '21:09'
    assert actual_result == expected_result





