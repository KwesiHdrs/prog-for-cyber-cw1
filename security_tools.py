# Check that a password contains the required length and character types.
def is_strong_password(password):
    import re
    
    # Each rule must match for the password to pass validation.
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    
    return bool(re.search("[!@#$%^&*(),.?\":{}|<>]", password))

# Validate an IPv4 address by checking its four numeric octets.
def validate_ip(ip_address):
    parts = ip_address.split('.')
    
    # IPv4 addresses contain exactly four dot-separated parts.
    if len(parts) != 4:
        return False
    
    # Each octet must be an integer in the inclusive range 0-255.
    for part in parts:
        try:
            num = int(part)
            if not (0 <= num <= 255):
                return False
        except ValueError:
            return False
    
    return True

# Build a password by randomly selecting characters from the configured pool.
def generate_strong_password(length=12):
    import random
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
    return ''.join(random.choice(chars) for _ in range(length))
