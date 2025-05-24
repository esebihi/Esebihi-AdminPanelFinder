#!/usr/bin/env python3


import requests
from urllib.parse import urljoin
import sys
import os

# ANSI renk kodları
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Banner
BANNER = r"""
▓█████   ██████ ▓█████  ▄▄▄▄    ██▓ ██░ ██  ██▓
▓█   ▀ ▒██    ▒ ▓█   ▀ ▓█████▄ ▓██▒▓██░ ██▒▓██▒
▒███   ░ ▓██▄   ▒███   ▒██▒ ▄██▒██▒▒██▀▀██░▒██▒
▒▓█  ▄   ▒   ██▒▒▓█  ▄ ▒██░█▀  ░██░░▓█ ░██ ░██░
░▒████▒▒██████▒▒░▒████▒░▓█  ▀█▓░██░░▓█▒░██▓░██░
░░ ▒░ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░▒▓███▀▒░▓   ▒ ░░▒░▒░▓  
 ░ ░  ░░ ░▒  ░ ░ ░  ░▒░▒   ░  ▒ ░ ▒ ░▒░ ░ ▒ ░
   ░   ░  ░  ░     ░    ░    ░  ▒ ░ ░  ░░ ░ ▒ ░
   ░  ░      ░     ░  ░ ░       ░   ░  ░  ░ ░  
                             ░                  
"""

def load_wordlist(filename="worldlist/wordlist.txt"):
    if not os.path.isfile(filename):
        print(f"{RED}Hata: '{filename}' dosyası bulunamadı. Aynı dizinde olmalı.{RESET}")
        sys.exit(1)
    paths = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                paths.append(line)
    if not paths:
        print(f"{RED}Hata: '{filename}' dosyası boş veya yorum satırlarından ibaret.{RESET}")
        sys.exit(1)
    return paths

def check_url(base_url, path):
    url = urljoin(base_url, path)
    try:
        response = requests.get(url, timeout=7, allow_redirects=True)
        if response.status_code in [200, 401, 403]:
            return url, response.status_code, True
        else:
            return url, response.status_code, False
    except requests.RequestException:
        return url, None, False

def main():
    print(BANNER)  # Banner'ı yazdır
    print("Admin Panel Bulucu Tool")
    print("-----------------------")
    base_url = input("Site adresini girin (ör: https://site.com): ").strip()
    if not (base_url.startswith("http://") or base_url.startswith("https://")):
        print(RED + "Lütfen geçerli bir URL (http:// veya https:// ile başlayan) girin." + RESET)
        sys.exit(1)
    if not base_url.endswith('/'):
        base_url += '/'

    wordlist = load_wordlist()
    print(f"\n{base_url} üzerinde admin panel yolları aranıyor...\n")

    for path in wordlist:
        url, status, success = check_url(base_url, path)
        if success:
            print(f"{GREEN}[+] Bulundu: {url} (Status: {status}){RESET}")
        else:
            status_text = f"Status: {status}" if status is not None else "Erişim yok"
            print(f"{RED}[-] Bulunamadı: {url} ({status_text}){RESET}")

if __name__ == "__main__":
    main()
