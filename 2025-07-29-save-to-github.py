# 🧠 Sribuana Prompt Log – 2025-07-29
# 🔧 Save Prompt to GitHub Automatically using API

import requests
import base64

# Gantikan dengan token GitHub anda
token = "ghp_xxx..."  # ← JANGAN kongsi token sebenar
repo = "user/chatgpt-prompts"
file_path = "2025-07-29-meta-prompt.md"
commit_message = "Tambah prompt META Oracle"
prompt_content = """
## Prompt
Bagaimana save prompt dari ChatGPT ke GitHub?

## Jawapan
(Sribuana menjelaskan cara manual & automatik simpan prompt ke GitHub)
"""

url = f"https://api.github.com/repos/{repo}/contents/{file_path}"
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}
data = {
    "message": commit_message,
    "content": base64.b64encode(prompt_content.encode()).decode()
}

response = requests.put(url, headers=headers, json=data)

print("Status:", response.status_code)
print("Response:", response.json())
