
from madlib import food_input

def test_one(monkeypatch, capsys):
    inputs = iter(["cars 99", "quit 0"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    food_input()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["Eating 99 cars a day keeps you happy and healthy.\n"])

def test_two(monkeypatch, capsys):
    inputs = iter(["apples 5", "shoes 2", "quit 0"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    food_input()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["Eating 5 apples a day keeps you happy and healthy.\n", "Eating 2 shoes a day keeps you happy and healthy.\n"])

def test_three(monkeypatch, capsys):
    inputs = iter(["bananas 3", "quit 0"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    food_input()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["Eating 3 bananas a day keeps you happy and healthy.\n"])

def test_four(monkeypatch, capsys):
    inputs = iter(["oranges 7", "grapes 4", "quit 0"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    food_input()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ["Eating 7 oranges a day keeps you happy and healthy.\n", "Eating 4 grapes a day keeps you happy and healthy.\n"])

