"""
Name: Dante Castilleja
Lab Time: Friday 3:00
"""
def check_palindrome(user_input):
    pal = user_input [::-1]
    if pal == user_input :
        print(f'palindrome: {pal}')
    else :
        print(f'not a palindrome: {user_input}')
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)