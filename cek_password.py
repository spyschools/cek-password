#!/usr/bin/env python3

import hashlib
import requests
import getpass

def hash_password(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1[:5], sha1[5:]

def check_pwned(prefix, suffix):
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def main():
    password = getpass.getpass("Masukkan password: ")
    prefix, suffix = hash_password(password)
    jumlah = check_pwned(prefix, suffix)

    if jumlah:
        print(f"⚠️  Password pernah bocor sebanyak {jumlah} kali. Jangan gunakan ini lagi.")
    else:
        print("✅ Password aman (belum ditemukan di database kebocoran).")

if __name__ == "__main__":
    main()
