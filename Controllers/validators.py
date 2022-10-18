def phone_number_validator(phone_number):
    if len(phone_number) == 10 and phone_number[0] == '0':
        if phone_number[1] == '7' or phone_number[1] == '1':
            is_valid = True
        else:
            is_valid = False
    else:
        is_valid = False
    return is_valid


def email_validator(email):
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        is_valid = True
    else:
        is_valid = False
    return is_valid
