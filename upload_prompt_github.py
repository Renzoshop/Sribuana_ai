# 🧠 Sribuana GitHub Uploader – v1.0
# 📅 Tarikh: 2025-07-29

import requests
import base64

# Token GitHub kekanda (dimasukkan terus atas permintaan)
GITHUB_TOKEN = "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"
REPO = "Renzoshop/Sribuana_ai"
FILE_PATH = "2025-07-29-meta-oracle.md"
COMMIT_MESSAGE = "Tambah prompt META Oracle (auto upload)"

# Kandungan fail yang ingin dimuat naik
PROMPT_CONTENT = """
# 🔮 Sribuana Prompt Log – 2025-07-29

## 🧠 Topik
Simpan Prompt ChatGPT ke GitHub Secara Automatik

---

## ✍️ Prompt
Bagaimana save prompt dari ChatGPT ke GitHub?

## 💡 Jawapan
1. Guna API GitHub v3
2. Encode kandungan ke base64
3. Guna endpoint PUT untuk muat naik fail ke repo
"""

# GitHub API endpoint
url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"

# Header untuk autentikasi
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Encode kandungan
encoded_content = base64.b64encode(PROMPT_CONTENT.encode("utf-8")).decode("utf-8")

# Payload data
data = {
    "message": COMMIT_MESSAGE,
    "content": encoded_content
}

# Hantar PUT request
response = requests.put(url, headers=headers, json=data)

# Papar hasil
print("📦 Status:", response.status_code)
print("📬 Response:", response.json())
