def validate_local_part(local_part):
    allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789!#$%&'*+-/=?^_`{|}~."

    assert local_part[0] != '.', ValueError("Local part cannot start with a dot.")
    assert local_part[len(local_part) - 1] != '.', ValueError("Local part cannot end with a dot.")
    assert '..' not in local_part, ValueError("Cannot have consecutive dots (..) in local_part.")

    for character in local_part:
        if character not in allowed_characters:
            raise ValueError("Unrecognized character.")


def validate_email(email):
    found_at = False
    found_dot = False

    for character in email:
        if character == '.':
            found_dot = True
        elif character == '@':
            found_at = True

    assert found_at is True, ValueError("Missing '@' in email.")
    assert found_dot is True, ValueError("Missing '.' in email.")

    email_split_acc_dom = email.split('@')
    local_part = email_split_acc_dom[0]
    domain = email_split_acc_dom[1]

    assert '.' in domain, ValueError('Cannot find domain.')

    allowed_domains_with_extensions = ['yahoo.com', 'gmail.com', 'abv.bg']

    validate_local_part(local_part)
    assert domain in allowed_domains_with_extensions, ValueError('Unrecognized domain / domain + extension.')


def validate_password(password):
    symbols = "abcdefghijklmnopqrstuvwxyz0123456789"
    special_symbols = "!”#$%&’()*+,-./:;<=>?@[]^_`{|}~\\"

    found_special_symbol = False
    found_capital_letter = False

    assert len(password) < 8, ValueError('Password length must be greater or equal to eight.')

    for elem in password:
        if elem in special_symbols:
            found_special_symbol = True
        elif elem.isupper():
            found_capital_letter = True
        elif elem not in symbols:
            raise ValueError('Unrecognized symbol.')

    assert found_special_symbol is True, ValueError('Password must contain at least one special symbol.')
    assert found_capital_letter is True, ValueError('Password must contain at least one capital letter.')
