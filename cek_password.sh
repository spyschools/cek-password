# nano #!/bin/bash

read -sp "Masukkan password: " password
echo

# Hash password dengan SHA1 (uppercase)
hash=$(echo -n "$password" | sha1sum | awk '{print toupper($1)}')
prefix=${hash:0:5}
suffix=${hash:5}

# Ambil data dari API Pwned Passwords
response=$(curl -s "https://api.pwnedpasswords.com/range/$prefix")

# Cek apakah sisa hash ada di hasil
echo "$response" | grep -q "$suffix"

if [ $? -eq 0 ]; then
    echo "⚠️  Password INI PERNAH BOCOR! Jangan gunakan password ini lagi."
else
    echo "✅ Password AMAN (belum ditemukan di data kebocoran)."
fi
