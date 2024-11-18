import sys
import threading
from InquirerPy import prompt
from src.helper import ensure_checkpoint_dir, save_checkpoint, load_checkpoint, delete_checkpoint, clear_console, play_sound, typewriter, game_over_prompt, process_player_choice
from src.story.chapter4 import chapter_4, chapter_4_event_1,chapter_4_event_2,chapter_4_event_3,chapter_4_event_4,chapter_4_event_5
from src.gameLogic.chapter5_logic import chapter5

# Inisialisasi game_state dari checkpoint jika ada
game_state = load_checkpoint()  # Memuat state dari file checkpoint.json

def display_state(state):
    """Menampilkan lokasi, inventaris, dan progres permainan."""
    print(f"Nama Karakter: {state['nama_karakter']}")
    print(f"Lokasi: {state['location']}")
    print(f"Progres: {state['progres']}\n")

def chapter4(nama_karakter):
    """Mengelola alur chapter 4."""
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
        game_state["location"] = "Pintu Besar"
        game_state["progres"] = "Pintu yang terkunci"
        save_checkpoint(game_state)
    
    # Pilihan aksi pemain
        process_player_choice(
            chapter4_event2, 
            game_state, 
            "Pilih aksi:", 
        [
            {"name": "Meletakkan tangan di atas batu untuk membuka pintu.", "value": "benar"},
            {"name": "Mengabaikan batu dan mencoba mendorong pintu", "value": "salah"}
        ],
        lambda: chapter4_event1(game_state['nama_karakter']),
        display_state
    )
        
def chapter4_event2(nama_karakter):
    global game_state
    for line in chapter_4_event_2(nama_karakter):
        typewriter(line)
        game_state["location"] = "Lorong sempit"
        game_state["progres"] = "Gema di lorong gelap"
        save_checkpoint(game_state)
    
    # Pilihan aksi pemain
        process_player_choice(
            chapter4_event3, 
            game_state, 
            "Pilih aksi:", 
        [
            {"name": "Bergerak cepat ke arah cahaya untuk mencari tahu sumbernya.", "value": "benar"},
            {"name": "Berdiri diam, menunggu suara itu mendekat, yang menyebabkan mereka terjebak dalam perangkap bergerak.", "value": "salah"}
        ],
        lambda: chapter4_event2(game_state['nama_karakter']),
        display_state
    )

def chapter4_event3(nama_karakter):
    global game_state
    for line in chapter_4_event_3(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Jalan Berliku dan Tanda Darah"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Mengikuti jejak darah yang tampaknya menuju ke sebuah pintu besar.", "value": "ikuti"},
        {"name": "Menghindari jejak darah dan mengambil jalur yang tampaknya lebih aman.", "value": "hindari"}
    ]
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Pilih aksi:',
            'choices': options
        }
    ]
    answers = prompt(questions)
    clear_console()

    if answers['action'] == 'ikuti':
        chapter4_event4(game_state['nama_karakter'])
    else:
        chapter4_event4(game_state['nama_karakter'])

def chapter4_event4(nama_karakter):
    global game_state
    for line in chapter_4_event_4(nama_karakter):
        typewriter(line)
        game_state["location"] = "jalan Berliku"
        game_state["progres"] = "Teka-teki Suara"
        save_checkpoint(game_state)
    
    # Pilihan aksi pemain
        process_player_choice(
            end_chapter, 
            game_state, 
            "Pilih aksi:", 
        [
            {"name": "Memecahkan teka-teki dengan benar berdasarkan petunjuk yang ditemukan di dinding", "value": "benar"},
            {"name": "Menebak dengan sembarangan", "value": "salah"}
        ],
        lambda: chapter4_event4(game_state['nama_karakter']),
        display_state
    )

def end_chapter(nama_karakter):
    """Akhiri Chapter 4 dan lanjutkan ke Chapter 5"""
    typewriter("Chapter 4 selesai. Permainan berlanjut ke chapter berikutnya...")
    clear_console()
    chapter5(game_state['nama_karakter'])