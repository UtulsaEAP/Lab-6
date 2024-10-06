
from palindrome import check_palindrome

def test_one():
    outputs = check_palindrome("sees")
    assert outputs == "palindrome: sees"

def test_two():
    outputs = check_palindrome("never odd or even")
    assert outputs == "palindrome: never odd or even"

def test_three():
    outputs = check_palindrome("dr awkward")
    assert outputs == "palindrome: dr awkward"

def test_four():
    outputs = check_palindrome("evil is alive")
    assert outputs == "not a palindrome: evil is alive"

def test_five():
    outputs = check_palindrome("no lemon no melon")
    assert outputs == "palindrome: no lemon no melon"

def test_six():
    outputs = check_palindrome("taco cat")
    assert outputs == "palindrome: taco cat"

def test_seven():
    outputs = check_palindrome("seems")
    assert outputs == "not a palindrome: seems"

def test_palindrome():
    outputs = check_palindrome("bob")
    assert outputs == "palindrome: bob"

def test_not_palindrome():
    outputs = check_palindrome("statistics")
    assert outputs == "not a palindrome: statistics"
