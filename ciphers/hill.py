import numpy as np
from math import gcd

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inverse(matrix, mod):
    n = len(matrix)
    det = int(round(np.linalg.det(matrix))) % mod
    det = det % mod
    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        raise ValueError(f"Matriks tidak memiliki invers modular (det={det} tidak relatif prima dengan {mod}).")

    if n == 2:
        adj = np.array([
            [matrix[1][1], -matrix[0][1]],
            [-matrix[1][0], matrix[0][0]]
        ], dtype=int)
    elif n == 3:
        adj = np.zeros((3, 3), dtype=int)
        for i in range(3):
            for j in range(3):
                minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                cofactor = int(round(np.linalg.det(minor))) * ((-1) ** (i + j))
                adj[j][i] = cofactor
    else:
        raise ValueError("Ukuran matriks tidak didukung (hanya 2x2 atau 3x3).")

    inv = (det_inv * adj) % mod
    return inv.tolist()

def prepare_text(text, n):
    text = ''.join(filter(str.isalpha, text.upper()))
    while len(text) % n != 0:
        text += 'X'
    return text

def hill_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    key = np.array(key_matrix, dtype=int)

    det = int(round(np.linalg.det(key))) % 26
    if gcd(det % 26, 26) != 1:
        raise ValueError(f"Determinan matriks kunci (det={det % 26}) tidak relatif prima dengan 26. Pilih matriks lain.")

    prepared = prepare_text(plaintext, n)
    ciphertext = ""
    steps = []

    for i in range(0, len(prepared), n):
        block = [ord(c) - ord('A') for c in prepared[i:i+n]]
        block_vec = np.array(block)
        result_vec = np.dot(key, block_vec) % 26
        result_chars = [chr(int(v) + ord('A')) for v in result_vec]

        calc_detail = []
        for row_idx in range(n):
            row = key[row_idx]
            terms = " + ".join([f"{row[j]}×{block[j]}" for j in range(n)])
            total = sum(row[j] * block[j] for j in range(n))
            mod_val = int(result_vec[row_idx])
            calc_detail.append(f"({terms}) mod 26 = {total} mod 26 = {mod_val} → {result_chars[row_idx]}")

        steps.append({
            'block_text': prepared[i:i+n],
            'block_nums': block,
            'result_nums': [int(v) for v in result_vec],
            'result_chars': result_chars,
            'calc_detail': calc_detail
        })
        ciphertext += ''.join(result_chars)

    return ciphertext, steps, prepared

def hill_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    key = np.array(key_matrix, dtype=int)

    inv_key = matrix_mod_inverse(key, 26)
    inv_key_np = np.array(inv_key, dtype=int)

    prepared = prepare_text(ciphertext, n)
    plaintext = ""
    steps = []

    for i in range(0, len(prepared), n):
        block = [ord(c) - ord('A') for c in prepared[i:i+n]]
        block_vec = np.array(block)
        result_vec = np.dot(inv_key_np, block_vec) % 26
        result_chars = [chr(int(v) + ord('A')) for v in result_vec]

        calc_detail = []
        for row_idx in range(n):
            row = inv_key_np[row_idx]
            terms = " + ".join([f"{row[j]}×{block[j]}" for j in range(n)])
            total = sum(int(row[j]) * block[j] for j in range(n))
            mod_val = int(result_vec[row_idx])
            calc_detail.append(f"({terms}) mod 26 = {total} mod 26 = {mod_val} → {result_chars[row_idx]}")

        steps.append({
            'block_text': prepared[i:i+n],
            'block_nums': block,
            'result_nums': [int(v) for v in result_vec],
            'result_chars': result_chars,
            'calc_detail': calc_detail
        })
        plaintext += ''.join(result_chars)

    return plaintext, steps, prepared, inv_key
