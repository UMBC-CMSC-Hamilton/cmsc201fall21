def dec_to_binary(number):
    current_number = ''
    
    if not number:
        return '0b0'
    
    while number:
        if number % 2 == 0:
            current_number = '0' + current_number
        else:
            current_number = '1' + current_number
            
        number //= 2
        
    return '0b' + current_number


def dec_to_hex(number):
    current_number = ''
    
    if not number:
        return '0x0'
    
    hexits = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    
    while number:
        if number % 16 < 10:
            current_number = str(number % 16) + current_number
        else:
            current_number = hexits[number % 16] + current_number
        
        number //= 16
    
    return '0x' + current_number


for i in range(5000):
    print(i, dec_to_hex(i), hex(i))

