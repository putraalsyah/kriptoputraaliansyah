# 🔐 KriptoCipher — Simulasi Kriptografi Klasik

> Aplikasi Web interaktif untuk mensimulasikan lima algoritma kriptografi klasik secara transparan dan edukatif, dibangun dengan Python & Flask.

---

## 📋 Deskripsi

**KriptoCipher** adalah aplikasi web yang dikembangkan sebagai **Tugas 1 Mata Kuliah Kriptografi, Semester 6 TA 2025/2026**. Aplikasi ini mensimulasikan proses enkripsi dan dekripsi dari lima algoritma kriptografi klasik secara detail — menampilkan setiap langkah perhitungan, rumus matematis, dan visualisasi matriks secara real-time.

Tujuan utama aplikasi ini adalah **edukatif**: membantu pengguna memahami cara kerja algoritma kriptografi klasik melalui tampilan yang transparan dan interaktif.

---

## ✨ Fitur Utama

- **5 Algoritma Kriptografi Klasik** — Caesar, Vigenère, Affine, Hill, Playfair
- **Enkripsi & Dekripsi Real-time** — Hasil muncul langsung tanpa reload halaman
- **Langkah Demi Langkah** — Setiap karakter ditampilkan proses perhitungannya dalam tabel detail
- **Visualisasi Matriks** — Matriks kunci Hill (2×2 / 3×3) dan Playfair 5×5 ditampilkan secara visual
- **Rumus Matematis** — Formula lengkap ditampilkan di setiap halaman algoritma
- **Dark / Light Mode** — Toggle tema, preferensi disimpan di localStorage
- **Riwayat Operasi** — Semua enkripsi/dekripsi tercatat dalam sesi pengguna
- **Responsif** — Tampilan optimal di desktop, tablet, maupun mobile
- **Validasi Input** — Error handling yang informatif dan ramah pengguna

---

## 🧮 Algoritma yang Diimplementasikan

### 1. Caesar Cipher
Substitusi sederhana dengan pergeseran huruf tetap.

```
Enkripsi : C = (P + K) mod 26
Dekripsi : P = (C - K + 26) mod 26
```

- Input kunci: angka shift (1–25)
- Menampilkan nilai numerik tiap huruf dan hasil pergeserannya

---

### 2. Vigenère Cipher
Ekstensi Caesar Cipher menggunakan kata kunci yang diulang.

```
Enkripsi : Cᵢ = (Pᵢ + Kᵢ) mod 26
Dekripsi : Pᵢ = (Cᵢ - Kᵢ + 26) mod 26
```

- Input kunci: kata kunci alfabet (diulang sepanjang teks)
- Menampilkan pasangan huruf plaintext–kunci dan perhitungannya

---

### 3. Affine Cipher
Enkripsi berbasis fungsi linear modular.

```
Enkripsi : C = (a × P + b) mod 26
Dekripsi : P = a⁻¹ × (C - b + 26) mod 26
```

- Input kunci: dua integer `a` dan `b`
- `a` harus relatif prima dengan 26 (nilai valid: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)
- Menampilkan invers modular `a⁻¹` secara otomatis

---

### 4. Hill Cipher
Enkripsi berbasis perkalian matriks modular.

```
Enkripsi : C = K × P (mod 26)
Dekripsi : P = K⁻¹ × C (mod 26)
```

- Input kunci: matriks n×n (2×2 atau 3×3)
- Determinan matriks kunci harus relatif prima dengan 26
- Menampilkan matriks kunci, matriks invers, perhitungan per blok
- Padding otomatis dengan huruf 'X' jika teks tidak habis dibagi

---

### 5. Playfair Cipher
Enkripsi bigram (pasangan huruf) menggunakan matriks 5×5.

```
Aturan 1 (Baris sama)   : Enkripsi → geser kanan | Dekripsi → geser kiri
Aturan 2 (Kolom sama)   : Enkripsi → geser bawah | Dekripsi → geser atas
Aturan 3 (Persegi pjg)  : Tukar kolom (sama untuk keduanya)
```

- Input kunci: kata kunci untuk membentuk matriks 5×5
- Huruf J digabung dengan I
- Menampilkan matriks 5×5 interaktif, pasangan bigram, dan aturan yang digunakan tiap pasangan

---

## 🛠️ Teknologi

| Komponen | Teknologi |
|---|---|
| Backend | Python 3.x + Flask |
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| Template Engine | Jinja2 |
| Komputasi Matriks | NumPy |
| Font | Syne, Space Mono, DM Sans (Google Fonts) |
| Icon | Font Awesome 6 |
| Web Server (prod) | Gunicorn |

---

## 📁 Struktur Proyek

