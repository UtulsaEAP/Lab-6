"""
Name: Dante Castilleja
Lab Time: Friday 3:00
"""
def process_and_print(input_string):
      # Split into separate strings
  input_string = list(map(int, user_input.split()))
    # Convert strings to integers and filter out negative values
  input_data = [num for num in input_string if num < 0]
    # Sort integers in reverse order
  input_data.sort(reverse= True)
    # Print sorted integers
  print(*input_data)
if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
