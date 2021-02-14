#The input should be structured as follows:
#The name of encryption, the key, and the 
#encrypted message in binary should be in 
#order and separated by a colon.
#Save to a .txt file in the same directory as this .py

DIFFERENT_CHAR_BYTE = 256
CAESAR = 'caesar'
VIGENERE = 'vigenere'
RSA = 'rsa'


def to_binary(num):
    binary_num = ''
    while num >= 1:
        binary_num += str(num % 2)
        num //= 2

    return int(binary_num[::-1])


def to_decimal(num):
    decimal_num = 0
    digits = list(map(int, list(num)))[::-1]
    exponents = range(len(digits) - 1, -1, -1)

    for exponent in exponents:
        if digits[exponent] == 1:
            decimal_num += 2 ** exponent

    return decimal_num


def binary_to_ascii(binary_message):
    ascii_message = ''

    for byte in binary_message:
        decimal_value = to_decimal(byte)
        ascii_message += chr(decimal_value)

    return ascii_message


def caesar_decrypt(message, key):
    decrypted_msg = ''

    for character in message:
        binary_msg = ord(character)
        decrypted_msg += chr(((binary_msg - int(key)) % DIFFERENT_CHAR_BYTE))

    return decrypted_msg


def vigenere_decrypt(message, key):
    decrypted_msg = ''
    match_msg_length = int(len(message) / len(key)) + 1
    key = key * match_msg_length

    for character, symbol in zip(message, key):
        char_key = ord(symbol)
        decrypted_msg += caesar_decrypt(character, char_key)

    return decrypted_msg


def rsa_decrypt(message, key):
    decrypted_msg = ''
    message = message.split()
    key = key.split(',')
    key_modulo = int(key[0][1::])
    key_decrypt = int(key[1][:len(key[1]) - 1:])

    for encrypted_char in message:
        decimal_msg = to_decimal(encrypted_char)
        decrypted_char = (decimal_msg ** key_decrypt) % key_modulo
        decrypted_char = binary_to_ascii([str(to_binary(decrypted_char))])
        decrypted_msg += decrypted_char

    return decrypted_msg


def decrypt_line(line):
    line = line.split(':')
    encryption_type = line[0]
    key = line[1]
    message = line[2]

    if encryption_type == RSA:
        print('%s' % rsa_decrypt(message, key))

    message = binary_to_ascii(message.split())

    if encryption_type == CAESAR:
        print('%s' % caesar_decrypt(message, key))
    elif encryption_type == VIGENERE:
        print('%s' % vigenere_decrypt(message, key))


def start(file_name):
    lines = open(file_name).read().splitlines()
    for line in lines:
        decrypt_line(line)


#start
file_name = input("Enter the input file name: ")
start(file_name)
