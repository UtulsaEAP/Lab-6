"""
Name: Dante Castilleja
Lab Time: Friday 3:00
"""
def check_palindrome(user_input):
    one = user_input.replace(" ", "")
    pal = one [::-1]
    if pal == one :
        print(f'palindrome: {user_input}')
    else :
        print(f'not a palindrome: {user_input}')
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)