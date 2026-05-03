import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Setup Client
client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"), 
    api_key=os.getenv("OPENAI_API_KEY")
)

topic = "Sejarah dan produk unggulan di Gadget Central Java"

# --- STEP 1: GENERATE ---
# Kita minta AI memberikan informasi lengkap
response1 = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[{"role": "user", "content": f"Jelaskan secara detail tentang {topic}"}]
)
raw_info = response1.choices[0].message.content
print("Step 1 Selesai: Informasi mentah sudah didapat.")


# --- STEP 2: SUMMARIZE ---
# Kita masukkan hasil dari Step 1 untuk diringkas
response2 = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[{"role": "user", "content": f"Ringkas teks ini menjadi 1 paragraf: {raw_info}"}]
)
summary = response2.choices[0].message.content
print("Step 2 Selesai: Ringkasan sudah dibuat.")


# --- STEP 3: EXTRACT ---
# Kita masukkan hasil ringkasan dari Step 2 untuk diambil poin pentingnya
response3 = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[{"role": "user", "content": f"Ambil 3 kata kunci penting dari ringkasan ini: {summary}"}]
)
final_result = response3.choices[0].message.content
print("Step 3 Selesai: Poin penting sudah diekstrak.")


# Tampilkan Hasil Akhir
print("\n--- HASIL AKHIR ---")
print(final_result)
