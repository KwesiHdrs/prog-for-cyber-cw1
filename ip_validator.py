# Return whether a dotted address has four valid IPv4 octets.
def validate_ip(ip_address):
    parts = ip_address.split('.')
    
    # An IPv4 address must contain exactly four octets.
    if len(parts) != 4:
        return False
    
    # Reject non-integers and values outside the valid octet range.
    for part in parts:
        try:
            num = int(part)
            if not (0 <= num <= 255):
                return False
        except ValueError:
            return False
    
    return True
