#DRY Principle

#Problem
class ValidatePersonalData:

    def validate_email(self, email:str):
        if email == None or email.isspace():
            return False
        
        regex = "^email_regex"
        return email.__contains__(regex)
    
    def validate_phone_number(self, phone_number:str):
        if phone_number == None or phone_number.isspace():
            return False
        
        regex = "^phone_regex"
        return phone_number.__contains__(regex)

    def validate_username(self, username:str):
        if username == None or username.isspace():
            return False
        
        regex = "^username_regex"
        return username.__contains__(regex)

if __name__ == '__main__':
    validator = ValidatePersonalData()
    validator.validate_username("username", "roy")


#Solution

def validate_email(email:str):
    regex = "^email_regex"
    return email.__contains__(regex)

def validate_phone_number(phone_number:str):
    regex = "^phone_regex"
    return phone_number.__contains__(regex)

def validate_username(username:str):
    regex = "^username_regex"
    return username.__contains__(regex) 

def validate(type:str, input:str):
    if input == None or input.isspace():
        return False
    
    validation_function = VALIDATION_RULES[type]

    if validation_function != None:
        return validation_function(input)
    
    raise Exception("Unkown validation type: " + type)

if __name__ == '__main__':
    VALIDATION_RULES = {}
    
    VALIDATION_RULES['email'] = validate_email
    VALIDATION_RULES['phone_number'] = validate_phone_number
    VALIDATION_RULES['username'] = validate_username

    validate("username", "roy")

    