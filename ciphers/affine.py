from math import gcd

VALID_A = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(plaintext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError(f"Nilai 'a' = {a} tidak valid. 'a' harus relatif prima dengan 26. Nilai yang valid: {VALID_A}")

    steps = []
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            p = ord(char.upper()) - ord('A')
            c = (a * p + b) % 26
            enc_char = chr(c + ord('A'))
            steps.append({
                'char': char.upper(),
                'p_val': p,
                'formula': f"({a} × {p} + {b}) mod 26 = ({a*p + b}) mod 26 = {c}",
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


def affine_decrypt(ciphertext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError(f"Nilai 'a' = {a} tidak valid. 'a' harus relatif prima dengan 26. Nilai yang valid: {VALID_A}")

    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError(f"Invers modular dari a={a} tidak ditemukan.")

    steps = []
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            c = ord(char.upper()) - ord('A')
            p = (a_inv * (c - b + 26)) % 26
            dec_char = chr(p + ord('A'))
            steps.append({
                'char': char.upper(),
                'c_val': c,
                'formula': f"{a_inv} × ({c} - {b} + 26) mod 26 = {a_inv} × {(c - b + 26) % 26} mod 26 = {p}",
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

    return plaintext.upper(), steps, a_inv
