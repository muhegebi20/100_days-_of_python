alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(original_text, shift, direction):
    message = ""
    if direction == "decode":
        shift*=-1
    for l in original_text:
        if l not in alphabet:
            message+=l
            continue
        ind = alphabet.index(l) + shift
        ind %= len(alphabet)
        message+=alphabet[ind]
    print(f"here is the {direction}d message: {message}")

play = True
while play:
    ask = input("do you want to play, type yes/no: ").lower()
    if ask == "no":
        break;
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower();
    text = input("Type your message:\n").lower();
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)