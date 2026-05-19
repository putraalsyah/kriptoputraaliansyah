from flask import Flask, render_template, request, jsonify, session
import json
from datetime import datetime
from ciphers import (
    caesar_encrypt, caesar_decrypt,
    vigenere_encrypt, vigenere_decrypt,
    affine_encrypt, affine_decrypt,
    hill_encrypt, hill_decrypt,
    playfair_encrypt, playfair_decrypt
)

app = Flask(__name__)
app.secret_key = 'kriptoputraaliansyah_secret_2025'

# ─── Routes ────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/caesar')
def caesar_page():
    return render_template('caesar.html')

@app.route('/vigenere')
def vigenere_page():
    return render_template('vigenere.html')

@app.route('/affine')
def affine_page():
    return render_template('affine.html')

@app.route('/hill')
def hill_page():
    return render_template('hill.html')

@app.route('/playfair')
def playfair_page():
    return render_template('playfair.html')

@app.route('/history')
def history_page():
    hist = session.get('history', [])
    return render_template('history.html', history=hist)

# ─── API Endpoints ─────────────────────────────────────────────────────────────

def add_to_history(cipher_name, mode, plaintext, key_info, result):
    if 'history' not in session:
        session['history'] = []
    record = {
        'id': len(session['history']) + 1,
        'cipher': cipher_name,
        'mode': mode,
        'input': plaintext[:50] + ('...' if len(plaintext) > 50 else ''),
        'key': key_info,
        'output': result[:50] + ('...' if len(result) > 50 else ''),
        'timestamp': datetime.now().strftime('%d %b %Y, %H:%M:%S')
    }
    session['history'].insert(0, record)
    session['history'] = session['history'][:50]  # keep last 50
    session.modified = True

@app.route('/api/caesar', methods=['POST'])
def api_caesar():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        shift = int(data.get('shift', 3))
        mode = data.get('mode', 'encrypt')

        if not text:
            return jsonify({'error': 'Teks tidak boleh kosong.'}), 400
        if not 1 <= shift <= 25:
            return jsonify({'error': 'Shift harus antara 1-25.'}), 400

        if mode == 'encrypt':
            result, steps = caesar_encrypt(text, shift)
        else:
            result, steps = caesar_decrypt(text, shift)

        add_to_history('Caesar', mode, text, f"shift={shift}", result)
        return jsonify({'result': result, 'steps': steps})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/vigenere', methods=['POST'])
def api_vigenere():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        key = data.get('key', '').strip()
        mode = data.get('mode', 'encrypt')

        if not text:
            return jsonify({'error': 'Teks tidak boleh kosong.'}), 400
        if not key:
            return jsonify({'error': 'Kunci tidak boleh kosong.'}), 400

        if mode == 'encrypt':
            result, steps, clean_key = vigenere_encrypt(text, key)
        else:
            result, steps, clean_key = vigenere_decrypt(text, key)

        add_to_history('Vigenère', mode, text, f"key={clean_key}", result)
        return jsonify({'result': result, 'steps': steps, 'key': clean_key})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/affine', methods=['POST'])
def api_affine():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        a = int(data.get('a', 1))
        b = int(data.get('b', 0))
        mode = data.get('mode', 'encrypt')

        if not text:
            return jsonify({'error': 'Teks tidak boleh kosong.'}), 400

        if mode == 'encrypt':
            result, steps = affine_encrypt(text, a, b)
            return jsonify({'result': result, 'steps': steps})
        else:
            result, steps, a_inv = affine_decrypt(text, a, b)
            add_to_history('Affine', mode, text, f"a={a}, b={b}", result)
            return jsonify({'result': result, 'steps': steps, 'a_inv': a_inv})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/hill', methods=['POST'])
def api_hill():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        matrix = data.get('matrix', [])
        mode = data.get('mode', 'encrypt')

        if not text:
            return jsonify({'error': 'Teks tidak boleh kosong.'}), 400
        if not matrix or len(matrix) < 2:
            return jsonify({'error': 'Matriks tidak valid.'}), 400

        n = len(matrix)
        for row in matrix:
            if len(row) != n:
                return jsonify({'error': f'Matriks harus berukuran {n}x{n}.'}), 400

        if mode == 'encrypt':
            result, steps, prepared = hill_encrypt(text, matrix)
            add_to_history('Hill', mode, text, f"{n}x{n} matrix", result)
            return jsonify({'result': result, 'steps': steps, 'prepared': prepared})
        else:
            result, steps, prepared, inv_key = hill_decrypt(text, matrix)
            add_to_history('Hill', mode, text, f"{n}x{n} matrix", result)
            return jsonify({'result': result, 'steps': steps, 'prepared': prepared, 'inv_key': inv_key})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/playfair', methods=['POST'])
def api_playfair():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        key = data.get('key', '').strip()
        mode = data.get('mode', 'encrypt')

        if not text:
            return jsonify({'error': 'Teks tidak boleh kosong.'}), 400
        if not key:
            return jsonify({'error': 'Kunci tidak boleh kosong.'}), 400

        if mode == 'encrypt':
            result, steps, matrix, pairs = playfair_encrypt(text, key)
        else:
            result, steps, matrix, pairs = playfair_decrypt(text, key)

        add_to_history('Playfair', mode, text, f"key={key.upper()}", result)
        return jsonify({
            'result': result,
            'steps': steps,
            'matrix': matrix,
            'pairs': [f"{a}{b}" for a, b in pairs]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    session['history'] = []
    session.modified = True
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
