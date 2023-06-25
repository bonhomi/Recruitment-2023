Z = []
k = []
message = input("Enter input: ")

def reverse_fuNction(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isnumeric():
            result += chr(ord(char) + 1)
        elif char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr(ord(char) ^ 1)
    return result

def reverse_FuNction(input):
    for i in range(len(input)):
        if i < 11:
            Z.append(chr(ord(input[i]) - (i + 5)))
        else:
            Z.append(chr(ord(input[i]) - 4))
    return ''.join(Z)

def reverse_Function(input):
    st = []
    for i in range(len(input)):
        st.append(chr(ord(input[i]) ^ 1))
    return ''.join(st)

k = reverse_fuNction(reverse_Function(reverse_FuNction(message)), 4)
print(k)