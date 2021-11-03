"""


"""


def dec_to_binary(number):
    the_binary_string = ''
    while number:
        if number % 2:
            the_binary_string = '1' + the_binary_string
        else:
            the_binary_string = '0' + the_binary_string
        
        number //= 2
    
    if not the_binary_string:
        return '0b0'
    else:
        return '0b' + the_binary_string


def dec_to_hex(number):
    """
        77d into hex
        77 mod 16 == 13 -> d
        4 mod 16 == 4 -> 4
        
        0x4d
    """
    the_hex_string = ''
    hd = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    while number:
        if number % 16 < 10:
            # use the regular digit
            the_hex_string = str(number % 16) + the_hex_string
        else:
            # use the special hex digits
            the_hex_string = hd[number % 16] + the_hex_string
        
        number //= 16
    
    if not the_hex_string:
        return '0x0'
    else:
        return '0x' + the_hex_string


for i in range(32):
    print(dec_to_hex(i), hex(i))

print(dec_to_hex(77))
