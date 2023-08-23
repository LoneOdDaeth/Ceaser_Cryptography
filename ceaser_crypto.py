# it's basic cryptology tools. Just international letter!!

character = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ='.,!?1234567890" # if you want another character, you can add it

def generate_key(index):
    encrypt_key = {}
    cnt = 0
    for item in character:
        encrypt_key[item] = character[(cnt + index) % len(character)] # number of scrolls and generate the key
        cnt += 1
    return encrypt_key

def encrypt(encrypt_key, message):
    cipher = ""
    for item in message:
        if item in encrypt_key:
            cipher += encrypt_key[item]
        else:
            cipher += item
    return cipher

def decrypt(encrypt_key, cipher):
    decrypt_key = {v: k for k, v in encrypt_key.items()} # Create a decryption key by swapping values and keys in the encryption key dictionary.
    decrypted_message = ""
    
    for item in cipher:
        if item in decrypt_key:
            decrypted_message += decrypt_key[item]
        else:
            decrypted_message += item
    
    return decrypted_message

request = int(input("Do you want encrypted a message(please enter the 1) or decrypted a cipher(please enter the 2): "))

if request == 1:

    scroll_count = int(input("Enter the number of scrolls= "))
    generated_key = generate_key(scroll_count)
    print(generated_key)

    message = input("Enter the message: ")
    cipher = (encrypt(generated_key, message))
    print(cipher)

elif request == 2:

    scroll_count = int(input("Enter the number of scrolls: "))
    generated_key = generate_key(scroll_count)

    cipher = input("Enter the encrypted message: ")

    decrypted_message = decrypt(generated_key, cipher)
    print("Decrypted Message:", decrypted_message)