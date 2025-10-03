def move_index(index: int, move: int, max_index: int):
    if move > 0:
        for _ in range(move):
            if index != max_index:
                index += 1
            else:
                index = 0

    else:
        for _ in range(move * -1):
            if index != 0:
                index -= 1
            else:
                index = max_index

    return index


def cesar_encrypt(text: str, key: int):
    output = ""

    for letter in text:
        asci_val = ord(letter)

        letter = chr(move_index(asci_val - 97, key, 25) + 97) if letter != " " else " "
        output += letter

    return output
