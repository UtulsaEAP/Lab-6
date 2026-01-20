
from madlib import food_input

error_msg = "Ensure your spacing and newline characters are appropriate."
def test_one(monkeypatch, capsys):
    # inputs = iter(["cars 99", "quit 0"])
    # monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    
    # food_input()
    # captured = capsys.readouterr()
    # all_outputs = captured.out
    # assert all(x in all_outputs for x in ["Eating 99 cars a day keeps you happy and healthy.\n"])
    inputs = ["cars 99"]

    foods = [pair.split(' ')[0] for pair in inputs]
    nums = [pair.split(' ')[1] for pair in inputs]
    
    all_outputs = food_input(foods,nums)
    # captured = capsys.readouterr()
    # all_outputs = captured.out
    assert all(x in all_outputs for x in ["Eating 99 cars a day keeps you happy and healthy.\n"]), error_msg
def test_two(monkeypatch, capsys):
    inputs = ["apples 5", "shoes 2"]
    foods = [pair.split(' ')[0] for pair in inputs]
    nums = [pair.split(' ')[1] for pair in inputs]
    
    all_outputs = food_input(foods,nums)
    # monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # food_input()
    # captured = capsys.readouterr()
    # all_outputs = captured.out
    assert all(x in all_outputs for x in ["Eating 5 apples a day keeps you happy and healthy.\n", "Eating 2 shoes a day keeps you happy and healthy.\n"]), error_msg

def test_three(monkeypatch, capsys):
    inputs = ["bananas 3"]
    foods = [pair.split(' ')[0] for pair in inputs]
    nums = [pair.split(' ')[1] for pair in inputs]
    
    all_outputs = food_input(foods,nums)
    # monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # food_input()
    # captured = capsys.readouterr()
    # all_outputs = captured.out
    assert all(x in all_outputs for x in ["Eating 3 bananas a day keeps you happy and healthy.\n"]), error_msg

def test_four(monkeypatch, capsys):
    inputs = ["oranges 7", "grapes 4"]
    foods = [pair.split(' ')[0] for pair in inputs]
    nums = [pair.split(' ')[1] for pair in inputs]
    
    all_outputs = food_input(foods,nums)
    # monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # food_input()
    # captured = capsys.readouterr()
    # all_outputs = captured.out
    assert all(x in all_outputs for x in ["Eating 7 oranges a day keeps you happy and healthy.\n", "Eating 4 grapes a day keeps you happy and healthy.\n"]), error_msg

