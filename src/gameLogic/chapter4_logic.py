import sys
import threading
from InquirerPy import prompt
from src.helper import ensure_checkpoint_dir, save_checkpoint, load_checkpoint, delete_checkpoint, clear_console, play_sound, typewriter, game_over_prompt, process_player_choice
from src.story.chapter4 import chapter_4, chapter_4_event_1
from src.gameLogic.chapter5_logic import chapter5

# Inisialisasi game_state dari checkpoint jika ada
game_state = load_checkpoint()  # Memuat state dari file checkpoint.json

def display_state(state):
    """Menampilkan lokasi, inventaris, dan progres permainan."""
    print(f"Nama Karakter: {state['nama_karakter']}")
    print(f"Lokasi: {state['location']}")
    print(f"Progres: {state['progres']}\n")

def chapter4(nama_karakter):
    """Mengelola alur chapter 2."""
    for line in chapter_4(nama_karakter):
        typewriter(line)
    
    # Mengupdate status game
    game_state["location"] = "Kuil"  # Update lokasi
    game_state["progres"] = "Dalam Bayang-Bayang Kuil"  # Update progres
    
    # Menyimpan perubahan ke checkpoint
    save_checkpoint(game_state)
    clear_console()

    chapter4_event1(game_state['nama_karakter'])

def chapter4_event1(nama_karakter):
    global game_state

    for line in chapter_4_event_1(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Pintu yang Terkunci"
    save_checkpoint(game_state)
    end_chapter(game_state['nama_karakter']) # Nanti bagian ini hapus men, dipindahin ke event10, buat contohnya liat yang chapter1_logic fungsi chapter1_event10

    # Lanjutkan men (buat contoh liat yang chapter5_logic)

def end_chapter(nama_karakter):
    """Akhiri Chapter 4 dan lanjutkan ke Chapter 5"""
    typewriter("Chapter 4 selesai. Permainan berlanjut ke chapter berikutnya...")
    clear_console()
    chapter5(game_state['nama_karakter'])