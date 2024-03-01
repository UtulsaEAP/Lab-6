"""
Name: Dante Castilleja
Lab Time: Friday 3:00
"""
def food_input():
    user_input = input()
    tokens = user_input.split()
    #type you while  loop here
    while True :
        if 'quit' in user_input :
            break
        else :
            a, b = tokens
            print(f'Eating {b} {a} a day keeps you happy and healthy.')
            user_input = input()
            tokens = user_input.split()
if __name__ == "__main__":
    food_input()