```
kriptoputraaliansyah/
│
├── app.py                    # Flask app utama, routing, API endpoints
├── requirements.txt          # Dependensi Python
├── Procfile                  # Konfigurasi deployment (Gunicorn)
├── .gitignore
│
├── ciphers/                  # Modul algoritma (terpisah & modular)
│   ├── __init__.py
│   ├── caesar.py             # Implementasi Caesar Cipher
│   ├── vigenere.py           # Implementasi Vigenère Cipher
│   ├── affine.py             # Implementasi Affine Cipher
│   ├── hill.py               # Implementasi Hill Cipher (NumPy)
│   └── playfair.py           # Implementasi Playfair Cipher
│
├── templates/                # Template HTML (Jinja2)
│   ├── base.html             # Layout utama: sidebar, topbar, dark/light mode
│   ├── index.html            # Halaman dashboard / beranda
│   ├── caesar.html           # Halaman Caesar Cipher
│   ├── vigenere.html         # Halaman Vigenère Cipher
│   ├── affine.html           # Halaman Affine Cipher
│   ├── hill.html             # Halaman Hill Cipher + input matriks
│   ├── playfair.html         # Halaman Playfair Cipher + matriks 5×5
│   └── history.html          # Halaman riwayat operasi
│
└── static/
    ├── css/
    │   └── style.css         # Stylesheet utama (CSS variables, dark/light, animasi)
    └── js/
        └── main.js           # Script utama (theme toggle, API calls, helpers)
```

---

## ⚙️ Cara Menjalankan Secara Lokal

**1. Clone repository**
```bash
git clone https://github.com/USERNAME/kriptoputraaliansyah.git
cd kriptoputraaliansyah
```

**2. Buat virtual environment (opsional tapi disarankan)**
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

**3. Install dependensi**
```bash
pip install -r requirements.txt
```

**4. Jalankan aplikasi**
```bash
python app.py
```

**5. Buka di browser**
```
http://localhost:5000
```

---

## 🌐 Deployment

Aplikasi ini di-deploy dan dapat diakses secara publik di:

> **https://www.kriptoputraaliansyah.my.id**

### Panduan Deploy ke Railway (Rekomendasi)

1. Push repository ke GitHub
2. Buat akun di [railway.app](https://railway.app) dan hubungkan dengan GitHub
3. Pilih repository ini → Railway otomatis mendeteksi `Procfile`
4. Tambahkan environment variable: `SECRET_KEY=your_secret_key`
5. Setelah deploy, beli domain `.my.id` di Niagahoster atau Rumahweb
6. Tambahkan custom domain di Railway Settings → hubungkan DNS CNAME ke domain Railway
7. Aktifkan SSL otomatis dari Railway

---

## 🔌 API Endpoints

Semua endpoint menerima `POST` request dengan `Content-Type: application/json`.

| Endpoint | Method | Deskripsi |
|---|---|---|
| `/api/caesar` | POST | Enkripsi / Dekripsi Caesar |
| `/api/vigenere` | POST | Enkripsi / Dekripsi Vigenère |
| `/api/affine` | POST | Enkripsi / Dekripsi Affine |
| `/api/hill` | POST | Enkripsi / Dekripsi Hill |
| `/api/playfair` | POST | Enkripsi / Dekripsi Playfair |
| `/api/clear-history` | POST | Hapus riwayat sesi |

**Contoh Request Caesar:**
```json
POST /api/caesar
{
  "text": "HELLO",
  "shift": 3,
  "mode": "encrypt"
}
```

**Contoh Response:**
```json
{
  "result": "KHOOR",
  "steps": [
    { "char": "H", "p_val": 7, "formula": "(7 + 3) mod 26 = 10", "result": "K" },
    { "char": "E", "p_val": 4, "formula": "(4 + 3) mod 26 = 7",  "result": "H" },
    ...
  ]
}
```

---

## 🧪 Contoh Penggunaan

### Caesar Cipher
```
Plaintext : HELLO WORLD
Shift     : 3
Ciphertext: KHOOR ZRUOG
```

### Vigenère Cipher
```
Plaintext : HELLO
Kunci     : KEY
Ciphertext: RIJVS
```

### Affine Cipher
```
Plaintext : HELLO
a=5, b=8
Ciphertext: RCLLA
```

### Hill Cipher (2×2)
```
Plaintext  : ACT
Matriks K  : [[3,3],[2,5]]
Ciphertext : GKWX
```

### Playfair Cipher
```
Plaintext  : HELLO
Kunci      : MONARCHY
Ciphertext : CFSUPM
```

---

## 📌 Catatan Teknis

- **Hill Cipher**: Determinan matriks kunci harus relatif prima dengan 26. Jika tidak, aplikasi akan menampilkan pesan error beserta penjelasannya.
- **Playfair Cipher**: Huruf J secara otomatis diganti menjadi I sesuai standar algoritma. Pasangan huruf ganda dipisah dengan sisipan 'X'.
- **Affine Cipher**: Validasi nilai `a` dilakukan di sisi server; hanya nilai yang relatif prima dengan 26 yang diterima.
- **Padding Hill**: Jika panjang teks tidak habis dibagi ukuran blok, padding 'X' ditambahkan secara otomatis.
- **Riwayat**: Tersimpan di server-side session Flask, tidak persisten antar sesi browser.

---

## 👤 Identitas

| | |
|---|---|
| **Nama** | Putra Aliansyah |
| **Mata Kuliah** | Kriptografi |
| **Semester** | 6 |
| **Tahun Ajaran** | 2025/2026 Genap |
| **Domain** | kriptoputraaliansyah.my.id |

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik. Dilarang menyalin atau menggunakan ulang tanpa izin.

---

<div align="center">
  Dibuat dengan ☕ dan Python untuk Tugas Kriptografi Semester 6
</div>
