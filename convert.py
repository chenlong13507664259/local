import requests
import base64
import yaml

SOURCE_URL = "https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_BASE64.txt"
OUTPUT_FILE = "proxies.yaml"

res = requests.get(SOURCE_URL)
raw_data = res.text.strip().splitlines()

proxies = []

for line in raw_data:
    try:
        decoded = base64.b64decode(line.strip()).decode("utf-8")
        if decoded.startswith(("vmess://", "vless://", "trojan://")):
            proxies.append(decoded)
    except Exception:
        continue

yaml_data = {"proxies": proxies}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    yaml.dump(yaml_data, f, allow_unicode=True)

print(f"已生成 {OUTPUT_FILE}")
