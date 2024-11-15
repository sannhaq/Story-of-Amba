import sys
import threading
from InquirerPy import prompt
from src.helper import ensure_checkpoint_dir, save_checkpoint, load_checkpoint, delete_checkpoint, clear_console, play_sound, typewriter, game_over_prompt, process_player_choice
from src.story.chapter2 import chapter_2, chapter_2_event_1
from src.gameLogic.chapter3_logic import chapter3

# Inisialisasi game_state dari checkpoint jika ada
game_state = load_checkpoint()  # Memuat state dari file checkpoint.json

def display_state(state):
    """Menampilkan lokasi, inventaris, dan progres permainan."""
    print(f"Nama Karakter: {state['nama_karakter']}")
    print(f"Lokasi: {state['location']}")
    print(f"Progres: {state['progres']}\n")

def chapter2(nama_karakter):
    """Mengelola alur chapter 2."""
    for line in chapter_2(nama_karakter):
        typewriter(line)
    
    # Mengupdate status game
    game_state["location"] = "Kapal"  # Update lokasi
    game_state["progres"] = "Perjalanan ke Pulau Amba"  # Update progres
    
    # Menyimpan perubahan ke checkpoint
    save_checkpoint(game_state)
    clear_console()

    chapter2_event1(game_state['nama_karakter'])

def chapter2_event1(nama_karakter):
    global game_state

    for line in chapter_2_event_1(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Badai di Tengah Malam"
    save_checkpoint(game_state)
    end_chapter(game_state['nama_karakter']) # Nanti bagian ini hapus men, dipindahin ke event10, buat contohnya liat yang chapter1_logic fungsi chapter1_event10 

    # Lanjutkan men (buat contoh liat yang chapter5_logic)

def end_chapter(nama_karakter):
    """Akhiri Chapter 2 dan lanjutkan ke Chapter 3"""
    typewriter("Chapter 2 selesai. Permainan berlanjut ke chapter berikutnya...")
    clear_console()
    chapter3(game_state['nama_karakter'])