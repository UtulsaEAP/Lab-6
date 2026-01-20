
from palindrome import check_palindrome

template_error = "Verify the output format in the readme"
space_error = "Remove all spaces before verifying a phrase"
def test_one():
    outputs = check_palindrome("sees")
    assert outputs == "palindrome: sees", template_error

def test_two():
    outputs = check_palindrome("never odd or even")
    assert outputs == "palindrome: never odd or even", space_error

def test_three():
    outputs = check_palindrome("dr awkward")
    assert outputs == "palindrome: dr awkward", space_error

def test_four():
    outputs = check_palindrome("evil is alive")
    assert outputs == "not a palindrome: evil is alive", space_error

def test_five():
    outputs = check_palindrome("no lemon no melon")
    assert outputs == "palindrome: no lemon no melon", space_error

def test_six():
    outputs = check_palindrome("taco cat")
    assert outputs == "palindrome: taco cat", space_error

def test_seven():
    outputs = check_palindrome("seems")
    assert outputs == "not a palindrome: seems", template_error

def test_palindrome():
    outputs = check_palindrome("bob")
    assert outputs == "palindrome: bob", template_error

def test_not_palindrome():
    outputs = check_palindrome("statistics")
    assert outputs == "not a palindrome: statistics", template_error
