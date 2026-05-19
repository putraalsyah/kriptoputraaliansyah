def vigenere_encrypt(plaintext, key):
    key = key.upper()
    key = ''.join(filter(str.isalpha, key))
    if not key:
        raise ValueError("Kunci harus mengandung setidaknya satu huruf.")

    steps = []
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            p = ord(char.upper()) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')
            c = (p + k) % 26
            enc_char = chr(c + ord('A'))
            steps.append({
                'char': char.upper(),
                'key_char': key[key_index % len(key)],
                'p_val': p,
                'k_val': k,
                'formula': f"({p} + {k}) mod 26 = {c}",
                'result': enc_char
            })
            ciphertext += enc_char
            key_index += 1
        else:
            steps.append({
                'char': char,
                'key_char': '-',
                'p_val': '-',
                'k_val': '-',
                'formula': 'Bukan huruf, tetap',
                'result': char
            })
            ciphertext += char

    return ciphertext.upper(), steps, key


def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    key = ''.join(filter(str.isalpha, key))
    if not key:
        raise ValueError("Kunci harus mengandung setidaknya satu huruf.")

    steps = []
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            c = ord(char.upper()) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')
            p = (c - k + 26) % 26
            dec_char = chr(p + ord('A'))
            steps.append({
                'char': char.upper(),
                'key_char': key[key_index % len(key)],
                'c_val': c,
                'k_val': k,
                'formula': f"({c} - {k} + 26) mod 26 = {p}",
                'result': dec_char
            })
            plaintext += dec_char
            key_index += 1
        else:
            steps.append({
                'char': char,
                'key_char': '-',
                'c_val': '-',
                'k_val': '-',
                'formula': 'Bukan huruf, tetap',
                'result': char
            })
            plaintext += char

    return plaintext.upper(), steps, key
