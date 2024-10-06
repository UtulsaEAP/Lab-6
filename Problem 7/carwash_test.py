# Import the function from the main module
from carwash import calculate_car_wash_price

def test_one():
    input_one = "-"
    input_two = "-"
    expected_output = "ZyCar Wash\nBase car wash - $10\n-----\nTotal price: $10"
    assert calculate_car_wash_price(input_one, input_two) == expected_output

def test_two():
    input_one = "Tire shine"
    input_two = "Wax"
    expected_output = "ZyCar Wash\nBase car wash - $10\nTire shine - $2\nWax - $3\n-----\nTotal price: $15"
    assert calculate_car_wash_price(input_one, input_two) == expected_output
    
def test_three():
    input_one = "Rain repellent"
    input_two = "-"
    expected_output = "ZyCar Wash\nBase car wash - $10\nRain repellent - $2\n-----\nTotal price: $12"
    assert calculate_car_wash_price(input_one, input_two) == expected_output

def test_four():
    input_one = "Air freshener"
    input_two = "Vacuum"
    expected_output = "ZyCar Wash\nBase car wash - $10\nAir freshener - $1\nVacuum - $5\n-----\nTotal price: $16"
    assert calculate_car_wash_price(input_one, input_two) == expected_output
