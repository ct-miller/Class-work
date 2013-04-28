
#The get_login_name function accepts a first name, a last name, and ID number as arguments.
#It returns a system login name.

def get_login_name(first, last, idnumber):
    #get the first three letters of the first name.
    #If the name is less than 3 characters, the slice
    #will return the entire first name.

    set1 = first[0:3]

    #Get the first three letters of the last name.
    # If the name is less than 3 characters, the
    # slice will return the entire last name.

    set2 = last[0:3]

    #Get the last three characters of the student ID.
    #If the ID numbers is less than 3 characters, the
    #slice will return the entire ID number.

    set3 = idnumber[-3:]

    #Put the sets of characters together.
    login_name = set1 + set2 + set3

    #Return the login name.
    return login_name

#The valid_password function accepts a password as and argument and return either true or false to
#indicate whether the password is valid. A valid password must be a at least 7 characters in length,
#have at least one uppercase letter, one lowercase letter, and one digit.

def valid_password(password):
    #set boolean variables to false.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Begin the validation. Start by testing teh password's length.
    if len(password) >= 7:
        correct_length = True

        #test each character and set the appropriate flag when a required
        #character is found.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

            #deterimie whether all of the requirements are met. If they are, set is_valid to ture.
            #Otherwise, set is_valid to False.
            if correct_length and has_uppercase and has_lowercase and has_digit:
                is_valid = True
            else:
                is_valid = False

            #Return the is_valid variable.
            return is_valid
