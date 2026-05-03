# Assignment: AI Development with OpenAI

Repositori ini berisi kumpulan tugas pemrograman Python untuk integrasi dengan OpenAI LLM (Large Language Model), yang mencakup pembuatan chatbot interaktif dan sistem pipeline pemrosesan teks.

## 📂 Struktur Proyek

```text
.
├── 01_tugas/
│   ├── 01_chatbot.py    # Chatbot CS Gadget Central (Bahasa Jawa)
│   └── 02_pipeline.py   # Pipeline: Generate -> Summarize -> Extract
├── .env                 # Konfigurasi API (Hidden)
├── .env.example         # Template konfigurasi API
├── .gitignore           # Daftar file yang diabaikan Git
└── README.md            # Dokumentasi proyek
```

## 🚀 Persiapan (Setup)

1. **Clone repositori ini atau masuk ke direktori proyek.**
2. **Install dependensi yang dibutuhkan:**
   ```bash
   pip install openai python-dotenv
   ```
3. **Konfigurasi Environment Variables:**
   - Salin file `.env.example` menjadi `.env`.
   - Buka file `.env` dan masukkan `OPENAI_API_KEY` serta `OPENAI_BASE_URL` Anda.
   ```bash
   cp .env.example .env
   ```

## 🛠️ Penjelasan Tugas

### 1. Chatbot Customer Service (Bahasa Jawa)
File: `01_tugas/01_chatbot.py`

Chatbot ini dirancang untuk menjadi Customer Service di toko **Gadget Central Java**.
- **Fitur**: Menggunakan `SYSTEM_PROMPT` khusus untuk memaksa AI menjawab hanya dalam **Bahasa Jawa** yang ramah.
- **Konteks**: AI hanya akan menjawab berdasarkan informasi stok, lokasi, dan promo yang telah ditentukan dalam script.
- **Cara Menjalankan**:
  ```bash
  python 01_tugas/01_chatbot.py
  ```

### 2. 3-Step LLM Pipeline
File: `01_tugas/02_pipeline.py`

Script ini mendemonstrasikan bagaimana hasil dari satu pemanggilan LLM dapat digunakan sebagai input untuk pemanggilan berikutnya dalam sebuah alur kerja (pipeline).
- **Step 1 (Generate)**: Memberikan informasi detail mengenai topik tertentu.
- **Step 2 (Summarize)**: Meringkas hasil dari Step 1 menjadi satu paragraf.
- **Step 3 (Extract)**: Mengekstrak 3 kata kunci penting dari ringkasan di Step 2.
- **Cara Menjalankan**:
  ```bash
  python 01_tugas/02_pipeline.py
  ```

## 📝 Catatan
Proyek ini menggunakan model `gpt-5-nano` (atau sesuaikan dengan model yang tersedia pada provider Anda) melalui OpenAI SDK. Pastikan koneksi internet tersedia dan kuota API Anda mencukupi.
