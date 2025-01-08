alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower();
text = input("Type your message:\n").lower();
shift = int(input("Type the shift number:\n"))

def encrypt(original_txt, shift):
    encoded = ""
    for l in original_txt:
        if l == ' ':
            continue;
        ind = alphabet.index(l) + shift
        if ind > len(alphabet)-1:
            encoded+= alphabet[ind%len(alphabet)]
        else:
            encoded+=alphabet[ind]
    return encoded;


def decrypt(encoded_message, shift):
    message = ""
    for l in encoded_message:
        ind = alphabet.index(l) - shift
        if ind < 0:
            message += alphabet[ind+len(alphabet)]
        else:
            message += alphabet[ind]
    return message;



if direction == "encode":
    crypto_message = encrypt(text, shift)
    print(crypto_message)
else:
    decoded = decrypt(encoded_message=text, shift=shift)
    print(decoded)