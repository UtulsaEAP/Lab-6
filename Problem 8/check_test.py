from check import in_order

def test_passed():
    nums = [5, 6, 7, 8, 10]
    result = in_order(nums)
    assert result == True
    correct_result = True
    
def test_passed3():
    nums = [5, 6, 7, 8, 3]
    result = in_order(nums)
    assert result == False

def test_passed2():
    nums = [5, 5, 6, 6, 6, 7, 8, 10, 10, 10, 10]
    result = in_order(nums)
    assert result == True
