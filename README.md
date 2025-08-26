Tools Linux untuk memeriksa apakah kata sandi Anda pernah bocor 

*langsung dari terminal, aman (tidak mengirimkan kata sandi lengkap), dan tanpa menginstal alat tambahan.

$ git clone https://github.com/spyschools/cek-password.git
$ cd cek-password
$ chmod +x cek_password.sh

$ ./cek_password.sh
*Masukkan kata sandi yang ingin Anda periksa

*versi python
$ sudo apt update && sudo apt install python3 python3-pip -y
$ pip3 install requests
$ python3 cek_password.py
*Masukkan kata sandi yang ingin Anda periksa

*Keamanan:
Tidak mengirim password ke internet.
Hanya mengirim 5 huruf pertama hash SHA-1.
Semua proses cocokkan dilakukan di lokal.
