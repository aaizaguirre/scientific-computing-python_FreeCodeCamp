"""
Password Generator Script
Este módulo genera contraseñas seguras cumpliendo las siguientes restricciones:
    1. Longitud personalizable.
    2. Cantidad mínima de números, caracteres especiales, mayúsculas y minúsculas.
"""
import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Genera una contraseña segura de longitud especificada.
    Args:
        - length (int): longitud de la contraseña.
        - nums (int): cantidad mínima de dígitos.
        - special_chars (int): cantidad mínima de caracteres especiales.
        - uppercase (int): cantidad mínima de letras mayúsculas.
        - lowercase (int): cantidad mínima de letras minúsculas.
    Return:
        - str: contraseña generada que cumple con las restricciones.
    """

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    return password

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
