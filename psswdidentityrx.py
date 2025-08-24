import hashlib
import json

# Function to produce hash as required
def produce_hash(string_to_hash):
    hashed_object = hashlib.sha256(string_to_hash.encode('latin-1'))
    return hashed_object.hexdigest()

user_wants_to_continue = True 
passfile_present = True # Tracks whether password file is available
list_of_passwords = [] # Holds list of common passwords
produce_hash_dict = {} # Stores Hash Values = Original string taken from list_of_passwords
final_json_content = [] # Stores all values for output to JSON showing found passwords

# Startup Message
print("Welcome")

# Main loop continues until user chooses to exit
while user_wants_to_continue:
    jsonFile = input("Enter your JSON path or [E] to exit: ")

    # Check for exit
    if jsonFile.lower() == "e":
        print("Bye")
        user_wants_to_continue = False
        break

    try:
        # Open, store information then close JSON file
        loadusers = open(jsonFile, 'rb')
        loaduserslist = json.load(loadusers)
        loadusers.close()
    except:
        print("Error loading file")
        continue

    # Prompt user for password file
    password_file_path = input("Enter the path to your password file: ")

    try: 
        passfile = open(password_file_path, 'r', encoding="latin-1")
    except:
        passfile_present = False

    # Check for success opening password file
    if passfile_present:
        list_of_passwords = passfile.read().splitlines()
        passfile.close()
        for string_to_hash in list_of_passwords:
            produce_hash_dict[produce_hash(string_to_hash)] = string_to_hash 
    else:
        print(f"{password_file_path} not present, closing.")
        user_wants_to_continue = False
        break

    for i in loaduserslist:
        found = False

        # Store user_name and user_password from stored file data
        try:
            username = i["user_name"]
            password_hash = i["user_password"]
        except:
            print("File does not have correct data formatting")
            break

        # Check if hashed password is in the stored dictionary of hashed passwords
        try:
            password = produce_hash_dict[password_hash]
            found = True
        except:
            password = ""

        # Inform user if a password was found or not
        if found:
            print(f"{username} password found.")           
        else: 
            print(f"{username} password was not found.")

        # Create a dictionary item then add it to a permanent list, with username, password if found, and password status
        dict_of_content = {"username": username, "password": password, "password_found": found}
        final_json_content.append(dict_of_content)

    # Save data, overwriting previous existing instance of file
    data = open("password_finder.json", "w")
    json.dump(final_json_content, data, indent=1)
    data.close()