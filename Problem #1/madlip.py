def food_input():
    user_input = input()
    tokens = user_input.split()
    #type you while  loop here
    while True :
        if 'quit' in user_input :
            break
        else :
            return
if __name__ == "__main__":
    food_input()
