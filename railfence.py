def railfence():
    print("Rail Fence Cipher")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    if direction == 'encode':
        print(railfence_encode(text, shift))
    elif direction == 'decode':
        print(railfence_decode(text, shift))
    else:
        print("Please type 'encode' or 'decode'")

def railfence_encode(text, shift):
    railfence = [''] * shift
    row = 0
    direction = 1

    for char in text:
        railfence[row] += char
        if row == 0:
            direction = 1
        elif row == shift - 1:
            direction = -1
        row += direction

    return ''.join(railfence)

def railfence_decode(text, shift):
    railfence = [''] * shift
    row = 0
    direction = 1

    for _ in range(len(text)):
        railfence[row] += '*'

        if row == 0:
            direction = 1
        elif row == shift - 1:
            direction = -1
        row += direction

    index = 0
    for i in range(shift):
        for j in range(len(railfence[i])):
            railfence[i] = railfence[i][:j] + text[index] + railfence[i][j + 1:]
            index += 1

    row = 0
    direction = 1
    result = ''

    for _ in range(len(text)):
        result += railfence[row][0]
        railfence[row] = railfence[row][1:]

        if row == 0:
            direction = 1
        elif row == shift - 1:
            direction = -1
        row += direction

    return result

railfence()