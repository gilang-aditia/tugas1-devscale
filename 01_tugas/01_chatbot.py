import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    base_url=OPENAI_BASE_URL, 
    api_key=OPENAI_API_KEY
)

INFORMATION_CONTEXT = """
Nama Toko: Gadget Central Java
Lokasi: Mall Elektronik Lantai 2, Jakarta.
Produk Unggulan:
1. Smartphone X Pro - Rp 12.000.000 (Stok: 5 unit)
2. Laptop Ultra Slim - Rp 15.500.000 (Stok: 2 unit)
3. Wireless Earbuds - Rp 1.500.000 (Stok: 10 unit)
Layanan: Servis HP & Laptop, Tukar Tambah.
Jam Operasional: 10:00 - 21:00
Promo: Diskon 10% untuk pembelian Laptop Ultra Slim minggu ini!
"""

SYSTEM_PROMPT = f"""
Kamu adalah customer service untuk Gadget Central.
Selalu jawab dalam Bahasa jawa yang baik dan benar.

Hanya jawab berdasarkan konteks informasi berikut:
{INFORMATION_CONTEXT}

Jika kamu tidak memiliki informasinya, katakan dengan sopan bahwa kamu tidak tahu.
Gunakan emoji yang sesuai agar percakapan terasa ramah.
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

while True:
    user_input = input("User: ")
    user_message = {"role": "user", "content": user_input}
    
    messages.append(user_message)
    
    completion = client.chat.completions.create(
        model="gpt-5-nano",
        messages=messages,
    )
    
    final_output = completion.choices[0].message.content or ""
    print(f"AI: {final_output}\n")
    
    messages.append({"role": "assistant", "content": final_output})
