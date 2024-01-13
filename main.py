import random

key_rotation_number = random.randint(4, 9)
key_length = random.randint(5, 9)

valid_character_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '_', ' ']
valid_key_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
monolithic_character_list = ['n', 'x', 't', '_', 'B', 'R', 'o', 's', 'I', 'N', '4', '.', 'u', 'H', 'f', 'j', 'S', 'M', 'i', 'l', 'A', 'w', 'y', 'V', '6', '2', 'd', 'G', 'e', 'p', '8', '0', 'Z', 'k', 'W', 'z', 'T', 'Y', 'v', 'a', 'r', 'm', '7', 'K', '1', 'J', 'U', 'Q', ' ', 'c', 'E', 'q', '5', 'C', 'L', 'h', 'P', 'F', 'g', 'X', 'D', '3', '9', 'b', 'O']

def encrypt_key(password):
    monolithic_rotation_number = 0
    key = ""
    encrypted_key = ""
    
    for _ in range(0, key_length):
        present_key = random.choice(valid_key_list)
        key += present_key
        monolithic_rotation_number += int(valid_key_list.index(present_key))
    
    monolithic_rotation_number %= len(valid_character_list)
    key += str(key_rotation_number)
    
    j = 0
    for i in password:
        char_pos = valid_character_list.index(i)
        char_pos = (char_pos + monolithic_rotation_number + j) % len(valid_character_list)
        j += 1
        mono_pos = monolithic_character_list[char_pos]
        encrypted_key += str(mono_pos)
    
    encrypted_key = key + encrypted_key
    print("encrypted key ", encrypted_key)
    return encrypted_key

def decrypt_key(password):
    key_length = 0
    monolithic_rotation_number = 0
    decrypt_character_list = monolithic_character_list
    decrypted_key = ""
    
    for i in password:
        if i in number_list:
            break
        else:
            key_length += 1
    
    for i in range(0, key_length):
        present_key = password[i]
        monolithic_rotation_number += int(valid_key_list.index(present_key))
    
    monolithic_rotation_number %= len(valid_character_list)
    password_length = len(password) - key_length - 1
    j = 0
    
    for i in range(key_length + 1, len(password)):
        pos = password[i]
        char_pos = decrypt_character_list.index(pos) 
        rotation_value = (char_pos - monolithic_rotation_number - j) % len(decrypt_character_list)
        decrypted_key += valid_character_list[rotation_value]
        j += 1
    
    print("decrypted key ", decrypted_key)
    return decrypted_key


if __name__ == '__main__':
    decrypt_key(encrypt_key("hello world"))
