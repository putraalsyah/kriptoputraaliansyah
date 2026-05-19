def generate_playfair_matrix(key):
    key = key.upper().replace('J', 'I')
    seen = []
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.append(ch)
    for ch in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if ch not in seen:
            seen.append(ch)
    matrix = [seen[i*5:(i+1)*5] for i in range(5)]
    return matrix

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if val == char:
                return r, c
    return None, None

def prepare_plaintext(text):
    text = text.upper().replace('J', 'I')
    text = ''.join(filter(str.isalpha, text))
    prepared = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i+1]
            if a == b:
                prepared.append((a, 'X'))
                i += 1
            else:
                prepared.append((a, b))
                i += 2
        else:
            prepared.append((a, 'X'))
            i += 1
    return prepared

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    pairs = prepare_plaintext(plaintext)
    ciphertext = ""
    steps = []

    for (a, b) in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # Same row
            nc1 = (c1 + 1) % 5
            nc2 = (c2 + 1) % 5
            enc_a = matrix[r1][nc1]
            enc_b = matrix[r2][nc2]
            rule = f"Baris sama (baris {r1+1}): geser kanan"
        elif c1 == c2:  # Same column
            nr1 = (r1 + 1) % 5
            nr2 = (r2 + 1) % 5
            enc_a = matrix[nr1][c1]
            enc_b = matrix[nr2][c2]
            rule = f"Kolom sama (kolom {c1+1}): geser bawah"
        else:  # Rectangle
            enc_a = matrix[r1][c2]
            enc_b = matrix[r2][c1]
            rule = f"Persegi panjang: tukar kolom"

        steps.append({
            'pair': f"{a}{b}",
            'pos_a': f"({r1+1},{c1+1})",
            'pos_b': f"({r2+1},{c2+1})",
            'rule': rule,
            'result': f"{enc_a}{enc_b}"
        })
        ciphertext += enc_a + enc_b

    return ciphertext, steps, matrix, pairs

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    ciphertext = ciphertext.upper().replace('J', 'I')
    ciphertext = ''.join(filter(str.isalpha, ciphertext))

    if len(ciphertext) % 2 != 0:
        ciphertext += 'X'

    pairs = [(ciphertext[i], ciphertext[i+1]) for i in range(0, len(ciphertext), 2)]
    plaintext = ""
    steps = []

    for (a, b) in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            nc1 = (c1 - 1) % 5
            nc2 = (c2 - 1) % 5
            dec_a = matrix[r1][nc1]
            dec_b = matrix[r2][nc2]
            rule = f"Baris sama (baris {r1+1}): geser kiri"
        elif c1 == c2:
            nr1 = (r1 - 1) % 5
            nr2 = (r2 - 1) % 5
            dec_a = matrix[nr1][c1]
            dec_b = matrix[nr2][c2]
            rule = f"Kolom sama (kolom {c1+1}): geser atas"
        else:
            dec_a = matrix[r1][c2]
            dec_b = matrix[r2][c1]
            rule = f"Persegi panjang: tukar kolom"

        steps.append({
            'pair': f"{a}{b}",
            'pos_a': f"({r1+1},{c1+1})",
            'pos_b': f"({r2+1},{c2+1})",
            'rule': rule,
            'result': f"{dec_a}{dec_b}"
        })
        plaintext += dec_a + dec_b

    return plaintext, steps, matrix, pairs
