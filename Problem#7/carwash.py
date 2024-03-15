"""
Name: Dante Castilleja
Lab Time: Friday 3:00
"""
def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = 0
    service = []
    if service_choice1 == '-' and service_choice2 == '-' :
        print('ZyCar Wash\nBase car wash - $10\n-----\nTotal price - $10')
    elif service_choice2 == '-' :
        print(f'ZyCar Wash\nBase car wash - $10\n{service_choice1} - ${services[service_choice1]}\n-----\nTotal price - ${base_wash + services[service_choice1]}')
    else :
        print(f'Zycar Wash\nBase car wash - $10\n{service_choice1} - ${services[service_choice1]}\n{service_choice2} - ${services[service_choice2]}\n-----\nTotal price - ${base_wash + services[service_choice1] + services[service_choice2]}')

    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
