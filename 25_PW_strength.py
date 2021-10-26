def passwordValidator(password):
    # password = input("Please enter a password.")
        # very weak = only numbers, < 8 characters
        # weak = only letters, < 8 characters
        # strong = letters, 1 number, > 8 characters
        # very strong = letters, numbers, special characters, > 8 characters
    """
    input: one password 
    output: the password strength
    """
    if password.isalnum() == False and len(password) > 8:
        return 0; # very strong
    elif password.isnumeric() == True:
        return 3; # very weak
    elif password.isalpha() == True and len(password) < 8:
        return 2; # weak 
    elif password.isalnum() == True and len(password) > 8:
        return 1; # strong 

password = input("Please enter a password: ")
print(passwordValidator(password))



    # if password.isalnum() == False and len(password) > 8:
    #     print(f" The password '{password}' is a very strong password.")
    # elif password.isnumeric() == True:
    #     print(f" The password '{password}' is a very weak password.")
    # elif password.isalpha() == True and len(password) < 8:
    #     print(f" The password '{password}' is a weak password.")
    # elif password.isalnum() == True and len(password) > 8:
    #     print(f" The password '{password}' is a strong password.")