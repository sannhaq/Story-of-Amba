import json
import os
import pygame
import sys
import threading
import time

CHECKPOINT_DIR = 'checkpoints'
CHECKPOINT_FILE = os.path.join(CHECKPOINT_DIR, 'checkpoint.json')

def ensure_checkpoint_dir():
    """Membuat folder checkpoints jika belum ada."""
    if not os.path.exists(CHECKPOINT_DIR):
        os.makedirs(CHECKPOINT_DIR)
        print(f"Folder '{CHECKPOINT_DIR}' dibuat untuk menyimpan checkpoint.")

def save_checkpoint(state):
    """Menyimpan state permainan ke file checkpoint."""
    ensure_checkpoint_dir()  # Pastikan folder checkpoints sudah ada
    with open(CHECKPOINT_FILE, 'w') as file:
        json.dump(state, file)
    print("\nCheckpoint tersimpan.")

def load_checkpoint():
    """Memuat state permainan dari file checkpoint jika ada."""
    try:
        with open(CHECKPOINT_FILE, 'r') as file:
            state = json.load(file)
        print("Checkpoint dimuat.")
        return state
    except FileNotFoundError:
        print("Tidak ada checkpoint yang ditemukan.")
        clear_console()
        return None  # Mengembalikan None jika tidak ada checkpoint

def delete_checkpoint():
    """Menghapus file checkpoint jika ada."""
    if os.path.exists(CHECKPOINT_FILE):
        os.remove(CHECKPOINT_FILE)
        print("Checkpoint dihapus.")
    else:
        print("Tidak ada checkpoint yang ditemukan untuk dihapus.")

def clear_console():
    """Menghapus layar console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound(sound_file):
    """Memutar file suara yang diberikan."""
    # Tentukan path file suara
    sound_file_path = os.path.join('assets/sounds', sound_file).replace('\\', '/')
    
    # Periksa apakah file suara ada
    if os.path.exists(sound_file_path):
        # Inisialisasi pygame mixer untuk memutar suara
        pygame.mixer.init()
        
        # Memuat dan memutar suara
        try:
            pygame.mixer.music.load(sound_file_path)
            pygame.mixer.music.play()
            
            # Tunggu hingga suara selesai diputar
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  # Menjaga agar program tidak mengganggu suara
        except pygame.error as e:
            print(f"Gagal memutar suara '{sound_file}': {e}")
    else:
        print(f"File suara '{sound_file}' tidak ditemukan.")

# Fungsi untuk mencetak teks dengan efek typewriter
def typewriter(text, typing_sound_file='typing.mp3', delay=0.05):
    """Menampilkan teks dengan efek typewriter dan suara ketikan."""
    # Jalankan suara ketikan di thread terpisah
    sound_thread = threading.Thread(target=play_sound, args=(typing_sound_file,))
    sound_thread.start()  # Memulai suara ketikan

    for char in text:
        sys.stdout.write(char)  # Menulis karakter ke console
        sys.stdout.flush()  # Memaksa output ke console
        time.sleep(delay)  # Delay antara karakter

    # Hentikan suara ketikan setelah selesai
    pygame.mixer.music.stop()
    sound_thread.join()  # Tunggu hingga suara ketikan selesai
    print()  # Pindah ke baris baru setelah teks selesai dicetak