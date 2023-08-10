def validate_email(email):
    if email[0] == '@':
        return False

    count = email.count('@')
    if count != 1:
        return False

    endings = ['.it', '.com', '.africa']
    domain = email.split('@')[1]
    valid_domain = any(domain.endswith(ending) for ending in endings)

    return valid_domain


test = ['yila.ben@yahoo.com', 'sikiru@semicolon.africa', 'benson@yahoo.co']
for email in test:
    is_valid = validate_email(email)
    print(f'{email}: {"Valid email" if is_valid else "Invalid email"}')
