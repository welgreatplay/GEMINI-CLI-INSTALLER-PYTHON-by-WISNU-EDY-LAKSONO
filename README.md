file ini menjadi Final Project Wisnu Edy Laksono A.K.A Sensei Wisnu

   Program ini hanya bekerja bagi siapapun yang sudah menginstall gemini CLI, dimana program ini dibuat secara interaktif berjalan pada CMD dengan kecepatan yang lebih cepat ketimbang gemini CLI.
   titik fokus pada program ini adalah penggunaan chatbot gemini inetraktif sekilas tanpa perlu menyimpan histori.
  pengembang sudah melanjutkan project ini dalam bentuk yang advanced namun masih perlu dikembangkan sebelum rilis di update selanjutnya.
 
berikut adalah tutorial membuat chat bot interaktif dari GEMINI AI pada Windows Command Prompt (CMD)

1. Install Python versi terbaru Install git versi terbaru jalankan file bat yang saya buat gemini sudah siap
2. install gemini CLI 
3. install Gemini API KEY di System Properties, klik tombol "Environment Variables...".(untuk yang mau menjalankan dengan Gemini API permanen)
4. jalankan bat Program

Terdapat jenis dua file Chatbot
1. Gemini Chat API Installed : API KEY sudah terinstall di windows
2. Gemini Chat API Manual    : hanya pada saat pertama kali menggunakan program ini API KEy di chat.py perlu dirubah selanjutnya tidak.


########## GEMINI API KEY MANUAL ###########

Langkah 1 : buka file simplified_chat_Gemini_API_Manual.py
Langkah 2 : edit pada bagian 


    # --- Konfigurasi ---
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(BASE_DIR) # Add base directory to sys.path for module imports
    API_KEY = "YOUR_GEMINI_API_KEY_HERE" <-----------# Ganti "YOUR_GEMINI_API_KEY_HERE" dengan kunci API Gemini Anda yang sebenarnya


    kemudian simpan
Langkah 3 : Jalankan bat. 
    Gemini Interaktif sudah siap.



########## GEMINI API KEY INSTALLED ###########

Langkah 1: Menginstal Python dan Google SDK
Instal Python: Jika Anda belum memiliki Python, unduh dan instal versi terbaru dari situs web resminya. Pastikan Anda mencentang opsi "Add python.exe to PATH" saat instalasi. Ini sangat penting agar Python dapat diakses dari Command Prompt.

Verifikasi Instalasi Python: Buka Command Prompt (tekan Win + R, ketik cmd, lalu Enter) dan jalankan perintah berikut untuk memastikan Python telah terinstal dengan benar:


Bash

python --version
Instal Google Generative AI Library: Di Command Prompt yang sama, instal library yang diperlukan untuk berinteraksi dengan Gemini API.


Bash

pip install -q -U google-generativeai
-q berarti quiet (tidak menampilkan banyak output), dan -U berarti upgrade (memastikan Anda mendapatkan versi terbaru).


Langkah 2: Mendapatkan Gemini API Key
Buka AI Studio: Pergi ke Google AI Studio dan login dengan akun Google Anda.

Buat API Key: Di panel kiri, klik "Get API key" atau "Create new API key". Google akan secara otomatis membuat API key untuk Anda.

Salin Key: Salin API key yang telah dibuat. Penting: Simpan key ini di tempat yang aman dan jangan bagikan secara publik.

Langkah 3: Mengatur Environment Variable di Windows
Menggunakan environment variable adalah cara terbaik dan teraman untuk menyimpan API key, karena Anda tidak perlu menuliskannya langsung dalam kode Anda.

Buka Environment Variables: Tekan tombol Win, ketik "Edit the system environment variables", lalu klik hasil pencarian yang muncul.

Buka Environment Variables Wizard: Di jendela System Properties, klik tombol "Environment Variables...".

Tambahkan Variabel Baru: Di bagian "User variables for [Username]", klik "New...".

Isi Data Variabel:

Variable name: GOOGLE_API_KEY

Variable value: Tempel API key yang telah Anda salin sebelumnya.

Simpan: Klik "OK" di semua jendela yang terbuka untuk menyimpan perubahan.



########## Menguji Instalasi #########

Untuk memastikan apakah Gemini CLI dan Gemini API key sudah terinstall atau belum, keterangan tersebut dapat dilihat dari output dengan menjalankan program coding dibawah ini.
Buat File Python: Buat file Python baru, misalnya test_gemini.py, dan tambahkan kode berikut:


Python

import os
import google.generativeai as genai

# Mengambil API Key dari environment variable


try:
    api_key = os.environ['GOOGLE_API_KEY']
    genai.configure(api_key=api_key)
    print("API Key berhasil dimuat!")
except KeyError:
    print("Error: GOOGLE_API_KEY environment variable tidak ditemukan.")



# Menguji koneksi dengan model


for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
Kode ini akan mengambil API key dari environment variable dan mencoba mencetak daftar model yang tersedia, memastikan koneksi berhasil.

Jalankan Kode: Buka Command Prompt baru (ini penting agar perubahan environment variable terdeteksi) dan jalankan skrip Python:



Bash

python test_gemini.py
Verifikasi Output: Jika instalasi berhasil, Anda akan melihat pesan "API Key berhasil dimuat!" diikuti dengan daftar model yang didukung, seperti models/gemini-1.5-pro atau models/gemini-1.0-pro.


