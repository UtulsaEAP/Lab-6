"""
Name: Dante Castilleja
Lab Time: Friday 3:00
"""
def process_user_contacts(user_input):
    user_contacts = {}
    tokens = user_input.split(',')

    # Put word pairs into a dictionary
    for num in range(0, len(tokens)-1, 2) :
        user_contacts[tokens[num].strip()] = tokens[num + 1].strip()
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ").strip()
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)