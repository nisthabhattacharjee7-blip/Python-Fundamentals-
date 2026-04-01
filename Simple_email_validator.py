def email_validator(email):
    if "@" in email and "." in email:
        return True 
    return False


email = input("Enter your email :")
if email_validator(email):
    print ("Valid email !")
else :
    print ("Invalid email !")    