from contactlist import process_user_contacts

def test_contact_found():
    inputs = ['Joe','123-5432','Linda','983-4123','Frank','867-5309']
    contact_input = "Frank"
    assert process_user_contacts(inputs,contact_input) == "867-5309"
    
def test_contact_not_found():
    inputs = ['Jasmin','312-3145','Scooby-Doo','093-1212']
    contact_input = "Jasmin"
    assert process_user_contacts(inputs,contact_input) == "312-3145"

def test_additional_case():
    inputs = ['Mo','391-0993','Rachel','019-1265','Ruby','010-8712','Steve','312-3318','Maria','871-0091']
    contact_input = "Rachel"
    assert process_user_contacts(inputs,contact_input) == "019-1265"
    
def test_four():
    inputs = ['Sally','190-1214','Sue','119-6442']
    contact_input = "Sue"
    assert process_user_contacts(inputs,contact_input) == "119-6442"
