def caesar_encrypt(plaintext, shift):
    steps = []
    ciphertext = ""
    shift = shift % 26

    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            p = ord(char.upper()) - ord('A')
            c = (p + shift) % 26
            enc_char = chr(c + ord('A'))
            steps.append({
                'char': char.upper(),
                'p_val': p,
                'formula': f"({p} + {shift}) mod 26 = {c}",
                'result': enc_char
            })
            ciphertext += enc_char
        else:
            steps.append({
                'char': char,
                'p_val': '-',
                'formula': 'Bukan huruf, tetap',
                'result': char
            })
            ciphertext += char

    return ciphertext.upper(), steps


def caesar_decrypt(ciphertext, shift):
    steps = []
    plaintext = ""
    shift = shift % 26

    for char in ciphertext:
        if char.isalpha():
            c = ord(char.upper()) - ord('A')
            p = (c - shift + 26) % 26
            dec_char = chr(p + ord('A'))
            steps.append({
                'char': char.upper(),
                'c_val': c,
                'formula': f"({c} - {shift} + 26) mod 26 = {p}",
                'result': dec_char
            })
            plaintext += dec_char
        else:
            steps.append({
                'char': char,
                'c_val': '-',
                'formula': 'Bukan huruf, tetap',
                'result': char
            })
            plaintext += char

    return plaintext.upper(), steps
