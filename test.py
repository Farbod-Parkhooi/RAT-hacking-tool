def encode_string(s):
    encoded = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count > 2:
                encoded += s[i-1] + str(count)
            else:
                encoded += s[i-1] * count 
            count = 1

    if count > 2:
        encoded += s[-1] + str(count)
    else:
        encoded += s[-1] * count 
    return encoded


def decode_string(encoded):
    decoded = ""
    i = 0

    while i < len(encoded):
        char = encoded[i]
        count = 1
        if i + 1 < len(encoded) and encoded[i + 1].isdigit():
            count = int(encoded[i + 1])
            i += 1 
        decoded += char * count
        i += 1

    return decoded


original_string = "hello budddy im farbod and this is test of you?"
encoded_string = encode_string(original_string)
decoded_string = decode_string(encoded_string)

print("Original String:", original_string)
print("Encoded String:", encoded_string)
print("Decoded String:", decoded_string)
