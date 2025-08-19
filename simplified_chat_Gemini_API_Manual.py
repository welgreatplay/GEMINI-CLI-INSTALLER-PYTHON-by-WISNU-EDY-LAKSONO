
# This is a simplified version of chat.py for interactive chat only.
# No offline chat saving or export features are included.

import os
import google.generativeai as genai
import sys
import re

# Fungsi untuk membersihkan layar konsol
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Konfigurasi ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR) # Add base directory to sys.path for module imports
# Ganti "YOUR_GEMINI_API_KEY_HERE" dengan kunci API Gemini Anda yang sebenarnya
API_KEY = "YOUR_GEMINI_API_KEY_HERE"

# --- Fungsi Pembantu ---
def clean_text(text):
    """Menghilangkan simbol/teks aneh dan merapikan spasi, sambil mempertahankan paragraf."""
    # Pola yang ingin dihapus: *, **, ##, --, __, |, |--|, <br>, |---|---|---|
    # Menggunakan regex untuk menghapus semua pola ini
    # Urutan penting: hapus pola yang lebih panjang dulu
    patterns_to_remove = [
        r'\*\*',  # **
        r'##',      # ##
        r'\|---|---|---|', # |---|---|---|
        r'\|--\|', # |--|
        r'<br>',    # <br>
        r'--',      # --
        r'__',      # __
        r'\*',     # *
        r'\|',     # |
    ]

    cleaned_text = text
    for pattern in patterns_to_remove:
        cleaned_text = re.sub(pattern, '', cleaned_text)

    # Ganti multiple spasi (bukan newline) dengan satu spasi
    cleaned_text = re.sub(r'[ \t]+', ' ', cleaned_text)

    # Ganti multiple newlines dengan maksimal dua newlines untuk paragraf
    cleaned_text = re.sub(r'\n{3,}', '\n\n', cleaned_text)

    # Hapus spasi di awal/akhir baris
    cleaned_text = '\n'.join([line.strip() for line in cleaned_text.split('\n')])

    # Hapus spasi di awal/akhir keseluruhan teks
    cleaned_text = cleaned_text.strip()

    return cleaned_text

# --- Fungsi Utama ---
def main():
    """Fungsi utama untuk menjalankan chat."""
    # 1. Konfigurasi API Key
    api_key = API_KEY
    if not api_key or api_key == "YOUR_GEMINI_API_KEY_HERE":
        print("Error: Kunci API Gemini belum diatur. Harap ganti 'YOUR_GEMINI_API_KEY_HERE' dengan kunci API Anda.")
        return

    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"Error saat mengkonfigurasi Gemini API: {e}. Pastikan API Key Anda valid dan tidak ada masalah koneksi.")
        return

    # 2. Pilihan Mulai/Lanjutkan Chat
    history = []
    while True:
        clear_screen()
        print("--- Menu Chat Gemini Interaktif ---")
        print("--By Sensei Wisnu--")
        print("1. Mulai Chat Baru")
        print("0. Keluar")
        
        main_menu_choice = input("Pilihan Anda (0/1): ").strip().lower()

        if main_menu_choice == '0':
            print("Terima kasih! Sampai jumpa.")
            break # Exit the main loop

        elif main_menu_choice == '1': # Mulai Chat Baru
            history = [] # Reset history for new chat
            print("Memulai chat baru.")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()
        else:
            print("Pilihan tidak valid. Harap masukkan '0' atau '1'.")
            input("Tekan Enter untuk melanjutkan...")
            continue

        # --- Model Initialization and Chat Loop (NOW INSIDE THE MAIN MENU LOOP) ---
        if main_menu_choice == '1': # Only proceed if 'Mulai Chat Baru' was chosen
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                chat = model.start_chat(history=history)
            except Exception as e:
                print(f"Error saat memulai model Gemini atau chat: {e}. Pastikan Anda memiliki akses ke model 'gemini-1.5-flash' dan koneksi internet stabil.")
                input("Tekan Enter untuk kembali ke menu utama...")
                continue

            print("\n--- Selamat Datang di Gemini Chat ---")
            print("Ketik 'keluar' atau 'exit' untuk berhenti.")
            print("-------------------------------------")

            # 3. Loop Chat Interaktif (NOW INSIDE THE MAIN MENU LOOP)
            try:
                while True: # Interactive chat loop
                    user_input = input("Anda: ").strip()
                    user_input_lower = user_input.lower()

                    if user_input_lower in ['keluar', 'exit']:
                        print("Terima kasih! Sesi selesai.")
                        break # Break out of interactive chat loop, return to main menu loop

                    if not user_input:
                        continue

                    try:
                        response = chat.send_message(user_input)
                        # Pastikan response.text ada sebelum mencetak
                        if response.text:
                            print(f"Gemini: {response.text}")
                        else:
                            print("Gemini: (Tidak ada respons teks)")
                        
                    except Exception as e:
                        print(f"Terjadi error saat mengirim pesan: {e}. Mungkin ada masalah koneksi atau respons dari Gemini.")
                        break

            except KeyboardInterrupt:
                print("\nTerima kasih! Sesi dihentikan.")
            
            # After interactive chat loop finishes, control returns here,
            # and the main menu while True loop will continue, showing the menu again.

if __name__ == "__main__":
    main()
