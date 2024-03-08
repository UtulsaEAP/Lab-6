"""
Name: Dante Castilleja
Lab Time: Friday 3:00
"""
def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    input_list = [num for num in integer_list if min_val <= num <= max_val]
    print(','.join(map(str, input_list)) + ',')
if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = list(map(int, user_input.split()))

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = list(map(int, user_input.split()))

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)