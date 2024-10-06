from elementsrange import filter_and_print_range

def test_first_input(capsys):
    input = [25, 51, 0, 200, 33]
    min_val, max_val = 0, 50
    filter_and_print_range(input, min_val, max_val)
    output = capsys.readouterr().out
    assert output == "25,0,33,"

def test_second_input(capsys):
    input = [100, 200, 150, 75]
    min_val, max_val = 75, 100
    filter_and_print_range(input, min_val, max_val)
    output = capsys.readouterr().out
    assert output == "100,75,"

def test_three_input(capsys):
    input = [1,2,3]
    min_val, max_val = 0,5
    filter_and_print_range(input, min_val, max_val)
    output = capsys.readouterr().out
    assert output == "1,2,3,"

def test_four_input(capsys):
    input = [1,2,3,4,5]
    min_val, max_val = 0,5
    filter_and_print_range(input, min_val, max_val)
    output = capsys.readouterr().out
    assert output == "1,2,3,4,5,"

def test_five_input(capsys):
    input = [1,2,3,4,5]
    min_val, max_val = 0,3
    filter_and_print_range(input, min_val, max_val)
    output = capsys.readouterr().out
    assert output == "1,2,3,"
    
def test_six_input(capsys):
    input = [1,2,3,4,5]
    min_val, max_val = 0,1
    filter_and_print_range(input, min_val, max_val)
    output = capsys.readouterr().out
    assert output == "1,"
