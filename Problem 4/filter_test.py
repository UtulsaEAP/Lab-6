
from filter import process_and_print

def test_positive_input():
    input = "10 -7 4 -39 -6 12 -2"
    output = process_and_print(input)
    assert output == "-2 -6 -7 -39 "

def test_negative_input():
    input = "-25"
    output = process_and_print(input)
    assert output == "-25 "

def test_another_negative_input():
    input = "-3 -99 -3 -1 -27"
    output = process_and_print(input)
    assert output == "-1 -3 -3 -27 -99 "
    
def test_four():
    input = "1 7 2 88 -5 6"
    output = process_and_print(input)
    assert output == "-5 "

def test_five():
    input = "0 -8 -23 4 -9"
    output = process_and_print(input)
    assert output == "-8 -9 -23 "
