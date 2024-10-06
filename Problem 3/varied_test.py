from varied import process_input

def test_case_1():
    input_string = "14.25 25 0 5.75"
    max_value, average_value = process_input(input_string)
    assert max_value == 25.00
    assert average_value == 11.25

def test_case_2():
    input_string = "2 2 2 2 12 0 8 4"
    max_value, average_value = process_input(input_string)
    assert max_value == 12.00
    assert average_value == 4.00

def test_case_3():
    input_string = "5.25 1 2"
    max_value, average_value = process_input(input_string)
    assert max_value == 5.25
    assert average_value == 2.75

def test_case_4():
    input_string = "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    max_value, average_value = process_input(input_string)
    assert max_value == 0.00
    assert average_value == 0.00
